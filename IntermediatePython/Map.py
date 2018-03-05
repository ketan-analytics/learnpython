items = [1, 2, 3, 4, 5]
squared =(map(lambda x: x * 2, items))
print(list(squared))


def multiply(x):
        return x*x
def add(x):
    return x+x

func=[multiply,add]

for i in range(5):
    test=list(map(lambda x:x(i),func))
    print(test)


from functools import reduce

result = reduce((lambda x,y:x*y),[1,2,3,4])
print(result)