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


class Scheduler:
    """A schedule of tasks to be run in background threads. Call the
    schedule method to schedule a task to run at a particular time.
    Call the task's cancel method to cancel it if it has not already
    started running.

    """

    @functools.total_ordering
    class _Task:
        "A scheduled task."

        def __init__(self, fn, start):
            "Create task that will run fn at or after the datetime start."
            self.fn = fn
            self.start = start
            self.cancelled = False

        def __le__(self, other):
            # Tasks compare according to their start time.
            return self.start <= other.start

        @property
        def timeout(self):
            "Return time remaining in seconds before task should start."
            return (self.start - datetime.now()).total_seconds()

        def cancel(self):
            "Cancel task if it has not already started running."
            self.cancelled = True
            logger.info("canceled %s", self)

    def __init__(self):
        cv = self._cv = threading.Condition(threading.Lock())
        tasks = self._tasks = []

        def run():
            while True:
                with cv:
                    while True:
                        timeout = None
                        while tasks and tasks[0].cancelled:
                            heapq.heappop(tasks)
                        if tasks:
                            timeout = tasks[0].timeout
                            if timeout <= 0:
                                task = heapq.heappop(tasks)
                                break
                        cv.wait(timeout=timeout)
                logger.info("starting task %s", task)
                threading.Thread(target=task.fn).start()

        threading.Thread(target=run, name='Scheduler').start()

    def schedule(self, fn, start):
        """Schedule a task that will run fn at or after start (which must be a
        datetime object) and return an object representing that task.

        """
        task = self._Task(fn, start)
        logger.info("scheduling task %s", task)
        with self._cv:
            heapq.heappush(self._tasks, task)
            self._cv.notify()
        logger.info("scheduled task %s", task)
        return task


def main():
    logging.basicConfig(level=logging.INFO, format='%(threadName)-10s: %(message)s')

    start = datetime.now()

    def task():
        logger.info('running, elapsed: {}'.format((datetime.now() - start).total_seconds()))

    s = Scheduler()
    s.schedule(functools.partial(task), start + timedelta(seconds=1))
    t = s.schedule(functools.partial(task), start + timedelta(seconds=2))
    t.cancel()
    s.schedule(functools.partial(task), start + timedelta(seconds=3))
    # note that task-4 precedes task-3, but is registered after task-3
    s.schedule(functools.partial(task), start + timedelta(seconds=2.5))
    time.sleep(5)
    now = datetime.now()
    s.schedule(functools.partial(task), now + timedelta(seconds=5))
    s.schedule(functools.partial(task), now + timedelta(seconds=4))
    s.schedule(functools.partial(task), now + timedelta(seconds=3.5))


if __name__ == '__main__':
    main()
