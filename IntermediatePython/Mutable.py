def add_to(num, target=[]):
    target.append(num)
    print(target)
    return target


add_to(1)
# Output: [1]

add_to(2)
# Output: [1, 2]

add_to(3)


# Output: [1, 2, 3]



def add_to_new(num, target=None):
    if target is None:
        target = []
    target.append(num)
    print(target)
    return target

add_to_new(1)
# Output: [1]

add_to_new(2)
# Output: [1, 2]

add_to_new(3)
# Output: [1, 2, 3]
