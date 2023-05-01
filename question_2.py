#!/usr/bin/env python

#Line to run program: python question_2.py 2021 9 13 2021 12 20 covid_summary_data_ontario.csv schoolcovidsummary2021_2022.csv > plot2.csv

import sys
import csv
from datetime import date

def main(argv):

  #ensure right num of arguments
  if len(argv) != 9:
    print("Usage: python question_2.py <year1> <month1> <day1> <year2> <month2> <day2> covid_summary_data_ontario.csv schoolcovidsummary2021_2022.csv > plot2.csv")
    sys.exit(1)
    
  year1 = int(argv[1])
  month1 = int(argv[2])
  day1 = int(argv[3])
  year2 = int(argv[4])
  month2 = int(argv[5])
  day2 = int(argv[6])
  positive_cases_file = argv[7]
  school_cases_file = argv[8]

  try:
      file1_opened = open(positive_cases_file, encoding="utf-8-sig")
  except IOError as err:
    print("Unable to open file '{}' : {}".format( positive_cases_file, err),file=sys.stderr)
    sys.exit(1)

  try:
    file2_opened = open(school_cases_file, encoding="utf-8-sig")
  except IOError as err:
    print("Unable to open file '{}' : {}".format(school_cases_file, err),file=sys.stderr)
    sys.exit(1)

  file1_reader = csv.reader(file1_opened)
  file2_reader = csv.reader(file2_opened)

  def concat0(x):
    if x < 10:
      return "0" + str(x)
    return x
  
  month1 = concat0(month1)
  day1 = concat0(day1)
  month2 = concat0(month2)
  day2 = concat0(day2)
  
  starting_date = date.fromisoformat(f"{year1}-{month1}-{day1}")
  ending_date = date.fromisoformat(f"{year2}-{month2}-{day2}")

  #check if valid date range 
  if starting_date < date.fromisoformat("2021-08-25") or ending_date > date.fromisoformat("2021-12-22"):
    print("Data is only available between 2021-08-25 to 2021-12-22.")
    sys.exit(1)

  print("Date,Number of Cases,Type of Data")

  #skip header
  next(file1_reader, None)
  next(file2_reader, None)
  
  #each row in file

  for row_data_fields in file1_reader:
    row_date = date.fromisoformat(row_data_fields[0])
    
    #check if the date of the line is in the date range
    if row_date >= starting_date and row_date <= ending_date:
      positive_cases = row_data_fields[1]
      print(f"{row_date},{positive_cases},Total Ontario Cases")

  #skip first line
  next(file2_reader, None)
  
  for row_data_fields in file2_reader:
    
    row_date = date.fromisoformat(row_data_fields[0])
    #check if the date of the line is in the date range
    if row_date >= starting_date and row_date <= ending_date:
      school_cases = row_data_fields[5]
      print(f"{row_date},{school_cases},Total School Cases")


main(sys.argv)