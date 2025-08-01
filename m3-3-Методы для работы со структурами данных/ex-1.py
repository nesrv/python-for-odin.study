list_ = [1,2,3,4]
tuple_ = (1,2,3,4)
set_ = {1,2,3,4}
str_ = "1234"


list_ += [5]
tuple_ += (5,)
set_ |= {5}
str_ += "5"


# print(list_, tuple_, set_, str_, sep="\n")

for item in {1, 2, 3}:
    print(item)