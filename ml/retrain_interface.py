import os
from module_urls import module_urls

def get_retrain_command(images_path, module_url, model_path, model_name):
    command_string = ("python retrain.py \\" +
        "--image_dir " + images_path + " \\" +
        "--tfhub_module " + module_url + " \\" +
        "--bottleneck_dir " + model_path + "/bottleneck \\" +
        "--output_graph " + model_path +  "/" + model_name + ".pb \\" +
        "--output_labels " + model_path +  "/" + model_name + "_labels.txt \\" +
        "--intermediate_output_graphs_dir " + model_path +  "/intermediate_graph/ \\" +
        "--summaries_dir " + model_path +  "/retrain_logs \\" +
        "--saved_model_dir " + model_path +  "/exported_graph")
    return command_string

def run_bash_command(command):
    os.system(command)

def retrain_model(
    images_path,
    module_url=module_urls["inception_v3"],
    model_path="./retrained_model",
    model_name="retrained_model"
    ):
    run_bash_command(get_retrain_command(images_path, module_url, model_path, model_name))
