import os
import argparse
import hashlib
import threading
from collections import defaultdict
from queue import Queue


rem = Queue(maxsize=0)
sem = threading.Semaphore(value=5)


_file_info = defaultdict(set)
_lock = threading.Lock()


def worker(top):
    while True:
        path = os.path.join(top, rem.get())
        sem.acquire()
        try:
            if os.path.isdir(path):
                for _path in os.listdir(path):
                    if _path.startswith('.'):
                        continue
                    rem.put(os.path.join(path, _path), block=False)
            else:
                hasher = hashlib.md5()
                with open(path, 'rb') as f:
                    hasher.update(f.read())
                with _lock:
                    _file_info[hasher.hexdigest()].add(
                        (path, os.stat(path).st_size)
                    )
        finally:
            sem.release()
            rem.task_done()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d')
    parser.add_argument('-n', type=int)

    args = parser.parse_args()

    for _ in range(args.n):
        threading.Thread(target=worker, args=(args.d,)).start()
    rem.put(args.d)
    rem.join()

    print(_file_info)
