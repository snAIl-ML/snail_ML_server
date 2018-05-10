'Module for retraining interface'
import os
import time
from module_urls import module_urls

def get_retrain_command(images_path, module_url, model_path, model_name):
    'Function to retrain command'
    command_string = ("python retrain.py \\" +
                      "--image_dir " + images_path + " \\" +
                      "--tfhub_module " + module_url + " \\" +
                      "--bottleneck_dir " + model_path + "/bottleneck \\" +
                      "--output_graph " + model_path +  "/" + model_name + ".pb \\" +
                      "--output_labels " + model_path +  "/" + model_name + "_labels.txt \\" +
                      "--intermediate_output_graphs_dir " + model_path +
                      "/intermediate_graph/ \\" +
                      "--summaries_dir " + model_path +  "/retrain_logs \\" +
                      "--saved_model_dir " + model_path +  "/exported_graph")
    return command_string

def run_bash_command(command):
    'Function to write in the terminal'
    os.system(command)

def retrain_model(images_path, module_url=module_urls["inception_v3"]):
    'Function to retrain modelr'
    model_name = "snail_" + time.strftime("%Y_%b_%d_%a_%H_%M", time.localtime())
    model_path = "./" + model_name
    run_bash_command(get_retrain_command(images_path, module_url, model_path, model_name))
