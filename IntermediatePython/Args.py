def test_args(first, *args):
    print('This is first argument {}'.format(first))

    for i in args:
        print('This is other args:{}'.format(i))


def keyword_args(**kwargs):
    for name, value in kwargs.items():
        print("{0}={1}".format(name, value))


def generator_function():
        for i in range(10):
                yield i


if __name__ == '__main__':
    test_args('Ketan', 'Gauri', 'Patel', 'Hello')
    keyword_args(city="chicago")

    for item in generator_function():
            print(item)
