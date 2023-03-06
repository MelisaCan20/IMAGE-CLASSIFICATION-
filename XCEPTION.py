import tensorflow as tf
base_model = tf.keras.applications.Xception(
    weights='imagenet',  # Load weights pre-trained on ImageNet.
    input_shape=(100, 100, 3),
    include_top=False)

for layer in base_model.layers[:-5]:
    layer.trainable=False
inputs = tf.keras.Input(shape=(100, 100, 3))
x = base_model(inputs, training=False)

# Convert features of shape `base_model.output_shape[1:]` to vectors
x = tf.keras.layers.GlobalAveragePooling2D()(x)
# A Dense classifier with a single unit (binary classification)
x=tf.keras.layers.Dense(64,activation='relu') (x)
outputs =tf. keras.layers.Dense(5)(x)
model = tf.keras.Model(inputs, outputs)
model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss="categorical_crossentropy",
              metrics=["accuracy"])
model.fit(train, epochs=2, validation_data=test)
