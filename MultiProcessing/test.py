import PrimNumberWithMultiThreading
import time
n=int(input("Enter Number : "))
t=int(input("Enter Theard Count : "))
start_time=time.time()
PrimNumberWithMultiThreading.PrimNumber(n,t)
print("--- %s Seconds ---"%(time.time()-start_time))