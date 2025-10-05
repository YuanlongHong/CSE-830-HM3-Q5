import main

total_list=[]
for i in range(10):
    for j in range(200):
        if main.merge_time(j) < main.insertion_time(j) and j > 10:
            break
    total_list.append(j)
total_list.sort()
result = total_list[5]
print('merge sort is faster when n =', result)