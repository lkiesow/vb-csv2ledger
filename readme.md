Volksbank CSV Export ro Ledger Conversion
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

% ledger -f xy.ledger print                                                                                                                                 (git)-[master] [1] 
1970/01/01 Initial ammount
    assets:123456678                     1234.56 EUR
    throughput:init

...
```

Configuration
-------------

Initial balances can be specified for accounts. Take a look at `config.yml` for
an example.
