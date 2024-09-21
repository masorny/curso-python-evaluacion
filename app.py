url = "https://jaguarete.unida.edu.py/jaguarete"
matricula = input('Ingrese su matricula: ')
clave = input('Ingrese su clave: ')

print('Inicializando servicio espere ...')

# Llamamos al modulo.
from scraping import initialize
initialize(url, matricula, clave)