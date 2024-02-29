import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)

    data = []    
    
    #print(header)

# Estos van a ser nuestras claves:

# ['Rank', 'CCA3', 'Country/Territory', 'Capital', 'Continent', '2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate', 'World Population Percentage']

    for row in reader:
      # print('***' * 15)
      iterable = zip(header, row)
      #print(list(iterable)) # nos lo da en tuplas pero ocupamos convertirlo a dict con dict comprehentions
      country_dict = {key: value for key, value in iterable}
      #print(country_dict) # ahora si ya tenemosun dict con clave: valor pero necesitamos retornarlo a una lista con todos sus diccionarios porque no esta en ningun lado.

      data.append(country_dict)
    return data

    
    """for row in reader:
      print('***' * 5)
      print(row)"""

"""leer = read_csv('./app/data.csv') # pero debemos usar un if para ejecutarlo desde la terminal como un script
print(leer)"""

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  # print(data[0])


"""me marca este error: line 39, in <module>
    search = list(filter(lambda country: country['Country/Territory'] == 'Mexico', data))
NameError: name 'data' is not defined"""

#esto lo puso un alumno en un comentario
"""search = list(filter(lambda country: country['Country/Territory'] == 'Mexico', data))
print(search)"""

# [{'Rank': '10', 'CCA3': 'MEX', 'Country/Territory': 'Mexico', 'Capital': 'Mexico City', 'Continent': 'North America', '2022 Population': '127504125', '2020 Population': '125998302', '2015 Population': '120149897', '2010 Population': '112532401', '2000 Population': '97873442', '1990 Population': '81720428', '1980 Population': '67705186', '1970 Population': '50289306', 'Area (km²)': '1964375', 'Density (per km²)': '64.9082', 'Growth Rate': '1.0063', 'World Population Percentage': '1.6'}]