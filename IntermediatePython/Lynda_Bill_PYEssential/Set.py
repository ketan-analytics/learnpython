

def main():
   seq=range(11)
   from math import pi
   seq2=[(x,x*2) for x in seq]
   seq3=[round(pi,i) for i in seq]
   seq4={x:x**2 for x in seq}
   print(seq)
   print(seq2)
   print(seq3)
   print(seq4)


if __name__ == '__main__':
    main()