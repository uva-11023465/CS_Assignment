import csv
import sys

import matplotlib.pyplot as plt


def main(filename):
    headers = None
    data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\ufeff').strip()
            if len(line) == 0:
                continue
            line = line.split(';')
            if headers is None:
                headers = line
                continue
            data.append(dict(zip(headers, line)))
    print(data)
    plt.plot(
        [int(d['Year']) for d in data],
        [float(d['WO [x1000]'].replace(',', '.')) for d in data]
    )
    plt.title('WO')
    plt.xlabel('year')
    plt.ylabel('WO [x1000]')
    plt.savefig('graph1.png')
    plt.plot(
        [int(d['Year']) for d in data],
        [float(d['NL Beer consumption [x1000 hectoliter]'].replace(',', '.')) for d in data]
    )
    plt.title('NL Beer consumption')
    plt.xlabel('year')
    plt.ylabel('NL Beer consumption [x1000 hectoliter]')
    plt.savefig('graph2.png')

if __name__ == '__main__':
    main(sys.argv[1])

