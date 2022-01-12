import csv
import os
from datetime import datetime

def main():
      # execute script
      
      print("Session initialized.")
      print("...")

      if 'statement.csv' not in os.listdir():
            print("Creating file...")
            create_statement()

      print("Recording file ready.")
      print("...")
      print("Use the invest function for new recordings.")
      
def create_statement():
      # generates a new statement file for investment recording.

      header = ['date','name','amount ($)','interest rate (%)']
      
      f = open('statement.csv', 'w',encoding = 'UTF8', newline = '')   
      writer = csv.writer(f)
      writer.writerow(header)
      f.close()

def invest():
      # write a new line into a csv file called statement.

      # ask for investmet details
      inp_date = input('Investment date (dd/mm/yyyy): ')
      name = input('Investment name or description: ')
      amount = float(input('Amount ($): ').replace(',','.'))
      rate = float(input('Interest rate (%): ').replace(',','.'))

      # correct date format
      date = convert_date(inp_date)

      # list of investiment information
      inp_vector = [date,name,amount,rate]

      # write on statement file
      f = open('statement.csv', 'a',encoding = 'UTF8', newline = '')
      writer = csv.writer(f)
      writer.writerow(inp_vector)
      f.close()

      print('Recording succeeded.')

def calculate():
      # calculate the total portfolio worth on the specified date

      result = 0.0
      
      # set ref date type and format
      inp_date = input('Reference date(dd/mm/yyyy): ')
      date = convert_date(inp_date)

      # read csv statement file and calculate investment worth
      with open('statement.csv','r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                  print(row[0])

def convert_date(str_date):
      # set date type and format
      [dd,mm,yyyy] = [int(str_date[0:2]),int(str_date[3:5]),int(str_date[6:10])]
      date = datetime(yyyy,mm,dd)
      return date

main()
