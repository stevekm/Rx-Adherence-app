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
from rxadherence.models import User
from rxadherence.models import Usage
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

def import_user(username):
    instance, created = User.objects.get_or_create(username = username)
    if created:
        print("Successfully created user: {0}".format(username))
    else:
        print("ERROR: could not create user: {0}".format(username))

def import_usage(username, drug_id):
    """
    """
    user_instance = User.objects.get(username = username)
    drug_instance = Drug.objects.get(id = int(drug_id))
    Usage.objects.create(
        username = user_instance,
        drug = drug_instance
        )
    print("Successfully created usage of {0} for {1}".format(drug_instance, user_instance))

def main(**kwargs):
    """
    Main control function for the module.
    """
    import_type = kwargs.pop('import_type', None)
    import_file = kwargs.pop('import_file', None)
    username = kwargs.pop('username', None)
    drug_id = kwargs.pop('drug_id', None)

    if import_type == "drug":
        import_drugs(import_file)
    if import_type == "user":
        import_user(username)
    if import_type =="usage":
        import_usage(username, drug_id)

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
    parser.add_argument("--username",
        dest = 'username',
        help="Username to import")
    parser.add_argument("--drug-id",
        dest = 'drug_id',
        help="Database ID of the drug to assocaite with a usage")
    args = parser.parse_args()
    main(**vars(args))

if __name__ == '__main__':
    parse()
