from heapq import heappop, heappush  
print('Введите кол-во элементов списка: ')
a=int(input())

list1=[0]*a
for i in range(len(list1)):
    print('Введите значение',i+1,'элемента списка :')
    list1[i]=input()

print('Исходный список: \n',list1)
          
def bucket_sort(list1):
    m=float(max(list1))
    r=m/len(list1)
    

    list2=[]
    for i in range(len(list1)):
        list2.append([])

    for j in range(len(list1)):
        k=int(float(list1[j]) / r)
        if k!=len(list1):
            list2[k].append(list1[j])
        else:
            list2[len(list1)-1].append(list1[j])

    for q in range(len(list1)):
        list2[q]=sorted(list2[q])

    list3=[]
    for w in range(len(list1)):
        list3=list3+list2[w]
    return list3
def heapsort(list1):
    heap=[]
    for i in list1:
        heappush(heap,i)

    list2=[]

    while heap:
        list2.append(heappop(heap))
    return list2

print('Выбкрите метод сортировки:\n1.Блочная \n2.Пирамидальная')
a=int(input())
if a==1:
    flist=bucket_sort(list1)
elif a==2:
    flist=heapsort(list1)
else:
    print('Попробуйе еще раз')
print('Отсоритрованный список: \n', flist)
    
