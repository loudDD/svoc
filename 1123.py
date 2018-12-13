
def add(x,y):
    return x + y

num = [1,2,3,4]
b = list(map((lambda x,y: x + y),(num),[1,2,3,4]))
print(b)