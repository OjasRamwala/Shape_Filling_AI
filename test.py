import os
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import tensorflow as tf

model = tf.keras.models.load_model("model.h5")

test_input = 'Test_Input'
test_ground_truth = 'Test_Ground_Truth'
outputs = 'Output'

os.makedirs(test_input, exist_ok = True)
os.makedirs(test_ground_truth, exist_ok = True)
os.makedirs(outputs, exist_ok = True)

count = 0
for image in os.listdir(test_input):
  count += 1
  input_path = os.path.join(test_input, image)
  input = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

  model_input = input.copy()
  model_input = model_input/255.0
  model_input = model_input.astype(np.float32)
  model_input = np.expand_dims(model_input, axis = 0)
  predicted_image = model.predict(model_input)
  predicted_image = predicted_image[0]
  predicted_image = (predicted_image>0.5)*255.0
  
  ground_truth_path = os.path.join(test_ground_truth, image)
  ground_truth = cv2.imread(ground_truth_path, cv2.IMREAD_GRAYSCALE)

  output = np.concatenate([np.squeeze(input), np.squeeze(predicted_image), np.squeeze(ground_truth)], axis = 1)
  cv2.imwrite('{}/{}.png'.format(outputs, count), output)