from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return ('Welcome to Shirlys cars app!')

@app.route('/cars')
def cars_view():
    list_of_cars = []
    for i in range(1, 6):           # First 5 pages
        URL = 'https://www.cars24.com/buy-used-cars-chennai/?page={}'.format(i)
        try:
            page = requests.get(URL)
        except Exception as e:
            return ('An error occured: {}'.format(e))
        results = BeautifulSoup(page.content, 'html.parser')
        job_elems = results.find_all(itemprop="image")
        for i in job_elems:
            list_of_cars.append(i['alt'])
            list_of_cars.append(str(i))
    return '<br/>'.join(list_of_cars)


if __name__ == '__main__':
    app.run(debug=True)
