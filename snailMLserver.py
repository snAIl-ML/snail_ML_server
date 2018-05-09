import os
import path_helper_main_ml
from label_image_no_cli import initialize_classifier, classify_image
from flask import Flask, render_template, url_for, redirect, request, session
import requests

graph, label = initialize_classifier('ml/model8MayP2', 'model8MayP2')
SERVER_PORT = "8000"
REMOTE_API_PORT = "5000"

app = Flask(__name__)
app.secret_key = 'SUPER SECRET KEY'
# USER ROUTES

# USER ROUTES main page
@app.route('/')
def welcome_page():
    return render_template('index.html')

@app.route('/set_ip_address')
def set_ip_address():
    session['ip'] = 'http://' + request.args.get('ip') + ':' + REMOTE_API_PORT
    return redirect('/given_ip')

@app.route('/given_ip')
def select_mode_page():
    return render_template('given_ip.html')

# USER ROUTES AI
@app.route('/ai')
def self_driven():
    return render_template('ai.html')

@app.route('/start')
def start_ai():
    start = requests.get(session['ip'] + '/ai_start')
    return redirect('/ai')

@app.route('/stop')
def stop_ai():
    stop = requests.get(session['ip'] + '/ai_stop')
    return redirect('/ai')

# USER ROUTES RC

@app.route('/rc')
def user_driven():
    html_return = requests.get(session['ip']).text
    image_url = session['ip'] + html_return.split("img src=")[1].split('><')[0]
    return render_template('rc.html',image_url=image_url)

@app.route('/route_left')
def get_move_left():
    left_command = requests.get(session['ip'] + '/piv_left')
    return redirect('/rc')

@app.route('/route_forward')
def get_move_forward():
    forward_command = requests.get(session['ip'] + '/forward')
    return redirect('/rc')

@app.route('/route_right')
def get_move_right():
    right_command = requests.get(session['ip'] + '/piv_right')
    return redirect('/rc')

# USER ROUTES making of
@app.route('/making_of')
def tutorials():
    return 'You are in the url designated to explain how this project made!'

# USER ROUTES authors
@app.route('/authors')
def authors():
    return 'You are in the url designated to introduce you to the 4 authors!'

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
