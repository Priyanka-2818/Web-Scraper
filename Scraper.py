from flask import Flask,jsonify
import requests
from bs4 import BeautifulSoup
import sqlite3

app=Flask(__name__)

@app.route('/scrape',methods=['GET'])
def scrape_data():
    url="http://quotes.toscrape.com"
    try:    
        response=requests.get(url,timeout=10)
        response.raise_for_status()

        #if response.status_code==200:
        soup=BeautifulSoup(response.text,"html.parser")
        titles=soup.find_all("h2")
        data=[title.got_text(strip=True) for title in titles if title.get_text(strio=True)]
        return jsonify({"titles":data,"count":len(data)})
    except Exception as e:
        #print(f"Failed to retrieve data: {response.status_code}")
        #requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000)