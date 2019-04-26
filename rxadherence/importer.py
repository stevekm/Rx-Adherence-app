#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import data from files into the databases.
"""
import os
import sys
import django
import argparse
import csv

# initialize the Django app
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, parentdir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
django.setup()
from rxadherence.models import Drug
sys.path.pop(0)

def import_drugs(import_file):
    """
    Demo test import data into the database
    """
    all_created = []
    num_entries = 0
    with open(import_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            num_entries += 1
            drug_name = row['drug_name']
            instance, created = Drug.objects.get_or_create(name = drug_name)
            if created:
                all_created.append(instance)
    print("Read {0} entries, imported {1} entries.".format(num_entries, len(all_created)))

def main(**kwargs):
    """
    Main control function for the module.
    """
    import_type = kwargs.pop('import_type', None)
    import_file = kwargs.pop('import_file', None)

    print(os.getcwd())

    if import_type == "drug":
        import_drugs(import_file)

def parse():
    """
    Parses script args.
    """
    parser = argparse.ArgumentParser(description='Import data from files into the app database')
    parser.add_argument("--type",
        # default = ,
        dest = 'import_type',
        help="Type of data to import")
    parser.add_argument("--file",
        dest = 'import_file',
        help="File to import from")
    args = parser.parse_args()
    main(**vars(args))

if __name__ == '__main__':
    parse()
