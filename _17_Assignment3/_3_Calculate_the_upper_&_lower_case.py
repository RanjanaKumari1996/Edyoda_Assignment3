str1=input("Please enter a message:")

upper_counter=0
lower_counter=0
for i in str1:
    if i.isupper():
        upper_counter+=1
    elif i.islower():
        lower_counter+=1
    else:
        pass
print("Original Message is:", str1)
print("Number of upper case characters are:", upper_counter)
print("Number of lower case characters are:", lower_counter)