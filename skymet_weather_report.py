"""
Program to display Pune's current temperature and weather condition from skymet website
"""

import requests
import bs4

res = requests.get(r'https://www.skymetweather.com/forecast/weather/india/maharashtra/pune/pune')
res.raise_for_status()

bs = bs4.BeautifulSoup(res.text, "html.parser")

temp = bs.find('span', attrs={'class': 'c'})
weath_cond = bs.find('div', attrs={'class': 'crCondition'})

print("==== Pune Current Weather ====")
print("{} : {}".format('Temperature', temp.text))
print("{} : {}".format('Weather Condition', weath_cond.text))



