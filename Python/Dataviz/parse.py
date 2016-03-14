import csv

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
  opened_file = open(raw_file)
  csv_data = csv.reader(opened_file, delimiter=delimiter)
  
  parsed_data = []
  fields = csv_data.next()
  for row in csv_data:
    parsed_data.append(dict(zip(fields, row)))
    
  opened_file.close()
  return parsed_data
  
  
def main():
  new_data = parse(MY_FILE, ",")
  print new_data
  
def __name__ = "__main__":
  main()
