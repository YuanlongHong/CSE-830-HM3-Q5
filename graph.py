import matplotlib.pyplot as plt
import main



merge_y=[]
insertion_y=[]
x=[]
for i in range(200):
    merge_y.append(main.merge_time(i))
    insertion_y.append(main.insertion_time(i))
    x.append(i)



plt.plot(x,merge_y,x,insertion_y)
plt.xlabel('list size')
plt.ylabel('seconds')
plt.title('Merge Sort vs Insertion Sort(100 times each)')
plt.show()



