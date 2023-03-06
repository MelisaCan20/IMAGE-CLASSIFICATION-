#tekrar eden verilerin temizlenmesi
from difPy import dif
for category in categoryNames:
    print(category)
    search = dif("Dataset/"+category,delete=True)


  
