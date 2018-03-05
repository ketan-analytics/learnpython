
def main():
    game = ('Ketan', 'Gauri', 'Vivaan', 'Kyara')

    print(','.join(game))
    print_list(game)

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
        print()

if __name__ == '__main__': main()
