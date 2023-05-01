#!/usr/bin/env python

#Line to run program: python question_1.py <year1> <month1> <day1> <year2> <month2> <day2> <file to read data from> > <file to write data into>
# python question_1.py 2021 9 13 2021 11 28 cases_by_age_vac_status_2021-12-02_22-52.csv > plot1.csv

import sys
import csv
from datetime import date

def main(argv):

  #ensure right num of arguments
  if len(argv) != 8:
    print("Usage: python question_1.py <year1> <month1> <day1> <year2> <month2> <day2> <file to read data from> > <file to write data into>")
    sys.exit(1)
  
  year1 = int(argv[1])
  month1 = int(argv[2])
  day1 = int(argv[3])
  year2 = int(argv[4])
  month2 = int(argv[5])
  day2 = int(argv[6])
  input_file = argv[7]

  try:
      file_opened = open(input_file, encoding="utf-8-sig")
    
  except IOError as err:
      print("Unable to open file '{}' : {}".format(
          input_file, err),
            file=sys.stderr)
      sys.exit(1)

  file_reader = csv.reader(file_opened)

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
  if starting_date < date.fromisoformat("2021-09-13") or ending_date > date.fromisoformat("2021-11-28"):
    print("Data is only available between 2021-09-13 to 2021-11-28.")
    sys.exit(1)


  print("date,cases_unvac_rate_per100K,age_group")

  next(file_reader, None)
  

  #each row in file
  for row_data_fields in file_reader:
    #date
    row_date = date.fromisoformat(row_data_fields[0])
    #age group
    row_agegroup = row_data_fields[1]
    #unvacc cases rate
    row_cases = row_data_fields[2]
    

    #find the given rage in file
    if row_date >= starting_date and row_date <= ending_date:
      #print date, unvacc cases rate, and age group
      print(f"{row_date},{row_cases},{row_agegroup}")

main(sys.argv)