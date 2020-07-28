# -*- coding: utf-8 -*-
from datetime import datetime
import re

class LedgerEntry(object):
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry


def format_entries(currency, locale, entries):
    header_formatter = '{:<10s} | {:<25s} | {:<13s}'
    entry_formatter = '{:<10s} | {:<25s} | {:>13s}'

    entries.sort(key=lambda e: (e.date, e.change))
    currency_sign = '$' if currency == 'USD' else (u'€' if currency == 'EUR' else '')
    if locale == 'en_US':
        header = header_formatter.format('Date', 'Description', 'Change')
        date_formater = '%m/%d/%Y'
    elif locale == 'nl_NL':
        header = header_formatter.format('Datum', 'Omschrijving', 'Verandering')
        date_formater = '%d-%m-%Y'
    table = header

    for entry in entries:
        table += '\n'

        # Write entry date to table
        date_str = entry.date.strftime(date_formater)

        # Write entry description to table
        # Truncate if necessary
        entry_des = entry.description if len(entry.description) <= 25 else entry.description[:22] + '...'

        # Write entry change to table
        change_amt = abs(entry.change) / 100
        if entry.change < 0:
            if locale == 'nl_NL':
                change_str = f'{currency_sign}-{change_amt:,.2f} '
            elif locale == 'en_US':
                change_str = f'({currency_sign}{change_amt:,.2f})'
        else:
            change_str = f'{currency_sign}{change_amt:,.2f} '
        if locale == 'nl_NL':
            change_str = re.sub(',', '|', change_str)
            change_str = re.sub(r'\.', ',', change_str)
            change_str = re.sub(r'\|', '.', change_str)
            change_str = re.sub(r'(.)(.*)$', r'\g<1> \g<2>', change_str)
        
        table += entry_formatter.format(date_str, entry_des, change_str)
    return table
    