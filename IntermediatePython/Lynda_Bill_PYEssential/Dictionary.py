def main():
    animals = dict(kittne='mew', puppy='bark', lion='grr')
    print_dict(animals)


def print_dict(o):
    for k,v in o.items():
        print(f'{k}:{v}')





if __name__ == '__main__':
        main()
