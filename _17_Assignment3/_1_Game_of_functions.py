num=int(input("enter the range of a list:"))
lst=[]
for i in range(num):
    item=int(input("Enter element:"))
    lst.append(item)

#print(lst)

def sum_lst(l1):
    sum=0
    for i in range(num):
        sum=sum+l1[i]
    print("Sum of List elements is:", sum)

sum_lst(lst)