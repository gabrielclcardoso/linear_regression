import pandas as pd
import sys

try:
    data = pd.read_csv('data.csv')
    print(data)
except Exception as e:
    print(e, file=sys.stderr)
