"""
matplotlib

Version 3.7.2
Python plotting package
"""

"""import matplotlib.pyplot as plt

def generate_bar_chart():
  labels = ['a', 'b', 'c']
  values = [100, 200, 80]
  
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

if __name__ == '__main__':
  generate_bar_chart()"""

"""#ahora vamos a hacerlo dinamico recibiendo parametros
import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):  
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 80]
  generate_bar_chart(labels, values) # no entiendo porque no grafica si la primera si grafico"""


import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):  
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()
  
def generate_pie_chart(labels, values):  
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 80]
  generate_pie_chart(labels, values)

