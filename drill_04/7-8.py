import time

class StopWatch:
    def __init__(self):
        self.__starttime = time.time()

    def getstarttime(self):
        return self.__starttime

    def getendtime(self):
        return self.__endtime

    def start(self):
        self.__starttime = time.time()

    def stop(self):
        self.__endtime = time.time()

    def getelaspsedtime(self):
        return int((self.__endtime - self.__starttime) * 1000)

s = StopWatch()
sum = 0
for i in range(1,10000001):
    sum += 1
s.stop()
print('1부터 100만까지 더하는데 걸린 시간 : {0}ms'.format(s.getelaspsedtime()))