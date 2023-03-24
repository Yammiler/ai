import csv

def write_data(data):
  data = [[s.strip().replace('\n','') for s in sub_list] for sub_list in data]
  with open('data.csv','w', encoding="utf-8-sig",newline='') as file:
   list_data = csv.writer(file,quoting=csv.QUOTE_MINIMAL )
   for x in data:
      row = [cell.replace('"','') for cell in x]
      list_data.writerow(row)
