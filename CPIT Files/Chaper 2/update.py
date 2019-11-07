import time
import sys
import threading


def update(i, last_time=time.time()-1):
    sys.stdout.write(str(i)+'\r')
    sys.stdout.flush()
    print()
    i += 1
    cur_time = time.time()
    threading.Timer(2-(cur_time-last_time), update, [i, cur_time]).start()


