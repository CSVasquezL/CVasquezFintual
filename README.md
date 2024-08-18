Portfolio Management in Python
This repository contains a simple Python project that implements a Portfolio class. The class allows users to manage a portfolio of stocks, calculate the profit between two dates, and compute the annualized return over a given period.

Features
Portfolio Class: Manage a portfolio of stocks.
Profit Calculation: Calculate the total profit between a start and end date.
Annualized Return Calculation: Compute the annualized return based on the portfolio’s performance over a specified period.
Getting Started
Prerequisites
Python 3.x
Pandas library
You can install the necessary dependencies using:

bash
Copiar código
pip install pandas
Installation
Clone the repository to your local machine:

bash
Copiar código
git clone https://github.com/yourusername/portfolio-management.git
cd portfolio-management
Usage
Load your portfolio data: The portfolio data should be in a CSV file with the following structure:

Date: In DD-MM-YYYY format.
Stock Prices: Columns for each stock with prices as float values (using commas as decimal separators is supported).
Create a Portfolio: Use the Portfolio class to load your data and manage your stocks.

python
Copiar código
import pandas as pd
from portfolio import Portfolio

# Load your data
data = pd.read_csv('portfolio.csv')

# Create a Portfolio instance
portfolio = Portfolio(data)
Calculate Profit: Calculate the profit between a start and end date.
python
Copiar código
start_date = '01-01-2020'
end_date = '01-01-2024'
profit = portfolio.Profit(start_date, end_date)
print(f"Profit between {start_date} and {end_date}: {profit}")
Calculate Annualized Return: Compute the annualized return for a specified period.
python
Copiar código
annualized_return = portfolio.Retorno_Anual(start_date, end_date)
print(f"Annualized Return between {start_date} and {end_date}: {annualized_return}")
Example
Here’s a quick example of how you might use the Portfolio class in practice:

python
Copiar código
# Assuming you have a CSV file 'portfolio.csv' with stock data
portfolio = Portfolio('portfolio.csv')
profit = portfolio.Profit('01-01-2020', '01-01-2024')
annualized_return = portfolio.Retorno_Anual('01-01-2020', '01-01-2024')

print(f"Profit: {profit}")
print(f"Annualized Return: {annualized_return}")
Customization
The output messages for the Profit and Retorno_Anual methods can be customized to fit your specific formatting preferences. You can edit these methods in the Portfolio class to include custom messages or formats.

Contributing
Feel free to contribute to this project by submitting a pull request or opening an issue.

License
This project is licensed under the MIT License - see the LICENSE file for details.
