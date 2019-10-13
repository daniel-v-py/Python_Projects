n = int(input("Please enter a number : "))
print("Type of data : " , type(n))
n1 = n
n2 = int("%s%s" % (n , n))
n3 = int("%s%s%s" % (n , n , n))
print(n+n2+n3)
