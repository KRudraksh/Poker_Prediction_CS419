# This file is used to generate .csv file from a given data file for testing and trainign

# Usage: python generate_csv.py [filename]
# example: python generate_csv.py train_data.data

import csv
import os, argparse

parser = argparse.ArgumentParser(description='Generates CSV files for a given text file delimited by commas')
parser.add_argument('filename', metavar = 'filename', type = str, nargs = '?', help = 'Filename of comma seperated text file')

args = parser.parse_args()
csv_file = os.path.splitext(args.filename)[0] + ".csv"

in_txt = csv.reader(open(args.filename, "r"), delimiter = ',')
out_csv = csv.writer(open(csv_file, 'w'))
out_csv.writerows(in_txt)