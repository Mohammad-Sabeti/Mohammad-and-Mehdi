import threading
import queue


exitFlag=0

class myTheard(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.q=q


    def run(self):
        print("Starting "+self.name)
        process_data(self.name,self.q)
        print("Exiting "+self.name)

def process_data(threadName,q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data=q.get()
            queueLock.release()
            print("%s processing %s " % (threadName, data))
        else:
            queueLock.release()
        for j in range(10000):
            if (countDivisors(j)):
                print("%s  ===>>>  %s " % (threadName, j))


def countDivisors(n):
    sum = 1
    for i in range(2, (int)(n**0.5)+1):
        if (n % i == 0):
            sum += i

            if (n / i != i):
                sum += (n / i)

    if (sum == n):
        return True
    return False


# Start Main Thread
threadList=["Thread-1","Thread-2","Thread-3","Thread-4"]
nameList=["One","Two","Three","Four"]

queueLock=threading.Lock()
workQueue=queue.Queue(10)
threads=[]
threadID=1

for tName in threadList:
    thread=myTheard(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID+=1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)

queueLock.release()

while not workQueue.empty():
    pass

exitFlag=1

for t in threads:
    t.join()


print("Exiting Main Thread ")


# End Main Thread




