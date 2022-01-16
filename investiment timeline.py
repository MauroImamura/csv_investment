import csv
import os
from datetime import datetime
import urllib.request
import numpy

def main():
      # execute script
      
      print("Session initialized.")
      print("...")

      if 'statement.csv' not in os.listdir():
            print("Creating file...")
            create_statement()

      print("Getting calendar information.")
      print("...")
      global holidays_list
      holidays_list = get_holidays()

      print("Recording file ready.")
      print("...")
      print("Use invest()/calculate() functions to record or evaluate investments.")
      print("Use show() to see your statement.")
      
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
      date = input('Investment date (dd/mm/yyyy): ')
      name = input('Investment name or description: ')
      amount = float(input('Amount ($): ').replace(',','.'))
      rate = float(input('Interest rate (%): ').replace(',','.'))

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
      date = input('Reference date(dd/mm/yyyy): ')
      date_as_date = datetime.strptime(date,'%d/%m/%Y')

      # read csv statement file and calculate investment worth
      with open('statement.csv','r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                  initial_date = datetime.strptime(row[0],'%d/%m/%Y')
                  if date_as_date > initial_date:
                        t = numpy.busday_count(initial_date.strftime('%Y-%m-%d'),date_as_date.strftime('%Y-%m-%d'))
                        current_amount = float(row[2])*(1+(float(row[3])/100))**(t/252)
                        print('Resulting amount of ', row[1], ': ', format(current_amount,'.2f'))
                        result += current_amount

      print('Resulting total amount: R$', format(result, '.2f'))

def show():
      #displays current statement on screen

      with open('statement.csv','r') as f:
            reader = csv.reader(f)
            for row in reader:
                  print(row)

def get_holidays():
      #get the list of holidays and their dates on ANBIMA's library

      hol_hist = {}
      
      for year in range(2001,2078):
            link = 'https://www.anbima.com.br/feriados/fer_nacionais/{}.asp'.format(year)
            with urllib.request.urlopen(link) as f:
                  content = f.read()
                  dec = content.decode()
            hol_hist.update({year:dec})
      return hol_hist

main()
