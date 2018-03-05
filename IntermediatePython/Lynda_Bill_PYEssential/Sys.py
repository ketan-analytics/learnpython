#!/usr/bin/env python3

import sys
import os
import datetime

def main():
    v=sys.version_info
    print(type(v))
    print('Python version {}.{}.{}'.format(*v))

    p = sys.platform
    print(type(v))
    print('Python version {}.{}.{}'.format(*p))

    print(os.getcwd())

    now=datetime.datetime.now()
    print(now)

if __name__ == '__main__':
    main()