#!/usr/bin/env python3

import argparse
import csv
import re
import yaml

ENTRY = '''
%(date)s %(comment)s
    assets:%(account)s    %(amount)s %(currency)s
    throughput:%(recipient)s
'''

def main(config, infiles):

    data = set()

    transactions = []

    if config:
        with open(config, 'r') as f:
            config = yaml.load(f)
    else:
        config = {}

    # Initialize accounts
    for name, account in config.get('accounts', {}).items():
        transactions.append({
            'account': name,
            'date': '1970/01/01',
            'recipient': 'init',
            'comment': 'Initial ammount',
            'amount': account.get('amount', 0),
            'currency': account.get('currency', 'EUR')
            })
    for transaction in transactions:
        data.add(ENTRY % transaction)

    # Go through CSV files
    for infile in infiles:
        with open(infile, 'rb') as csvfile:
            content = csvfile.read().decode('latin1').split('\n')
            reader = csv.reader(content, delimiter=';', quotechar='"')
            for row in reader:
                if not row or row[0] == 'Kontonummer':
                    continue

                # prepare date
                d = row[1].split('.')

                transaction = {
                        'account': row[0],
                        'date': '%s/%s/%s' % (d[2], d[1], d[0]),
                        'recipient': re.sub('   *', ' ', row[3]),
                        'comment': re.sub('   *', ' ', ' '.join(row[5:19])),
                        'amount': row[19],
                        'currency': row[21]
                        }

                data.add(ENTRY % transaction)

    # Print data
    print(''.join(sorted(data)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Volksbank to ledger.')
    parser.add_argument('csvfiles', nargs='+',
                        help='Volksbank CSV export files')
    parser.add_argument('-c', '--config', dest='config',
                        help='Configuration file')
    args = parser.parse_args()
    main(args.config, args.csvfiles)
