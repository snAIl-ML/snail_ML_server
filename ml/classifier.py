# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
'Classifier module'
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import re
import numpy as np
import tensorflow as tf

def get_model_name(path="./ml/model"):
    'Function to get model name'
    model_name = [x for x in os.listdir(path) if re.match(".*(.pb)", x)][0]
    return model_name.split(".pb")[0]

def initialize_classifier(
        model_name=get_model_name()
    ):
    'Function to get classifier'

    # load graph
    model_file = "./ml/model/" + model_name + ".pb"
    graph = tf.Graph()
    graph_def = tf.GraphDef()
    with open(model_file, "rb") as file:
        graph_def.ParseFromString(file.read())
    with graph.as_default():
        tf.import_graph_def(graph_def)

    # load labels
    label_file = "./ml/model/" + model_name + "_labels.txt"
    label = []
    proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
    for lab in proto_as_ascii_lines:
        label.append(lab.rstrip())

    return graph, label

def read_tensor_from_image_file(file_name,
                                input_height=299,
                                input_width=299,
                                input_mean=0,
                                input_std=255):
    'Function to read tensorflow'
    input_name = "file_reader"
    file_reader = tf.read_file(file_name, input_name)
    if file_name.endswith(".png"):
        image_reader = tf.image.decode_png(
            file_reader, channels=3, name="png_reader"
        )
    elif file_name.endswith(".gif"):
        image_reader = tf.squeeze(
            tf.image.decode_gif(file_reader, name="gif_reader")
        )
    elif file_name.endswith(".bmp"):
        image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
    else:
        image_reader = tf.image.decode_jpeg(
            file_reader, channels=3, name="jpeg_reader"
        )
    float_caster = tf.cast(image_reader, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0)
    resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.Session() # does this process close? possible memory leak cause..
    result = sess.run(normalized)
    return result

def classify_image(img_path, graph, labels):
    'Function to classify images'
    tens = read_tensor_from_image_file(file_name=img_path)
    input_name = "import/" + "Placeholder"
    output_name = "import/" + "final_result"
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    with tf.Session(graph=graph) as sess: # this bit is the core of the routine
        results = sess.run(output_operation.outputs[0], {
            input_operation.outputs[0]: tens
        })
    results = np.squeeze(results) # can cut off everything except the first choice?

    top_k = results.argsort()[-5:][::-1]
    final_output = []
    for i in top_k:
        final_output.append([labels[i], results[i]])
    return final_output
