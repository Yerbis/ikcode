# Class thing

class CountFromBy:
    pass

a = CountFromBy()
b = CountFromBy()

c = CountFromBy()

c.increase()
c.increase()
c.increase()

print(c)

d = CountFromBy(100)

d.increase()
d.increase()
d.increase()
   
print(d)

e = CountFromBy(100, 10)

for i in range(3):
    e.increase()

f = CountFromBy(increment=15)

for j in range(3):
    f.increase()