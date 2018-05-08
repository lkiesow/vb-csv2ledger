Volksbank CSV Export to Ledger Conversion
=========================================

This script converts bank transaction exported via the Volksbank's web
interface as CSV file to ledger files. Duplicate entries are removed
automatically and the output is sorted by date.

Usage
-----

```
usage: vb-csv2ledger.py [-h] [-c CONFIG] csvfiles [csvfiles ...]

Volksbank to ledger.

positional arguments:
  csvfiles              Volksbank CSV export files

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Configuration file
```

Example
-------

```
% ./vb-csv2ledger.py -c config.yml .../umsaetze/*.csv

1970/01/01 Initial ammount
    assets:123456678    1234.56 EUR
    throughput:init

...

% ./vb-csv2ledger.py -c config.yml .../umsaetze/*.csv > xy.ledger

% ledger -f xy.ledger print
1970/01/01 Initial ammount
    assets:123456678                     1234.56 EUR
    throughput:init

...
```

Configuration
-------------

Initial balances can be specified for accounts. Take a look at `config.yml` for
an example.


Merge CSV Files
---------------

The additional tool `vb-uniq-transactions.py` can merge several exported CSV
files ensuring that each transaction is listed only once. This is helpful since
the timespan of exported transactions may easily overlap.

The script will produce separate files for each account listed in the set of CSV
files. They are named in the form of `<account_no>-<start_date>-<end_date>.csv`.

Example:

```bash
% ./vb-uniq-transactions.py file1.csv file2.csv
Writing 231767402-20170601-20180425.csv
Writing 231767403-20170829-20180425.csv
Writing 231767405-20170428-20170428.csv
```
