#!/usr/bin/env python

#Line to run program: python question_3.py <year1> <month1> <day1> <year2> <month2> <day2> <cases by status and phu file> <covid alert file> > <file to write data into>

# python question_3.py 2021 3 3 2022 2 2 cases_by_status_and_phu_2022-03-21_22-16.csv covid_alert_downloads_canada_2022-03-21_22-17.csv > plot3.csv

import sys
import csv
from datetime import date

def main(argv):

  #ensure right num of arguments
  if len(argv) != 9:
    print("Usage: python question_3.py <year1> <month1> <day1> <year2> <month2> <day2> <cases by status and phu file> <covid alert file> > <file to write data into>")
    sys.exit(1)
    
  year1 = int(argv[1])
  month1 = int(argv[2])
  day1 = int(argv[3])
  year2 = int(argv[4])
  month2 = int(argv[5])
  day2 = int(argv[6])
  input_file_1 = argv[7]
  input_file_2 = argv[8]

  #open reader for first file
  try:
      file_opened = open(input_file_1, encoding="utf-8-sig")
    
  except IOError as err:
      print("Unable to open file '{}' : {}".format(
          input_file_1, err),
            file=sys.stderr)
      sys.exit(1)

  file_reader_1 = csv.reader(file_opened)

  #open reader for second file
  try:
      file_opened = open(input_file_2, encoding="utf-8-sig")
    
  except IOError as err:
      print("Unable to open file '{}' : {}".format(
          input_file_2, err),
            file=sys.stderr)
      sys.exit(1)

  file_reader_2 = csv.reader(file_opened)

  #function for getting the user inputted day into iso format
  def concat0(x):
    if x < 10:
      return "0" + str(x)
    return x
  
  month1 = concat0(month1)
  day1 = concat0(day1)
  month2 = concat0(month2)
  day2 = concat0(day2)

  #converts dates to iso variable
  starting_date = date.fromisoformat(f"{year1}-{month1}-{day1}")
  ending_date = date.fromisoformat(f"{year2}-{month2}-{day2}")

  #check if valid date range
  if starting_date < date.fromisoformat("2020-12-31") or ending_date > date.fromisoformat("2022-03-21"):
    print("Data is only available between 2020-12-16 to 2022-03-21.")
    sys.exit(1)
    
  #variable to track what element the list is on
  list_counter = 0

  print("date,number_of_cases/downloads,which_data")
  
  #skip first line
  next(file_reader_1, None)
  
  for row_data_fields in file_reader_1:
    
    row_date = date.fromisoformat(row_data_fields[0])
    #check if the date of the line is in the date range
    if row_date >= starting_date and row_date <= ending_date:
      #add that number of cases into the list
      print(f"{row_date},{row_data_fields[3]},case")
    
  #skip first line
  next(file_reader_2, None)
  
  for row_data_fields in file_reader_2:
    row_date = date.fromisoformat(row_data_fields[0])
    #check if the date of the line is in the date range
    if row_date >= starting_date and row_date <= ending_date:
      download_count = row_data_fields[6]
      print(f"{row_date},{download_count},download")
      #move next in the list
      list_counter = list_counter + 1
  
main(sys.argv)