import numpy as np
import sys


def main():
    # Read thetha from training
    thetha = read_thetha()
    print(thetha)


def read_thetha():
    try:
        file = open('thetha.bin', 'r')
        thetha = np.fromfile(file, dtype=np.float64)
        file.close()
    except Exception:
        thetha = np.array([0, 0], dtype=np.float64)
    if thetha.shape != (2,):
        print("File content is not an array of size 2 doubles",
              file=sys.stderr)
        exit(1)
    return thetha


if __name__ == '__main__':
    main()
