import csv

def add_header(inp_vector, file_name):
      # write the header line into a csv file called file_name.
      # if the file doesn't exists, a new one is created.

      content = []

      f = open(file_name)

      reader = csv.reader(f)
      for row in reader:
            content.append(row)

      f.close()
      
      f = open(file_name, 'w',encoding = 'UTF8', newline = '')
      
      writer = csv.writer(f)
      writer.writerow(inp_vector)
      for i, row in enumerate(content):
            if i > 0:
                  writer.writerow(row)

      f.close()

def add_line(inp_vector, file_name):
      # write a new line into a csv file called file_name.
      # if the file doesn't exists, a new one is created.
      
      f = open(file_name, 'a',encoding = 'UTF8', newline = '')

      writer = csv.writer(f)

      writer.writerow(inp_vector)

      f.close()
