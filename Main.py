import urllib.request
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

mwurl = "https://www.nasdaq.com/symbol/"

trlist = []
def init():
    stocklist = ['AAPL','WMT','WFC','BAC']
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
    for table in soup.findAll("table")[5:6]:
        r = 0
        for tr in table.findAll("tr")[2:]:
            print('row: ' + str(r))
            r += 1
            c = 0
            tdlist = []
            tdlist.append(ticker)
            for td in  tr.findAll("td"):
                print('col: ' + str(c))
                dirtyvar = str(td.get_text().strip())
                c += 1
                print(dirtyvar)
                tdlist.append(dirtyvar)
            trlist.append(tdlist)
def lookmeup():
    stockselect = input("Input Ticker: ")
    searchlist = []
    for srow in trlist[:]:
        if srow[0] == stockselect:
            stemprow = []
            for sdata in srow[:]:
                stemprow.append(sdata)
            searchlist.append(stemprow)
    dtlookup(searchlist)
def dtlookup(searchlist):
    print("Type 1 to select stock")
    dateselect = input("Input Date: ")
    if dateselect == '1':
        lookmeup()
    else:
        findcount = 0
        for dtrow in searchlist[:]:
            if dtrow[1] == dateselect:
                print("Stock: " + dtrow[0])
                print("Date: " + dtrow[1])
                print("Open: " + dtrow[2])
                print("Close: " + dtrow[5])
                print("Volume: " + dtrow[6])
                findcount += 1
        if findcount < 1:
            print("not found")
        dtlookup(searchlist)
init()
lookmeup()

