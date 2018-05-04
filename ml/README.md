STEP 1: pip3 install tensorflow_hub

python retrain.py -h

help ouput
usage: retrain.py [-h]

ALL FLAGS SET IN THE BOTTOM OF THE retrain.py FILE!

optional arguments:
  -h, --help            show this help message and exit
  --image_dir IMAGE_DIR
                        Path to folders of labeled images.
  --output_graph OUTPUT_GRAPH
                        Where to save the trained graph.
  --intermediate_output_graphs_dir INTERMEDIATE_OUTPUT_GRAPHS_DIR
                        Where to save the intermediate graphs.
  --intermediate_store_frequency INTERMEDIATE_STORE_FREQUENCY
                        How many steps to store intermediate graph. If "0"
                        then will not store.
  --output_labels OUTPUT_LABELS
                        Where to save the trained graph's labels.
  --summaries_dir SUMMARIES_DIR
                        Where to save summary logs for TensorBoard.
  --how_many_training_steps HOW_MANY_TRAINING_STEPS
                        How many training steps to run before ending.
  --learning_rate LEARNING_RATE
                        How large a learning rate to use when training.
  --testing_percentage TESTING_PERCENTAGE
                        What percentage of images to use as a test set.
  --validation_percentage VALIDATION_PERCENTAGE
                        What percentage of images to use as a validation set.
  --eval_step_interval EVAL_STEP_INTERVAL
                        How often to evaluate the training results.
  --train_batch_size TRAIN_BATCH_SIZE
                        How many images to train on at a time.
  --test_batch_size TEST_BATCH_SIZE
  How many images to test on. This test set is only used
                       once, to evaluate the final accuracy of the model
                       after training completes. A value of -1 causes the
                       entire test set to be used, which leads to more stable
                       results across runs.
 --validation_batch_size VALIDATION_BATCH_SIZE
                       How many images to use in an evaluation batch. This
                       validation set is used much more often than the test
                       set, and is an early indicator of how accurate the
                       model is during training. A value of -1 causes the
                       entire validation set to be used, which leads to more
                       stable results across training iterations, but may be
                       slower on large training sets.
 --print_misclassified_test_images
                       Whether to print out a list of all misclassified test
                       images.
 --bottleneck_dir BOTTLENECK_DIR
                       Path to cache bottleneck layer values as files.
 --final_tensor_name FINAL_TENSOR_NAME
                       The name of the output classification layer in the
                       retrained graph.
 --flip_left_right     Whether to randomly flip half of the training images
                       horizontally.
 --random_crop RANDOM_CROP
                       A percentage determining how much of a margin to
                       randomly crop off the training images.
 --random_scale RANDOM_SCALE
                       A percentage determining how much to randomly scale up
                       the size of the training images by.
 --random_brightness RANDOM_BRIGHTNESS
                       A percentage determining how much to randomly multiply
                       the training image input pixels up or down by.
 --tfhub_module TFHUB_MODULE
                       Which TensorFlow Hub module to use. See https://github
                       .com/tensorflow/hub/blob/r0.1/docs/modules/image.md
                       for some publicly available ones.
 --saved_model_dir SAVED_MODEL_DIR
                       Where to save the exported graph.
