#!/usr/bin/env python3
import sys


def main(infiles):
    rawdata = set()
    for infile in infiles:
        with open(infile, 'rb') as f:
            line = f.readline()
            while line:
                rawdata.add(line)
                line = f.readline()
    header = ''
    data = {}
    for line in rawdata:
        sline = line.decode('latin1')
        if not sline[0].isdigit():
            header = line
            continue
        no, date, _ = sline.split(';', 2)
        date = date.split('.')
        date = ''.join(date[::-1])
        if no not in data.keys():
            data[no] = []
        data[no].append((date, line))
    for no, kdata in data.items():
        kdata.sort(key=lambda x: x[0])
        first = kdata[0][0]
        last = kdata[-1][0]
        filename = '%s-%s-%s.csv' % (no, first, last)
        print('Writing %s' % filename)
        with open(filename, 'wb') as f:
            f.write(header)
            for line in kdata:
                f.write(line[1])


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: %s infile.csv [infile2.csv ...]' % sys.argv[0])
    main(sys.argv[1:])
