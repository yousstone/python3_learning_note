import os
print(range(1,11))
print(list(range(1,11)))

print([x*x for x in range(1,11)])


print([x*x for x in range(1,11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'efg'])

print([d for d in os.listdir('/home/youngstone/project/python')])


print([d for d in os.listdir('.')])

d = {'age':30,'gender':'男','height':175}
d_list = [k+'->'+ str(v) for k,v in d.items()]
print(d_list) 

L = ['HELLO', 'WORLD', 'IBM', 'APPLE']
print([s.lower() for s in L])

L1 = ['HELLO', 'WORLD', 18 ,'IBM', 'APPLE']
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)
