a = set()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(6)
a.add(6)
b = set()
b.add("Nurik")
b.add("yyh")
a.pop()
a.remove(6)
b.discard("yyh")
a.clear()
b.clear()
c = a.union(b)
print(a)
print(b)
print(c)