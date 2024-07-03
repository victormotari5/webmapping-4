from flask import Flask, jsonify, render_template, send_from_directory
import os

app = Flask(__name__, template_folder=os.getcwd())

def read_data_from_file():
    data = []
    with open('data.txt', 'r') as f:
        for line in f:
            name, lat, lon, area, county = line.strip().split(',')
            data.append({
                "name": name,
                "latitude": float(lat),
                "longitude": float(lon),
                "area_sq_km": area,
                "county": county
            })
    return data

@app.route('/api/locations')
def get_locations():
    locations = read_data_from_file()
    return jsonify(locations)

@app.route('/')
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/database')
def database():
    locations = read_data_from_file()
    return render_template('database.html', locations=locations)

if __name__ == '__main__':
    app.run(debug=True)
