#!/usr/bin/env python

#Line to run program: python question_4.py <year1> <month1> <day1> <year2> <month2> <day2> <agegroup> <file to read data from> > <file to write data into>
# python question_4.py 2020 12 16 2022 3 21 "12-17yrs" vaccines_by_age_2022-03-21_22-18.csv > plot4.csv

import sys
import csv
from datetime import date

def main(argv):

  #ensure right num of arguments
  if len(argv) != 9:
    print("Usage: python question_4.py <year1> <month1> <day1> <year2> <month2> <day2> <agegroup> <file to read data from> > <file to write data into>")
    sys.exit(1)
  
  year1 = int(argv[1])
  month1 = int(argv[2])
  day1 = int(argv[3])
  year2 = int(argv[4])
  month2 = int(argv[5])
  day2 = int(argv[6])
  agegroup = argv[7]
  input_file = argv[8]

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
  if starting_date < date.fromisoformat("2020-12-16") or ending_date > date.fromisoformat("2022-03-28"):
    print("Data is only available between 2020-07-30 to 2022-03-21.")
    sys.exit(1)

  #check if valid age group
  if agegroup not in ["12-17yrs","18-29yrs","30-39yrs","40-49yrs","50-59yrs","60-69yrs","70-79yrs","80+","Adults_18plus","Ontario_12plus"
"Undisclosed_or_missing"]:
    print("Age group must be one of: '12-17yrs' '18-29yrs' '30-39yrs' '40-49yrs' '50-59yrs' '60-69yrs' '70-79yrs' '80+' 'Adults_18plus' 'Ontario_12plus' 'Undisclosed_or_missing'")
    sys.exit(1)


  print("Date,Percentage_fully_vaccinated")

  #each row in file
  for row_data_fields in file_reader:

    row_agegroup = row_data_fields[1]
    percentage = row_data_fields[8]
    #done so that the value can be read as an integer as perecentages in the file start with a period
    percentage = "0" + percentage
    
    if row_data_fields[0] != "Date":
      row_date = date.fromisoformat(row_data_fields[0])
      percentage = float(percentage) * 100

      if row_date >= starting_date and row_date <= ending_date:

        if agegroup == row_agegroup:
          print(f"{row_date},{percentage}")

main(sys.argv)