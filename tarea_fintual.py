## Inicialización de librerías para la clase
import pandas as pd

    
    
class Portfolio:
    """
    Portfolio, by Caro
    
    Esta clase crea un objeto con atributos interesantes para un portafolio de acciones.
    * Primero es importante tener un portafolio en un csv llamado "portfolio.csv".
    * El archivo tiene series de tiempo para los precios de las acciones.
    
    Atributos:
    - stocks: crea un diccionario con las series de tiempo de acciones del portafolio
    - dataframe: crea un dataframe para el portafolio.
    
    Métodos:
    - Profit: entrega la ganancia obtenida entre dos fechas del portafolio. Requiere una fecha inicial y una fecha final.
    - Annualized_Return: entrega el retorno anualizado entre dos fechas. Requiere una fecha inicial y una fecha final.
    
    """   
    
    ## Paso 1: Creación del portafolio como dataframe
    def __init__(self):
        
        file="portfolio.csv"
        ## Carga el archivo, convierte los valores a un formato correcto
        try:
            df = pd.read_csv(file, sep=';', index_col=0, parse_dates=True, dayfirst=True)
            price_columns = [col for col in df.columns if col != 'Date']
            for col in price_columns:
                df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')

        except:
            print("¡Ha ocurrido un error! Archivo no encontrado")
            return False
        ## Guarda los datos como dataframe
        self.dataframe = df
        ## Crea un diccionario para guardar las series de tiempo
        self.stocks = {}
        ## Agrega las series de precios al diccionario
        for i, column in enumerate(df.columns, start=1):  
            self.stocks[f'stock{i}'] = df[column]
            
            
    ## Paso 2: Método Profit. Obtiene la ganancia entre dos fechas.
    def Profit(self, start_date, end_date):
        ## Valida el formato de las fechas introducidas:
        try:
            start_date = pd.to_datetime(start_date,format='%Y-%m-%d', errors='raise')
            end_date = pd.to_datetime(end_date,format='%Y-%m-%d', errors='raise')
        except:
            print("¡Error! Ingresa un formato de fechas correcto (YYYY-MM-DD)")
            return False

        if start_date > end_date:
            print("¡Error! La fecha inicial no puede ser posterior a la fecha final")
            return False
        ## Se guardan los precios para realizar la operación
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

        ## Calcula el valor total del portafolio en la fecha inicial y final
        portfolio_value_start = sum(start_prices)
        portfolio_value_end = sum(end_prices)

        ## Calcula la ganancia
        profit = portfolio_value_end - portfolio_value_start

        print(f"La ganancia entre {start_date.date()} y {end_date.date()} fue de USD {profit:.2f}")

        return profit
    
    ## Paso 3: Método del retorno anualizado. Obtiene el retorno anualizado del portafolio entre dos fechas.
    def Annualized_Return(self, start_date, end_date):
        
        try:
            start_date = pd.to_datetime(start_date,format='%Y-%m-%d', errors='raise')
            end_date = pd.to_datetime(end_date,format='%Y-%m-%d', errors='raise')
        except:
            print("¡Error! Ingresa un formato de fechas correcto (YYYY-MM-DD)")
            return False

        if start_date > end_date:
            print("¡Error! La fecha inicial no puede ser posterior a la fecha final")
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

        ## Calcula el valor total del portafolio en la fecha inicial y final
        portfolio_value_start = sum(start_prices)
        portfolio_value_end = sum(end_prices)

        ## Calcula la ganancia
        profit = portfolio_value_end - portfolio_value_start
        
        ## Obtiene la cantidad de días entre ambas fechas para anualizar
        d = end_date - start_date
        
        ## Retorno anualizado
        retorno = ((1+(profit/portfolio_value_start))**(360/d.days))-1

        print(f"El retorno anualizado entre {start_date.date()} y {end_date.date()} fue de {retorno * 100:.2f}%")

        return retorno
    
## Ejemplos de prueba

if __name__ == "__main__":

    port = Portfolio()
    #port.dataframe
    #port.stocks
    #print(port.stocks.items())

    # Ejemplo con fechas válidas
    profit = port.Profit("2020-10-26","2023-10-26")

    # Ejemplo con fechas inválidas
    profit = port.Profit("2020-10-26","2024-10-26") ## Aquí no existen datos para la fecha final
    retorno = port.Annualized_Return("26-10-2020","2023-10-26") ## Aquí está mal escrito el formato de la primera fecha
    profit = port.Profit("2020-10-26","2019-10-26") ## Aquí la fecha inicial es posterior a la final
    profit = port.Profit("2020-10-","2020-10-26") ## Aquí está mal ingresada la fecha inicial