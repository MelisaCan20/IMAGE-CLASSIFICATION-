from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
image = load_img("kazak.jpg", target_size=(224,224))
image = img_to_array(image) / 255 # 0-255 -> 0-1
image = np.expand_dims(image, axis=0) 
pred = model.predict(image)
class_names[pred.argmax()]
