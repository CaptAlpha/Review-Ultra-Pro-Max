#Flask App
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import session as login_session
from flask import make_response
from sqlalchemy import create_engine
from scraperbs import getdata, html_code, cus_data, cus_rev

app = Flask(__name__)

#First Page Render - Home Page

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    link = ""
    #Request for link from index.html
    if request.method == 'POST':
        link = request.form['link']
        #redirect to scrape route
        return redirect(url_for('scrape', link=link))
    return render_template('index.html')

# Web Scraping route
@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    #return to scrape.html 
    link = request.args.get('link')
    #Go to the product reviews and scrape the data
    data = html_code(link)
    #return customer data
    cus_res = cus_data(data)
    rev_data = cus_rev(data)
    



    return render_template('scrape.html', link=link, cus_res=cus_res, cus_rev=rev_data)

    


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(debug=True)

