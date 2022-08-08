import os
import numpy as np
import tensorflow as tf
from model import unet
from data import load_dataset, tf_dataset
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping

if __name__ == "__main__": 

  dataset_path = 'Shape_Filling_AI\'

  (train_x, train_y), (valid_x, valid_y) = load_dataset(dataset_path)
  train_dataset = tf_dataset(train_x, train_y, batch = batch_size)
  valid_dataset = tf_dataset(test_x, test_y, batch = batch_size)

  input_shape = (256, 256, 1)
  batch_size = 8
  epochs = 5
  lr = 3e-4
  model_path = 'model.h5'

  train_dataset = tf_dataset(train_x, train_y, batch = batch_size)
  valid_dataset = tf_dataset(test_x, test_y, batch = batch_size)

  model = build_unet(input_shape)
  model.compile(
      loss = tf.keras.losses.BinaryFocalCrossentropy(),
      optimizer = tf.keras.optimizers.Adam(lr),
      metrics = [
          tf.keras.metrics.MeanIoU(num_classes = 2),
          tf.keras.metrics.Recall(),
          tf.keras.metrics.Precision()
      ]
  )
  model.summary()


  callbacks = [
      ModelCheckpoint(model_path, monitor = "val_loss", verbose = 2),
      ReduceLROnPlateau(monitor="val_loss", patience = 2, factor = 0.1, verbose = 2),
      EarlyStopping(monitor="val_loss", patience = 3)
  ]

  train_steps = len(train_x)//batch_size
  if len(train_x) % batch_size != 0:
    train_steps += 1
  print(train_steps)

  valid_steps = len(test_x)//batch_size
  if len(test_x) % batch_size != 0:
    valid_steps += 1
  print(valid_steps)

  model.fit(
      train_dataset,
      validation_data = valid_dataset,
      epochs = epochs,
      steps_per_epoch = train_steps,
      validation_steps = valid_steps,
      callbacks = callbacks
  ) 

