import time
import sys
import threading

totalSeconds = int(time.time())
totalMinutes = int(totalSeconds // 60)
totalHours = int(totalMinutes // 60)

currentSeconds = int(totalSeconds % 60)
currentMinutes = int(totalMinutes % 60)
currentHours = int(totalHours % 24)

print(str(currentHours) + ":" + str(currentMinutes) + ":" + str(currentSeconds) + " GMT")

'''
def update(i, last_time=time.time()-1):
    sys.stdout.write(str(i)+'\r')
    sys.stdout.flush()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    totalSeconds = int(time.time())
    totalMinutes = int(totalSeconds // 60)
    totalHours = int(totalMinutes // 60)

    currentSeconds = int(totalSeconds % 60)
    currentMinutes = int(totalMinutes % 60)
    currentHours = int(totalHours % 24)

    print(str(currentHours) + ":" + str(currentMinutes) + ":" + str(currentSeconds) + " GMT")
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    i += 1
    cur_time = time.time()
    threading.Timer(2-(cur_time-last_time), update, [i, cur_time]).start()



update(0)
'''

# print(totalTime)
# 1 year = 365 days
# 1 day  = 24 hours
# 1 hour = 60 minutes
# 1 minute = 60 seconds
