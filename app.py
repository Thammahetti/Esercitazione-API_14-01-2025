from flask import Flask, render_template, redirect, url_for
import requests
app = Flask(__name__)
NASA_API_KEY = 'jmOsozqK9e1gHTW8aB7IXYZhQMWUBeuPFghiXEJg' #api kei della nasa

#ourte /nasa per immagine NASA
@app.route('/nasa')
def nasa_home():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}')
    data = response.json() 
    return render_template('nasa.html', title=data.get("title"),description=data.get("explanation"), image_url=data.get("url"))

@app.route('/cat')
def cat_home():
    response = requests.get('https://catfact.ninja/fact')
    data = response.json() 
    return render_template('cat_fact.html', fact=data.get("fact"))

@app.route('/cat/change', methods=['POST'])
def cat_change():
    return redirect(url_for('cat_home'))

@app.route('/')
def home():
    
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)