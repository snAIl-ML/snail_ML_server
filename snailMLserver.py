import os
import path_helper_main_ml
from classifier import initialize_classifier, classify_image
from flask import Flask, render_template, url_for, redirect
import requests

graph, label = initialize_classifier()
URL = 'http://192.168.49.20:5000'

from flask import Flask
app = Flask(__name__)

# USER ROUTES
@app.route('/')
def welcome_page():
    return render_template('index.html')

@app.route('/ai')
def self_driven():
    return 'You are in the url designated to start and stop buttons!'

@app.route('/rc')
def user_driven():
    html_return = requests.get(URL).text
    image_url = URL + html_return.split("img src=")[1].split('><')[0]
    return render_template('rc.html',image_url=image_url)

@app.route('/making_of')
def tutorials():
    return 'You are in the url designated to explain how this project made!'

@app.route('/authors')
def authors():
    return 'You are in the url designated to introduce you to the 4 authors!'

@app.route('/route_left')
def get_move_left():
    left_command = requests.get(URL + '/piv_left')
    print(left_command)
    return redirect('/rc')

@app.route('/route_forward')
def get_move_forward():
    forward_command = requests.get(URL + '/forward')
    return redirect('/rc')

@app.route('/route_right')
def get_move_right():
    right_command = requests.get(URL + '/piv_right')
    return redirect('/rc')

# API ROUTES
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    savepath = os.path.join("./current_image", file.filename)
    file.save(savepath)
    move = classify_image(savepath, graph, label)[0][0]
    os.remove(savepath)
    return move


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
