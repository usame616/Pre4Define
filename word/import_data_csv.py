#!/usr/bin/env python

"""
    Script to import book data from .csv file to Model Database DJango
    To execute this script run:
                                1) manage.py shell
                                2) exec(open('import_data_csv.py').read())
"""
import csv
from .models import WordsDefining

CSV_PATH = 'C:/Users/Lenovo/Desktop/word.csv'

contSuccess = 0
# Remove all data from Table
WordsDefining.objects.all().delete()

with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    print('Loading...')
    for row in spamreader:
        WordsDefining.objects.create(word=row[0], category=row[1], pegi=row[2], commentCount=row[3], commentScore=row[4], appSizeMb=row[5], downloads=row[6], ranking=row[7])
        contSuccess += 1
    print(f'{str(contSuccess)} inserted successfully! ')
