'''
This script takes a list of stocks from a text file and outputs the sector and industry for all stocks on the list.
The script url has been improved to cover a wider range of stocks. You will need to have the stocks.txt file in your
directory in order to run this script
# 05/21/2020
'''

import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

filename = 'stocks.txt'
stocks = open(filename).read().splitlines() # reads the text file and splits entries by lines

n = len(stocks) # number of stocks in text file

sector_text = ["" for x in range(n)] # string array to store the sector
industry_text = ["" for y in range(n)] # string array to store the industry


for i in range(0, n):

    company_name = stocks
    my_url = ('https://finance.yahoo.com/quote/' + company_name[i] + '/profile') # generate a url that accesses profile of every company

    # Opening connection and grabbing the page
    uClient = ureq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

    # grabs containers with sector and industry
    containers = page_soup.findAll("span", {"class": "Fw(600)"})
    container_sector = containers[0] # location of sector
    container_industry = containers[1]  # location of industry

    sector_text[i] = container_sector.get_text(strip=True)
    industry_text[i] = container_industry.get_text(strip=True)

    # print company name and both its sector and industry
    print(company_name[i] + ", sector: " + sector_text[i] + ", industry: " + industry_text[i])