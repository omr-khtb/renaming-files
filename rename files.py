import os 

path = os.chdir("C:\\Users\\Hp\\Desktop\\compressed\\26")

x = 329

for file in os.listdir(path):
    new_file_name="quran-page-{}.jpg".format(x)
    os.rename(file,new_file_name)

    x = x + 1