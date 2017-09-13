from collections import Iterable,Iterator

print('Is list iterable:',isinstance([],Iterable))
print('Is tuple iterable:',isinstance((),Iterable))
print('Is an str iterable:',isinstance('abc',Iterable))
print('Is dic iterable:',isinstance({},Iterable))

print('-'*100)

print('Is list an iterator:',isinstance([],Iterator))
print('Is tuple an iterator:',isinstance((),Iterator))
print('Is an str an iterator:',isinstance('abc',Iterator))
print('Is dic an iterator:',isinstance({},Iterator))

print('Is [x for x in range(1,11)] an iterator:',isinstance([x for x in range(1,11)],Iterator))

print('Is (x for x in range(1,11)) an iterator:',isinstance((x for x in range(1,11)),Iterator))
