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

t = ''
for i in range(3):
    hoja1 = pdf.getPage(i)
    texto = hoja1.extractText()
    txt.write(texto)
    t = t +texto

txt.close()
pdf_objeto.close()
remove('listadeprecios.pdf')

# Obtiene los datos de un producto determinado

def buscador_producto(texto,codigo):
    l_cod = len(codigo)
    l_texto = len(texto)
    inicio, final, puntero = 0, l_cod, None
    encontrado = False
    while final != (l_texto - 1):
        palabra_aux = texto[inicio:final]
        if codigo == palabra_aux:
            print('ENCONTRADO')
            cont_c = 0
            txt = ''
            for i in texto[inicio:]:
                if cont_c == 2:
                    return txt
                else:
                    txt = txt + i
                    if txt[len(txt)-1] == '•':
                        cont_c += 1
                    
        else:
            inicio += 1
            final += 1
    print('SIN COINCIDENCIA')

def depurar(codigo,nombre,texto):
    datos = {}
    x = lambda x: float(x.replace(' ','').replace(',','.'))
    aux = texto.split(nombre)
    aux2 = aux[1].split('•')[0:2]
    datos['Codigo'] = codigo
    datos['Nombre'] = nombre
    dat = list(map(x,aux2))
    datos['Compra'] = dat[1]
    datos['Venta'] = dat[0]
    return datos

# Ejemplo
texto = buscador_producto(t,'124162/01')
print(texto)
y = depurar('124162/01','8 x 1g de oro Maplegram de Canadá',texto)
print(y)
