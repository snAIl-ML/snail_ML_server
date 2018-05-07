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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf


def classify_image(model_path, model_name, img_path):

    file_name = img_path
    model_file = model_path + "/" + model_name + ".pb"
    label_file = model_path + "/" + model_name + "_labels.txt"
    input_height = 299
    input_width = 299
    input_mean = 0
    input_std = 255
    input_layer = "Placeholder"
    output_layer = "final_result"

    def load_graph(model_file):
      graph = tf.Graph()
      graph_def = tf.GraphDef()

      with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
      with graph.as_default():
        tf.import_graph_def(graph_def)

      return graph # can this be stored in memory or as environment variable? pretty hefty for ENV but maybe possible

    def read_tensor_from_image_file(file_name,
                                    input_height=299,
                                    input_width=299,
                                    input_mean=0,
                                    input_std=255):
      input_name = "file_reader"
      output_name = "normalized"
      file_reader = tf.read_file(file_name, input_name)
      if file_name.endswith(".png"):
        image_reader = tf.image.decode_png(
            file_reader, channels=3, name="png_reader")
      elif file_name.endswith(".gif"):
        image_reader = tf.squeeze(
            tf.image.decode_gif(file_reader, name="gif_reader"))
      elif file_name.endswith(".bmp"):
        image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
      else:
        image_reader = tf.image.decode_jpeg(
            file_reader, channels=3, name="jpeg_reader")
      float_caster = tf.cast(image_reader, tf.float32)
      dims_expander = tf.expand_dims(float_caster, 0)
      resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width]) # bet this bit is slow
      normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
      sess = tf.Session() # does this process close? possible memory leak cause..
      result = sess.run(normalized)

      return result


    def load_labels(label_file): # can probably turn this into ENV stuff also? investigate output, maybe it's not just strings...
      label = []
      proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
      for l in proto_as_ascii_lines:
        label.append(l.rstrip())
      return label

    graph = load_graph(model_file) # this bit here is probs heavy, reduce calls to this as much as possible
    t = read_tensor_from_image_file(
        file_name,
        input_height=input_height,
        input_width=input_width,
        input_mean=input_mean,
        input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)

    with tf.Session(graph=graph) as sess: # this bit is the core of the routine
        results = sess.run(output_operation.outputs[0], {
            input_operation.outputs[0]: t
        })
    results = np.squeeze(results) # might be trivial, but can cut off everything except the first choice?

    top_k = results.argsort()[-5:][::-1]
    labels = load_labels(label_file)
    final_output = []
    for i in top_k:
        final_output.append([labels[i], results[i]])
    return final_output
