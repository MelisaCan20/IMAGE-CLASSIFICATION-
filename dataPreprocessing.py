#tekrar eden verilerin temizlenmesi
from difPy import dif
for category in categoryNames:
    print(category)
    search = dif("Dataset/"+category,delete=True)
#hata oluşturulan verilerin temizlenmesi
import cv2
for category in categoryNames:
    os.chdir(category) 
    print('=> '+category) 
    for file in os.listdir('./'):
        img = cv2.imread(file) 
        if(isinstance(img, type(None))):
            os.remove(file)
    os.chdir('..') 

  
