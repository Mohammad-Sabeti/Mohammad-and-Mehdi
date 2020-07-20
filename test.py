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
        print_time(self.name,5,self.counter)
        print("Exiting "+self.name)

def print_time(threadName,n,delay):
    counter=1
    while counter<=n:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%i %s: %s "% (counter,threadName,time.ctime(time.time())))
        counter+=1




# Main Thread
theard1=myTheard(1,"Thread-1",1)
theard2=myTheard(2,"Thread-2",2)


theard1.start()
theard2.start()


print("Exiting Main Thread ")

# Main Thread 


