from collections import OrderedDict
from collections import Counter

colors = OrderedDict([("Red",198),("Blue",199),("Pink",200)])

for key,value in colors.items():
    print(key,value)


colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
    )

favs = Counter(name for name,value in colours)
print(favs)



my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)