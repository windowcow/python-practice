import gc

# 이렇게 같은 내용을 가지는 object들은 id들이 전부 같다.

hash([2, 3, 4])
print(id((2, 3, 4)))
print(id([2, 3, 4]))
print(id([2, 3, 4]))
print(id([2, 3, 4]))
print(id([2, 3, 4]))
gc.collect()

a = (2, 3, 4)
print(id(a))


a = (1, 2, 3)
a1 = (1, 2, 3)
b = [2, 3, 4]


print(a.__hash__())

print(id(a))
print(id(a1))
print(id((1, 2, 3)))
