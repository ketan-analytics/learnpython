class MyString(str):
    def __str__(self):
        return self[::-1]

s=MyString("Hello World")
print(s)

print('Hello World'.casefold())

s1='Hello World'
s2=s1.upper()

print(id(s1))
print(id(s2))