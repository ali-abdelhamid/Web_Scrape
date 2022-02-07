'''
This script takes a list of stocks from a text file and outputs the Earnings Per Share for all stocks on the list.
The script url has been improved to cover a wider range of stocks. You will need to have the stocks.txt file in your
directory in order to run this script
# 05/20/2020
'''

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq


filename = 'stocks.txt'
stocks = open(filename).read().splitlines() # reads the text file and splits entries by lines

n = len(stocks) # number of stocks in text file
EPS = np.zeros(n) # EPS array to save values of EPS for all shares in an array
EPS_text = ["" for x in range(n)]

for i in range(0, n):
    company_name = stocks
    my_url = ('https://finance.yahoo.com/quote/' + company_name[i]) # generate a url for every company

    # Opening connection and grabbing the page
    uClient = ureq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

    # grabs EPS
    containers = page_soup.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"}) # location of EPS in html code
    container = containers[10]

    EPS_text[i] = container.get_text(strip=True) # string value of EPS

    # print company name and its EPS as a string
    print('Earning Per Share for Stock ' + company_name[i] + ' is: ' + (EPS_text[i]))



