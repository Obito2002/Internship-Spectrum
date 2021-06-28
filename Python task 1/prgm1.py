#Q.no -> 1
#To invert the given string of characters  :
def upper_to_lower(value):
    for i in range(len(value)):
        if ord(value[i])>=97 and ord(value[i])<=122:
            value[i] = chr(ord(value[i])-32)
        elif ord(value[i])>=65 and ord(value[i])<=90:
            value[i] = chr(ord(value[i])+32)
    return value

#driver code:
value = input("Enter the string to be iverted")
value=list(value)
value=upper_to_lower(value)
value="".join(value)
print(value)

    