import heapq
import functools
import time
import threading
from datetime import datetime, timedelta
from collections import namedtuple


Task = namedtuple('Task', ['start', 'name', 'fn'])


class Scheduler(object):
    '''Class that schedules functions to be run in a separate thread at some future
    time. Supports cancellation of functions that haven't yet started.
    '''
    def __init__(self):
        self._cv = threading.Condition(threading.Lock())
        self._minheap = []
        self._timeout = None
        self._start_timer()

    def cancel(self, name):
        try:
            with self._cv:
                task = [task for task in self._minheap if task.name == name][0]
        except IndexError:
            return
        else:
            with self._cv:
                self._minheap.remove(task)
                heapq.heapify(self._minheap)
            print('canceled {}'.format(task.name))

    def schedule(self, name, fn, start):
        task = Task(start, name, fn)
        self._cv.acquire()
        heapq.heappush(self._minheap, task)
        if self._minheap[0] == task:
            self._cv.notify()
        self._cv.release()
        print('scheduled task: {}'.format(task.name))

    def _get_next_timeout(self):
        if not self._minheap:
            return None
        return (self._minheap[0].start - datetime.now()).total_seconds()

    def _start_timer(self):
        def run():
            while True:
                self._cv.acquire()
                no_timeout = self._cv.wait(timeout=self._timeout)
                if self._timeout is None:
                    self._timeout = self._get_next_timeout()
                    self._cv.release()
                elif no_timeout:
                    self._timeout = min(self._timeout, self._get_next_timeout())
                    self._cv.release()
                else:
                    # timed out; run a task
                    next_task = heapq.heappop(self._minheap)
                    th = threading.Thread(target=next_task.fn)
                    th.start()
                    self._timeout = self._get_next_timeout()
                    self._cv.release()
                print('next timeout in {} seconds'.format(self._timeout))

        th = threading.Thread(target=run)
        th.start()


def main():
    start = datetime.now()

    def task(name):
        print('running task: {}, elapsed: {}'.format(name, (datetime.now() - start).total_seconds()))

    s = Scheduler()
    s.schedule('task-1', functools.partial(task, 'task-1'), start + timedelta(seconds=1))
    s.schedule('task-2', functools.partial(task, 'task-2'), start + timedelta(seconds=2))
    s.cancel('task-2')
    s.schedule('task-3', functools.partial(task, 'task-3'), start + timedelta(seconds=3))
    # note that task-4 precedes task-3, but is registered after task-3
    s.schedule('task-4', functools.partial(task, 'task-4'), start + timedelta(seconds=2.5))
    time.sleep(5)
    s.schedule('task-5', functools.partial(task, 'task-5'), datetime.now() + timedelta(seconds=5))


if __name__ == '__main__':
    main()
