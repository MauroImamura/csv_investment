import csv
import os
import datetime

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

      #ask for investmet details
      inp_date = input('Investment date (dd/mm/yyyy): ')
      name = input('Investment name or description: ')
      amount = float(input('Amount ($): ').replace(',','.'))
      rate = float(input('Interest rate (%): ').replace(',','.'))

      #correct date format
      [dd,mm,yyyy] = [int(inp_date[0:2]),int(inp_date[3:5]),int(inp_date[6:10])]
      date = datetime.datetime(yyyy,mm,dd)

      #list of investiment information
      inp_vector = [date,name,amount,rate]

      #write on statement file
      f = open('statement.csv', 'a',encoding = 'UTF8', newline = '')
      writer = csv.writer(f)
      writer.writerow(inp_vector)
      f.close()

main()
