'Routes of the server'
import os
import requests
from flask import Flask, render_template, redirect, request
# Attention, linter stating: E:  5, 0: Unable to import 'classifier' (import-error)
from classifier import initialize_classifier, classify_image

GRAPH, LABEL = initialize_classifier()
URL = 'http://192.168.49.20:5000'

APP = Flask(__name__)

# USER ROUTES
@APP.route('/')
def welcome_page():
    'Main route'
    return render_template('index.html')

@APP.route('/ai')
def self_driven():
    'AI route'
    return 'You are in the url designated to start and stop buttons!'

@APP.route('/rc')
def user_driven():
    'RC route'
    html_return = requests.get(URL).text
    image_url = URL + html_return.split("img src=")[1].split('><')[0]
    return render_template('rc.html', image_url=image_url)

@APP.route('/making_of')
def tutorials():
    'Process throughout the project route'
    return 'You are in the url designated to explain how this project made!'

@APP.route('/authors')
def authors():
    'Authors route'
    return 'You are in the url designated to introduce you to the 4 authors!'

@APP.route('/route_left')
def get_move_left():
    'Move left request'
    requests.get(URL + '/piv_left')
    return redirect('/rc')

@APP.route('/route_forward')
def get_move_forward():
    'Move forward request'
    requests.get(URL + '/forward')
    return redirect('/rc')

@APP.route('/route_right')
def get_move_right():
    'Move right request'
    requests.get(URL + '/piv_right')
    return redirect('/rc')

# API ROUTES
@APP.route('/upload', methods=['POST'])
def upload_file():
    'API routess'
    file = request.files['image']
    savepath = os.path.join("./current_image", file.filename)
    file.save(savepath)
    move = classify_image(savepath, GRAPH, LABEL)[0][0]
    os.remove(savepath)
    return move


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=8000)
