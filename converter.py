#!/usr/bin/env python3

import argparse
import json

data_file = './data.json'

class currency:
    def __init__(self, filename):
        self.filename = filename
        self.rounding = 2
        self.data = None
        self.load()

    def load(self):
        with open(self.filename) as f:
            self.data = json.load(f)

    def rounder(self, value, r=False):
        value = round(value, self.rounding)
        value = str(value).split('.')
        value[1] = value[1] if len(value[1]) == 2 else f'{value[1]}0'
        return '.'.join(value)

    def get(self, origin):
        return self.list()[origin]

    def list(self):
        return self.data['currencies']

    def conversion(self, origin):
        return float(self.get(origin=origin)['usd'])

    def description(self, origin):
        return self.get(origin=origin)['description']

    def short_description(self, origin):
        return self.get(origin=origin)['short']

    def to_usd(self, origin, value):
        return value * self.conversion(origin=origin)

    def from_usd(self, origin, value):
        return value / self.conversion(origin=origin)

    def to_human(self, origin, value, f):
        return self.rounder(f(origin=origin, value=value))

    def to_usd_human(self, origin, value):
        out = self.to_human(origin=origin, value=value, f=self.to_usd)
        return f'US${out}'

    def from_usd_human(self, origin, value):
        out = self.to_human(origin=origin, value=value, f=self.from_usd)
        return f'{out} {self.short_description(origin=origin)}'

def show_currencies(c):
    o = []
    for _c in sorted(c.list().keys()):
        o.append(f'"{_c}" ({c.short_description(origin=_c)})')
    return ', '.join(o)

def check_code(c, code):
    if code not in c.list():
        print(f'Code "{code}" is invalid.')
        quit()
    else:
        print(f'Currency: {c.description(origin=code)}\n')

def convert_to(c, code, value):
    check_code(code=code, c=c)
    v = c.to_usd_human(origin=code, value=value)
    print(f'{c.rounder(value)} {c.short_description(origin=code)} converts to {v}\n')
    quit()

def convert_from(c, code, value):
    check_code(code=code, c=c)
    v = c.from_usd_human(origin=code, value=value)
    print(f'US${c.rounder(value)} converts to {v}\n')
    quit()

if __name__ == '__main__':
    print(f'Cariad\'s pointless game currency converter\n(c) 2021 Cariad Keigher <cariad@keigher.ca>\n')
    c = currency(filename=data_file)
    p = argparse.ArgumentParser()
    p.add_argument('value', metavar='VALUE', type=float,
                    help='Input value of whatever currency')
    p.add_argument('currency', metavar='CURRENCY', type=str, 
                    help='Game currency code you wish to use - ' + show_currencies(c=c))
    p.add_argument('--usd', dest='from_usd', action='store_true', 
                    help='Convert from US dollars instead (default is to)')
    p.set_defaults(from_usd=False)
    a = p.parse_args()
    if a.from_usd:
        convert_from(c=c, code=a.currency, value=a.value)
    else:
        convert_to(c=c, code=a.currency, value=a.value)