import clize
import csv
from datetime import datetime

REVOLUT_ACCOUNT = 'Assets:Revolut:Euro'

def format_date(revolut_stamp):
    in_fmt = '%d %b %Y'
    out_fmt = '%Y/%m/%d'
    return (datetime.strptime(revolut_stamp.strip(), in_fmt)
                    .strftime(out_fmt))

def to_hledger(is_incoming, date, ref, amount):
    to_acc, from_acc = ((REVOLUT_ACCOUNT, f'Income:{ref}')
                        if is_incoming
                        else (f'Expenses:{ref}', REVOLUT_ACCOUNT))

    if replace_comma:
    neg_amount = f"-{amount}"
    return f"""{date} {ref.strip()}
    {to_acc:34}    {amount:>10}
    {from_acc:34}    {neg_amount:>10}\n"""


def parse(revolut_csv):
    for date, ref, paid_out, paid_in, _exch_out, _exch_in, _bal, *opt in revolut_csv:
        if len(opt) >= 2:
            ref = f"{ref.strip()} ({opt[1].strip()})"

        is_incoming = bool(paid_in)
        stamp = format_date(date)
        amount = paid_in.strip() if is_incoming else paid_out.strip()
        yield is_incoming, stamp, ref, amount


def main(infile):
    with open(infile, 'r') as csvfile:
        lines = reversed(list(csvfile)[1:])
        reader = csv.reader(lines, delimiter=';')

    for entry in parse(reader):
        print(to_hledger(*entry))

if __name__ == '__main__':
    clize.run(main)
