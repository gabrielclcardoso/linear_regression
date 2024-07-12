import numpy as np
import sys


def main():
    # Read thetha from training
    try:
        file = open('thetha.bin', 'r')
        thetha = np.fromfile(file, dtype=np.float64)
        file.close()
        if thetha.shape != (2,):
            raise ValueError("File content is not an array of size 2 doubles")
    except Exception as e:
        print(e, file=sys.stderr)
        exit(1)

    print(f'thetha values = {thetha}')


if __name__ == '__main__':
    main()
