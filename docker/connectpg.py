#!/env/bin python
import sys
import time

import psycopg2


def main(url):
    while True:
        try:
            psycopg2.connect(url).close()
        except Exception:
            print('Waiting for postgres at {}'.format(url))
            time.sleep(3)
        else:
            print('Connected to postgres at {}'.format(url))
            break


if __name__ == '__main__':
    main(sys.argv[1])
