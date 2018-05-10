import os
import path_helper_main_ml
from classifier import initialize_classifier, classify_image
from flask import Flask, render_template, url_for, redirect, request
import requests

graph, label = initialize_classifier()
REMOTE_API_PORT = "5000"

app = Flask(__name__)
app.secret_key = 'SUPER SECRET KEY'

# USER ROUTES
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

@app.route('/rc')
def user_driven():
    html_return = requests.get(URL).text
    image_url = URL + html_return.split("img src=")[1].split('><')[0]
    return render_template('rc.html',image_url=image_url)

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

@app.route('/ai_move')
def ai_move():
    requests.get(session['ip'] + '/ai_move?host_url=' + request.base_url + '/upload')
    return redirect('/rc')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
