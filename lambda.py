from functools import reduce
#Lambda Function
sq = (lambda x : 2*x)
add = lambda x,y: x+y
mx = lambda x,y: x if x > y else y
print(sq(2))
print(add(2,3))
print(mx(8,5))

#Map
n = [4,3,2,1]
print(list(map(lambda x: x**2, n)))

#Filter
print(list(filter(lambda x: x>2, n)))

#REduce
print(reduce(lambda x,y:x*y,n))