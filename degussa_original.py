from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pandas import DataFrame
from time import sleep
import bs4

class Degussa():
    
    def __init__(self):
        
        url_path = 'https://www.degussa-mp.es/precios'
        
        accept_cookies  = '/html/body/div[1]/div/a'

        self.tables = ['tab2',
                       'tab3',
                       'tab4',
                       'tab5']

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        
        self.driver = webdriver.Chrome('Config_data\\chromedriver.exe', options=chrome_options)
        self.driver.get(url_path)
        
        sleep(2)

        try:
            self.driver.find_element_by_xpath(accept_cookies).click()
        except Exception:
            print('Error when trying to accept cookies')
            pass
    
    def get_data(self):

        '''

        Descripción:
        ------------

        Función que obtiene los datos referentes a la tienda degussa de España, siendo los datos seleccionados:
        fecha de actualización de precios, códigos de productos, nombre de los productos, precio de venta
        y precio de compra.

        Precondición:
        -------------

        - Tener instaladas las librerías correspondientes.
        - Tener el webdriver de crome en una carpeta llamada Config_data siendo el nombre del webdriver
        chromedriver.

        Retorna:
        --------

        La función retorna una tupla con la fecha de los precios actualizados y un DataFrame con los datos

        Ejemplo de llamada:
        -------------------

        Con desempaquetado de tupla
        >>> fecha, datos = Degussa().get_data()

        ó

        Sin desempaquetado de tupla
        >>> datos = Degussa().get_data()

        '''
        
        prices, code, name, sale = [], [], [], []

        change_price = lambda price: float(price.replace(' €','').replace('.','').replace(',','.'))

        html = bs4.BeautifulSoup(self.driver.page_source, 'html.parser')

        date = html.findAll('div', {'id':'text-block-9'})[0].findAll('div')[0].text

        for tab in self.tables:

            tab = html.findAll('div', {'id':tab})
            table = tab[0].findAll('table')[0].findAll('tbody')[0]

            lines = table.findAll('tr')

            for i in lines:

                aux = i.findAll('td')

                code.append(aux[0].text)
                name.append(aux[2].text)
                sale.append(aux[3].text)
                prices.append(aux[4].text)

        prices = list(map(change_price, prices))
        sale = list(map(change_price, sale))

        self.driver.quit()

        data = DataFrame([code, name, prices, sale]).T
        data.columns = ['Code', 'Name', 'selling price', 'purchase price']

        return date, data
