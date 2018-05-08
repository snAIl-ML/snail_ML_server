# from flask import Flask, render_template, url_for
# import os
# import path_helper_main_ml
# from label_image_no_cli import initialize_classifier, classify_image
# from flask import *
#
# graph, label = initialize_classifier('ml/train2model', 'training2model')
#
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return render_template('index.html')
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     file = request.files['image']
#     savepath = os.path.join("./current_image", file.filename)
#     file.save(savepath)
#     move = classify_image(savepath, graph, label)[0][0]
#     os.remove(savepath)
#     return move
from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome_page():
    return 'Welcome to sn_AI_l!'

@app.route('/ai')
def self_driven():
    return 'You are in the url designated to start and stop buttons!'
@app.route('/rc')
def user_driven():
    return 'You are in the url designated to left, right and forward buttons!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
