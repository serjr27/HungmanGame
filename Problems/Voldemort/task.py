import random


# work with this variable
n = int(input())
random.seed(n)
str_ = "Voldemort"
print(str_[random.randint(0, len(str_) - 1)])
