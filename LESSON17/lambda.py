from functools import reduce
def triple(x): return x * x * x
# lambda x : x * x


print(triple(3))


def addTwo(x): return x + 2
# lambda x : x + 2


print(addTwo(8))


def sum(a, b): return a + b
# lambda a, b : a + b


print(sum(4, 5))

#####################################


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(9))
print(addTwenty(9))

############################
# Higher Order function

numbers = [2, 3, 4, 5, 6, 7]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

#############################
odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))


###########################

total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)


####################
# total characters count

names = ["Abhsihek", "Adhikari", "Zuzu", "Gold"]


char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
