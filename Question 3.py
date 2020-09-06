x = input()
n = int(input())
list1 = [x]
a = x.split(sep = ' ')
del a[n]
print (*a)
