from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Ali.Abdelhamid\PycharmProjects\FinScrape\drivers\chromedriver.exe")

my_url = ('https://finance.yahoo.com/quote/' + 'aapl' + '/balance-sheet') #get URL
driver.get(my_url)


driver.find_element_by_xpath().send_keys("automation")


#Clicking on Quarterly Button
time.sleep(2)
driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[1]/div[2]/button/div/span').click()

#Clicking on both drop down buttons
time.sleep(2)
driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button').click()
driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/button').click()

#getting (B/S) data from droop down menu
time.sleep(2)
current_assets = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/span').text
noncurrent_assets = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/span').text
current_liabilities = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/span').text
noncurrent_liabilities = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/span').text
equity = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[4]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/span').text

#print, populate excel sheet
print('Current Assets:' + current_assets)
print('Non-Current Assets:' + noncurrent_assets)
print('Current Liabilities:' + current_liabilities)
print('Non-Current Liabilities:' + noncurrent_liabilities)
print('Equity:' + equity)

