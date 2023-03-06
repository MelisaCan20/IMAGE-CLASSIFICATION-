from kerastuner.tuners import RandomSearch
import tensorflow as tf

def build_model(hp):
  model = tf.keras.Sequential()

  #model.add(tf.keras.layers.AveragePooling2D(6,3,input_shape=(64,64,3)))

  for i in range(hp.Int("Conv Layers", min_value=0, max_value=3)):
    model.add(tf.keras.layers.Conv2D(hp.Choice(f"layer_{i}_filters", [16,32,64]), 3, activation='relu'))
  
  model.add(tf.keras.layers.MaxPool2D(2,2))
  model.add(tf.keras.layers.Dropout(0.5))
  model.add(tf.keras.layers.Flatten())

  model.add(tf.keras.layers.Dense(hp.Choice("Dense layer", [64, 128, 256,512,1024]), activation='relu'))

  model.add(tf.keras.layers.Dense(9, activation='softmax'))

  model.compile(optimizer='adam',
              loss="categorical_crossentropy",
              metrics=['accuracy'])
  
  return model

tuner = RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=32,
)

tuner.search(train,validation_data=test, epochs=10, batch_size=32)
