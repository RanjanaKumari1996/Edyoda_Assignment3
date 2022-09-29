str1=input("Enter a message to reverse it:")
reverse=''
for i in range(len(str1)-1,-1,-1):
    reverse=reverse+str1[i]
print("Reversed String is:", reverse)