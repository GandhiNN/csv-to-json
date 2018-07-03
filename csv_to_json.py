#!/usr/local/bin/python3

################################
# script_name : csv_to_json.py
# author      : __gandhi__
################################

import sys
import getopt
import csv
import json

# Read csv file
def read_csv(csv_file, json_file, format):
    csv_rows = []
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] \
                         for i in range(len(title))}])
        write_json(csv_rows, json_file, format)

# Convert csv data into json and write into
def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4,
                separators=(',',': '), ensure_ascii=False))
        else:
            f.write(json.dumps(data))

# Get command line arguments
def main(argv):
    input_file = ''
    output_file = ''
    format = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:f:", ["ifile=",
                                   "ofile=", "format="])
    except getopt.GetoptError:
        print('apn_to_json.py -i <path_to_inputfile> -o <path_to_outputfile> -f <dump/pretty>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('apn_to_json.py -i <path_to_inputfile> -o <path_to_outputfile> -f <dump/pretty>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-f", "--format"):
            format = arg
    read_csv(input_file, output_file, format)

if __name__ == "__main__":
    main(sys.argv[1:])
