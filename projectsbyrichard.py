#!/usr/bin/python3
from flask import Flask, redirect, url_for, render_template, request
import bs4
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
price = -1
ticker= ""
pricelist = []
returntickerlist = []
returnpricelist = []

@app.route("/")
def home():
    #return render_template("index.html") #, content = ticker, price = price)
    return render_template("index.html")

@app.route("/livetickerentry", methods=['POST', 'GET'])
def livetickerentry():
    global price
    global ticker
    global tickers
    global pricelist
    global tickerlist

    if request.method == "POST":
        ticker = str(request.form["tickerlist"])

        while True:
            return redirect(url_for("liveticker", tickers = ticker))
        #return render_template("livetickerentry.html", prices = price)
    else:
        #return "you are using get"
        return render_template("livetickerentry.html")

@app.route("/liveticker<tickers>", methods=["POST", "GET"])
def liveticker(tickers):
    tickerlist = tickers.split(" ")
    tickerlist = [str(x.upper()) for x in tickerlist]

    pricelist = []
    for elem in tickerlist:
        r = requests.get('https://finance.yahoo.com/quote/' + str(elem) + '?p=' + str(elem))
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        pricelist.append(str(price))
        price = -1
    while True:
        returnpricelist = list(pricelist)
        returntickerlist = list(tickerlist)
        prices = []
        tickers = []
        numtickers = len(tickerlist)
        print(numtickers)
        return render_template("liveticker.html", prices=returnpricelist, tickers=returntickerlist, numtickers = numtickers)


if __name__ == "__main__":
    app.run(debug=True)



