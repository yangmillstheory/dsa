import heapq
import logging
import functools
import time
import threading
from datetime import datetime, timedelta
from collections import namedtuple


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

Task = namedtuple('Task', ['start', 'name', 'fn'])


class Scheduler(object):
    '''Class that schedules functions to be run in a separate thread at some future
    time. Supports cancellation of functions that haven't yet started.
    '''
    def __init__(self):
        self._cv = threading.Condition(threading.Lock())
        self._minheap = []
        self._timeout = None
        self._start()

    def cancel(self, name):
        with self._cv:
            try:
                task = [task for task in self._minheap if task.name == name][0]
            except IndexError:
                return
            self._minheap.remove(task)
            heapq.heapify(self._minheap)
        logger.info('canceled {}'.format(task.name))

    def schedule(self, name, fn, start):
        task = Task(start, name, fn)
        logger.info('scheduling task: {}'.format(name))
        with self._cv:
            heapq.heappush(self._minheap, task)
            self._cv.notify()
        logger.info('scheduled task: {}'.format(name))

    def _get_next_timeout(self):
        if not self._minheap:
            return None
        return (self._minheap[0].start - datetime.now()).total_seconds()

    def _start(self):
        def run():
            while True:
                self._cv.acquire()
                logger.info('waiting with timeout: {}'.format(self._timeout))
                not_expired = self._cv.wait(timeout=self._timeout)
                if self._timeout is None:
                    logger.info('no timeout found; using min element')
                    self._timeout = self._get_next_timeout()
                    self._cv.release()
                elif not_expired:
                    logger.info('already waiting but woken up; comparing current with min element')
                    self._timeout = min(self._timeout, self._get_next_timeout())
                    self._cv.release()
                else:
                    logger.info('timed out; running next task')
                    next_task = heapq.heappop(self._minheap)
                    self._timeout = self._get_next_timeout()
                    self._cv.release()
                    threading.Thread(target=next_task.fn, name=next_task.name).start()

        threading.Thread(target=run, name='timer').start()


def main():
    logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')

    start = datetime.now()

    def task(name):
        logger.info('running task: {}, elapsed: {}'.format(name, (datetime.now() - start).total_seconds()))

    s = Scheduler()
    s.schedule('task-1', functools.partial(task, 'task-1'), start + timedelta(seconds=1))
    s.schedule('task-2', functools.partial(task, 'task-2'), start + timedelta(seconds=2))
    s.cancel('task-2')
    s.schedule('task-3', functools.partial(task, 'task-3'), start + timedelta(seconds=3))
    # note that task-4 precedes task-3, but is registered after task-3
    s.schedule('task-4', functools.partial(task, 'task-4'), start + timedelta(seconds=2.5))
    time.sleep(5)
    now = datetime.now()
    s.schedule('task-5', functools.partial(task, 'task-5'), now + timedelta(seconds=5))
    s.schedule('task-6', functools.partial(task, 'task-6'), now + timedelta(seconds=4))
    s.schedule('task-7', functools.partial(task, 'task-7'), now + timedelta(seconds=3.5))
    s.cancel('task-6')


if __name__ == '__main__':
    main()
