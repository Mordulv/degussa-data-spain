from selenium import webdriver
from pynput.mouse import Controller, Button
from time import sleep

raton = Controller()
# Para que funcione bien, actualizar el path en funcion de cada persona y tener descargado en ese mismo
# path el driver de chrome
path = 'C://Users//Guillermo//Desktop//Chrome//chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get('https://www.degussa-mp.es/wp-content/uploads/fen/preise/listadeprecios.pdf')
driver.maximize_window()

# Nota importante: las tuplas de valores de raton.position varian en funcion de la pantalla, resolucion
# y monitor de cada persona. Para solventar esto, se recomienda hacer puebas y determinar la posicion
# adecuada para cada uno
#
#Para deteminar la posicion del raton, posicionar el raton donde se desee y ejecutar en Python el
#comando: pynput.mouse.Controller().position

sleep(2)
raton.position = (1574, 140)
sleep(1)
raton.click(Button.left,1)
sleep(1)
raton.position = (676, 495)
raton.click(Button.left,1)

sleep(3)
driver.close()

import PyPDF2
from os import chdir, remove

# Para que funcione bien, actualizar el path en funcion de cada persona
path = 'C://Users//Guillermo//Downloads'
chdir(path)

pdf_objeto = open('listadeprecios.pdf','rb')
pdf = PyPDF2.PdfFileReader(pdf_objeto)

txt = open('datos.txt','a')

for i in range(3):
    hoja1 = pdf.getPage(i)
    texto = hoja1.extractText()
    txt.write(texto)

txt.close()
pdf_objeto.close()
remove('listadeprecios.pdf')

