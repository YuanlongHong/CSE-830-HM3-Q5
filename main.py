import matplotlib.pyplot as plt
import time
import random

def insertion_sort(n):
    mylist=[random.randint(0,10000)]
    for i in range(n-1):
        a=random.randint(0,10000)
        j=len(mylist)-1
        mylist.append(0)
        while j>=0 and mylist[j]>a:
            mylist[j+1]=mylist[j]
            j-=1
        mylist[j+1]=a
    return mylist

#define merge sort inner functions
def merge(left,right):
    merged=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def normal_merge_sort(mylist):
    if len(mylist)<=1:
        return mylist
    mid=len(mylist)//2
    left_sort=normal_merge_sort(mylist[:mid])
    right_sort=normal_merge_sort(mylist[mid:])
    return merge(left_sort,right_sort)


#define n size merge sort
def merge_sort(n):
    mylist=[]
    for i in range(n):
        mylist.append(random.randint(0,10000))
    mylist=normal_merge_sort(mylist)
    return mylist


def merge_time(n):
    start=time.time()
    for i in range(100):
        merge_sort(n)
    end=time.time()
    # print('merge sort running seconds:', end-start)
    return end-start


def insertion_time(n):
    start=time.time()

    for i in range(100):
        insertion_sort(n)
    
    end=time.time()
    # print('insertion sort running seconds:', end-start)
    return end-start

def time_result():
    merge_y=[]
    insertion_y=[]
    x=[]
    for i in range(200):
        merge_y.append(merge_time(i))
        insertion_y.append(insertion_time(i))
        x.append(i)

# plt.plot(x,merge_y,x,insertion_y)
# plt.xlabel('list size')
# plt.ylabel('seconds')
# plt.title('Merge Sort vs Insertion Sort(100 times each)')
# plt.show()

# for i in range(200):
#     if insertion_y[i]>merge_y[i] and i>10:
#         print('merge sort is faster when n =', i)
#         break
