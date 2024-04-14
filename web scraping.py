from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_website(url, content):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find elements containing the specified content
        scraped_content = soup.find_all(text=lambda text: content.lower() in text.lower())
        return scraped_content
    except Exception as e:
        return [f"An error occurred: {e}"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        content = request.form['content']
        scraped_content = scrape_website(url, content)
        return render_template('result.html', url=url, content=content, scraped_content=scraped_content)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
