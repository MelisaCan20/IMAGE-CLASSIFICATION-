import splitfolders 
input_folder = "C:/Users/melisa/Desktop/Son//Dataset"
output = "C:/Users/melisa/Desktop/Son/DatasetOutput2" 
splitfolders.ratio(input_folder, output=output, seed=42, ratio=(.7, .2, .1))

from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

#load datasets
datagen = ImageDataGenerator(rescale=1./255)
train_gen = datagen.flow_from_directory(train_dir,
                                        target_size=(224,224),
                                        batch_size = 32,
                                        class_mode = 'categorical')

valid_gen = datagen.flow_from_directory(val_dir,
                                        target_size=(224,224),
                                        batch_size = 32,
                                        class_mode = 'categorical')

test_gen = datagen.flow_from_directory(test_dir,
                                        target_size=(224,224),
                                        batch_size = 32,
                                        class_mode = 'categorical')
