import os
import random
import path_helper_test_ml

from retrain_interface import get_retrain_command, run_bash_command

def test_get_retrain_command_generates_command_string_properly():
    images_path = "test_dir"
    module_url = "test_url"
    model_path = "./model"
    model_name = "model_name"
    command_string = get_retrain_command(
    images_path, module_url, model_path, model_name)
    expected_return = ("python retrain.py \\" +
        "--image_dir test_dir \\" +
        "--tfhub_module test_url \\" +
        "--bottleneck_dir ./model/bottleneck \\" +
        "--output_graph ./model/model_name.pb \\" +
        "--output_labels ./model/model_name_labels.txt \\" +
        "--intermediate_output_graphs_dir ./model/intermediate_graph/ \\" +
        "--summaries_dir ./model/retrain_logs \\" +
        "--saved_model_dir ./model/exported_graph")
    assert(command_string) == expected_return

def test_run_bash_command_runs_command():
    filename = "testfile" + str(random.random())
    run_bash_command("touch " + filename)
    assert (filename in os.listdir('.')) == True
    run_bash_command("rm " + filename)
