'Routes of the server'
import os
import path_helper_main_ml
from classifier import initialize_classifier, classify_image
from flask import Flask, render_template, url_for, redirect, request
import requests

graph, label = initialize_classifier()
URL = 'http://192.168.49.20:5000'

from flask import Flask
app = Flask(__name__)

# USER ROUTES
@app.route('/')
def welcome_page():
    'Main route'
    return render_template('index.html')

@app.route('/ai')
def self_driven():
    'AI route'
    return 'You are in the url designated to start and stop buttons!'

@app.route('/rc')
def user_driven():
    'RC route'
    html_return = requests.get(URL).text
    image_url = URL + html_return.split("img src=")[1].split('><')[0]
    return render_template('rc.html',image_url=image_url)

@app.route('/making_of')
def tutorials():
    'Process throughout the project route'
    return 'You are in the url designated to explain how this project made!'

@app.route('/authors')
def authors():
    'Authors route'
    return 'You are in the url designated to introduce you to the 4 authors!'

@app.route('/route_left')
def get_move_left():
    'Move left request'
    left_command = requests.get(URL + '/piv_left')
    print(left_command)
    return redirect('/rc')

@app.route('/route_forward')
def get_move_forward():
    'Move forward request'
    forward_command = requests.get(URL + '/forward')
    return redirect('/rc')

@app.route('/route_right')
def get_move_right():
    'Move right request'
    right_command = requests.get(URL + '/piv_right')
    return redirect('/rc')

# API ROUTES
@app.route('/upload', methods=['POST'])
def upload_file():
    'API routes'
    file = request.files['image']
    savepath = os.path.join("./current_image", file.filename)
    file.save(savepath)
    move = classify_image(savepath, graph, label)[0][0]
    os.remove(savepath)
    return move


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
