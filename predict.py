import numpy as np
import sys

EXIT_INPUT = "exit"


def main():
    coefficients = read_coefficients()
    predict_value(coefficients)


def read_coefficients():
    """
    Try reading and storing training information from coefficients.bin.
    """

    try:
        file = open('coefficients.bin', 'r')
        coefficients = np.fromfile(file, dtype=np.float64)
        file.close()
    except Exception:
        print(
            "Training information not available, using [0,0] for coefficients")
        coefficients = np.array([0, 0], dtype=np.float64)
    if coefficients.shape != (2,):
        print("File content is not an array of size 2 with doubles",
              file=sys.stderr)
        exit(1)
    return coefficients


def predict_value(coefficients):
    """
    Infinite loop that takes user input and predicts the car value based
    on the coefficients values obtained from training.
    """

    print(f"Type in '{EXIT_INPUT}' to exit the program")
    while True:
        try:
            user_input = input("Enter the car's km: ")
            km = int(user_input)
        except ValueError:
            if user_input == EXIT_INPUT:
                exit(0)
            print(f"Error: {user_input} is not a number", file=sys.stderr)
            continue
        except KeyboardInterrupt:
            exit(0)
        if km < 0:
            print("Error: A car's km can't be negative", file=sys.stderr)
        else:
            value = int(coefficients[0] + coefficients[1] * km)
            if (value < 0):
                value = 0
            print(f"The predicted value for the car is {value}")


if __name__ == '__main__':
    main()
