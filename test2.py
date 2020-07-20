import threading
import time
exitFlag=0

class myTheard(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter


    def run(self):
        print("Starting "+self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        print("Exiting "+self.name)
        threadLock.release()


def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("%i %s: %s "% (counter,threadName,time.ctime(time.time())))
        counter-=1




# Main Thread
threadLock=threading.Lock()
threads=[]

theard1=myTheard(1,"Thread-1",1)
theard2=myTheard(2,"Thread-2",2)
theard3=myTheard(3,"Thread-3",3)
theard4=myTheard(4,"Thread-4",4)
theard5=myTheard(5,"Thread-5",5)


theard1.start()
theard2.start()
theard3.start()
theard4.start()
theard5.start()


threads.append(theard1)
threads.append(theard2)
threads.append(theard3)
threads.append(theard4)
threads.append(theard5)

for t in threads:
    t.join()

print("Exiting Main Thread ")

# Main Thread


