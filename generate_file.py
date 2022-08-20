from asyncssh import OPEN_REQUEST_PTY_FAILED
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

    numbers = pd.Series(data = {'numbers': range(1, n + 1)})
    numbers.to_csv('numbers.csv')    