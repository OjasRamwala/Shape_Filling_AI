import os
import numpy as np
import cv2
from glob import glob
import tensorflow as tf
from sklearn.model_selection import train_test_split


def load_dataset(dataset_path):    
    inputs = sorted(glob(os.path.join(dataset_path, "Input\*")))
    outputs = sorted(glob(os.path.join(dataset_path, "Output\*")))

    train_x, valid_x = train_test_split(inputs, test_size = 0.25, random_state = 42)
    train_y, valid_y = train_test_split(outputs, test_size = 0.25, random_state = 42)

    return (train_x, train_y), (valid_x, valid_y)

def read_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = img/255.0
    img = img.astype(np.float32)
    img = np.expand_dims(img, axis = -1)
    return img

def preprocess(input_path, output_path):
    def func(input_path, output_path):
        input_path = input_path.decode()
        output_path = output_path.decode()

        x = read_image(input_path)
        y = read_image(output_path)

        return x, y

    input, output = tf.numpy_function(func, [input_path, output_path], [tf.float32, tf.float32])
    input.set_shape([256, 256, 1])
    output.set_shape([256, 256, 1])

    return input, output

def tf_dataset(inputs, outputs, batch = 8):
    dataset = tf.data.Dataset.from_tensor_slices((inputs, outputs))
    dataset = dataset.shuffle(buffer_size = 10000)
    dataset = dataset.map(preprocess)
    dataset = dataset.batch(batch)
    dataset = dataset.prefetch(2)
    return dataset

if __name__ == "__main__":
    dataset_path = 'Shape_Filling_AI\'
    (train_x, train_y), (valid_x, valid_y) = load_dataset(dataset_path)
    train_dataset = tf_dataset(train_x, train_y, batch = batch_size)
    valid_dataset = tf_dataset(test_x, test_y, batch = batch_size)