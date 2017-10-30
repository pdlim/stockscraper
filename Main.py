import urllib.request
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

mwurl = "https://www.nasdaq.com/symbol/"

def init():
    #stocklist = ['AAPL','WMT','WFC','BAC']
    stocklist = ['AAPL']
    #params = ['Current Price']
    tickerjump(stocklist)

def tickerjump(stocklist):
  for t in range(0,len(stocklist)):
    ticker = stocklist[t]
    print(ticker)
    print(mwurl+ticker.lower())
    scrapesite(ticker)
def scrapesite(ticker):
    response = urllib.request.urlopen(mwurl+ticker+'/historical')
    soup = BeautifulSoup(response,"lxml")
    trlist = []
    for table in soup.findAll("table")[5:6]:
        r = 0

        for tr in table.findAll("tr")[2:]:
            print('row: ' + str(r))
            r += 1
            c = 0
            tdlist = []
            for td in  tr.findAll("td"):
                print('col: ' + str(c))
                dirtyvar = str(td.get_text().strip())
                c += 1
                print(dirtyvar)
                tdlist.append(dirtyvar)
            trlist.append(tdlist)
    getstockdate = input("enter row number")
    print(trlist[int(getstockdate)][1])

init()
