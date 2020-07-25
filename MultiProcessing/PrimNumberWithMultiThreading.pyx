import threading
def threadfunction(int s , int e):
    cdef unsigned int i
    for i in range(s,e):
        if IsPrimNumber(i):
            print(i)


def PrimNumber (int n, int t):
    cdef unsigned int i,l,s,e
    l=int(n/t)
    s,e=1,l
    theards=[]
    for i in range(t):
        theards.append(threading.Thread(target=threadfunction,args=(s,e)))
        theards[i].start()
        s+=1
        e+=1

    for theard in theards:
        theard.join()


cdef inline int IsPrimNumber(int n) nogil:
    cdef unsigned int i
    for i in range(2,n/2):
        if n%i==0:
            return 0
    return 1