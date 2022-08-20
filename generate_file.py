import pandas as pd
import sys

if __name__ == '__main__':
    n = None
    try:
        n = sys.argv[1]
        n = int(n)
        assert n > 0
    except IndexError:
        print('Provide number to generate')
        exit(1)
    except ValueError:
        print('Provide number as argument')
        exit(1)
    except AssertionError:
        print('Provide positive number')

    numbers = pd.Series(data = list(range(1, n + 1)), name = 'numbers')
    numbers.to_csv('numbers.csv', index = False)    
