import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pylab as plt
import numpy as np
mobilenet_v2 = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
model_layers = hub.KerasLayer(mobilenet_v2, input_shape=(224,224,3))
mobile_net_layers.trainable = False
model = tf.keras.Sequential([
  model_layers,
  tf.keras.layers.Dropout(0.3),
  tf.keras.layers.Dense(9,activation='softmax')])
model.compile(optimizer = tf.keras.optimizers.Adam(), loss = tf.keras.losses.CategoricalCrossentropy(from_logits=True), metrics = ["accuracy"])
model_fit = model.fit(train_gen, epochs=20, validation_data=valid_gen)
loss, accuracy = model.evaluate(test_gen)
