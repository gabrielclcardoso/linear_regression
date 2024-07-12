import pandas as pd
import sys
from array import array

# Read Database
try:
    data = pd.read_csv('data.csv')
except Exception as e:
    print(e, file=sys.stderr)
    exit(1)

# Gradient descent
thetha = array('d', [0, 1])
tmp_thetha = array('d', thetha)
learning_rate = 0.1  # What value shoud be put here?
max_iterations = 1e5  # What value shoud be put here?
iterations = 0
for i in data.itertuples():
    tmp_thetha[0] = thetha[0]  # formula with thetha0
    tmp_thetha[1] = thetha[1]  # formula with thetha1
    # check step size
    thetha[0] = tmp_thetha[0]
    thetha[1] = tmp_thetha[1]
    iterations += 1
    if iterations == max_iterations:
        break
