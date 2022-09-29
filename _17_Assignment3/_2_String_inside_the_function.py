str1=input("Enter a message to reverse it:")

def reverse_fun(str2):
    reverse=''
    for i in range(len(str2)-1,-1,-1):
        reverse=reverse+str1[i]
    print("Reversed String is:", reverse)

reverse_fun(str1)