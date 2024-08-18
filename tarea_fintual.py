## Inicialización de librerías para la clase
import os
import pandas as pd

    
    
class Portfolio:
    """
    Portfolio, by Caro
    
    Esta clase crea un objeto con atributos interesantes para un portafolio de acciones.
    * Primero es importante tener un portafolio en un csv llamado "portfolio.csv"
    * El archivo tiene series de tiempo para los precios de las acciones
    
    Atributos:
    - stocks: crea un diccionario con las acciones del portafolio
    
    Métodos:
    - Profit: entrega la ganancia obtenida entre dos fechas del portafolio. Requiere una fecha inicial y una fecha final.
    - Annualized_Return: entrega el retorno anualizado entre dos fechas. Requiere una fecha inicial y una fecha final.
    
    """
    

    
    ## Carga del archivo del portafolio
   
    
    ## Creación del portafolio
    def __init__(self):
        
        file="portfolio.csv"
    
        try:
            df = pd.read_csv(file, sep=';', index_col=0, parse_dates=True, dayfirst=True)
            price_columns = [col for col in df.columns if col != 'Date']
            for col in price_columns:
                df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')

        except:
            print("¡Ha ocurrido un error! Archivo no encontrado")
            return False

        self.dataframe = df
        
        self.stocks = {}
        
        for i, column in enumerate(df.columns, start=1):  
            self.stocks[f'stock{i}'] = df[column]
            
            
  
    def Profit(self, start_date, end_date):
        
        try:
            start_date = pd.to_datetime(start_date,format='%Y-%m-%d', errors='raise')
            end_date = pd.to_datetime(end_date,format='%Y-%m-%d', errors='raise')
        except:
            print("¡Error! Ingresa un formato de fechas correcto (YYYY-MM-DD)")
            return False

        start_prices = []
        end_prices = []

        for nombre, precios in self.stocks.items():
            start_price = precios.loc[start_date] if start_date in precios.index else None
            end_price = precios.loc[end_date] if end_date in precios.index else None

            if start_price is not None and end_price is not None:
                start_prices.append(start_price)
                end_prices.append(end_price)
            else:
                print(f"¡Error! Faltan datos para {nombre} en las fechas proporcionadas.")
                return False

        # Calcular el valor total del portafolio al inicio y al final
        portfolio_value_start = sum(start_prices)
        portfolio_value_end = sum(end_prices)

        # Calcular el profit
        profit = portfolio_value_end - portfolio_value_start

        return f"La ganancia entre {start_date.date()} y {end_date.date()} fue de USD {profit:.2f}"
    
    def Annualized_Return(self, start_date, end_date):
        try:
            start_date = pd.to_datetime(start_date,format='%Y-%m-%d', errors='raise')
            end_date = pd.to_datetime(end_date,format='%Y-%m-%d', errors='raise')
        except:
            print("¡Error! Ingresa un formato de fechas correcto (YYYY-MM-DD)")
            return False
            
        start_prices = []
        end_prices = []

        for nombre, precios in self.stocks.items():
            start_price = precios.loc[start_date] if start_date in precios.index else None
            end_price = precios.loc[end_date] if end_date in precios.index else None

            if start_price is not None and end_price is not None:
                start_prices.append(start_price)
                end_prices.append(end_price)
            else:
                print(f"¡Error! Faltan datos para {nombre} en las fechas proporcionadas.")
                return False

        # Calcular el valor total del portafolio al inicio y al final
        portfolio_value_start = sum(start_prices)
        portfolio_value_end = sum(end_prices)

        # Calcular el profit
        profit = portfolio_value_end - portfolio_value_start
        
        d = end_date - start_date
        #return d.days
                
        retorno = ((1+(profit/portfolio_value_start))**(360/d.days))-1

        return f"El retorno anualizado entre {start_date.date()} y {end_date.date()} fue de {retorno * 100:.2f}%"