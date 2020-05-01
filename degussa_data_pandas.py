from pandas import read_html, concat
from time import gmtime, strftime

class Degussa():

    def __init__(self):

        self.path = "https://www.degussa-mp.es/precios"
    
    def get_data(self):

        data = concat(read_html(self.path))

        metal_type = lambda x: x[0]
        change_price = lambda price: float(price.replace(' €','').replace('.','').replace(',','.'))

        data["Type"] = list(map(metal_type, list(data["Producto"])))
        data["Recompra"] = list(map(change_price, list(data["Precio de recompra"])))
        data["Compra"] = list(map(change_price, list(data["Precio de venta"])))
        data["Diferencia"] = data["Compra"] - data["Recompra"]

        data = data.reset_index(drop=True)
        data = data.replace({'Type': {"1": "Gold", "2":"Silver", "3":"Platinum", "4":"Palladium", "5":"Gold"}})

        data = data[["Producto", "Type", "Tienda", "Compra", "Recompra", "Diferencia"]]
        data.columns = ["Product", "Type", "Name", "Buy", "Sell", "Difference"]

        return data.round(4)
    
    def save_data(self, time_name = True, name='data.txt', decimal=','):

        if time_name:
            name = strftime("%Y-%m-%d %H-%M-%S", gmtime()) + ".txt"

        data = self.get_data()
        data.to_csv(name, sep=";", decimal=decimal)
