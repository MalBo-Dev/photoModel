from os import popen
from exif import Image
print (" ____  _           _         __  __           _      _")
print ("|  _ \| |__   ___ | |_ ___  |  \/  | ___   __| | ___| |")
print ("| |_) | '_ \ / _ \| __/ _ \ | |\/| |/ _ \ / _` |/ _ \ |")
print ("|  __/| | | | (_) | || (_) || |  | | (_) | (_| |  __/ |")
print ("|_|   |_| |_|\___/ \__\___/ |_|  |_|\___/ \__,_|\___|_|")
print('')
print(" >>> GitHub : https://github.com/MalBo-Dev <<<")
print('')
print("   >>> Telegram Chanell : https://T.me/MalBo_Dev <<<")
print ('')
print("          >>> OWNER : </> MONSTER_hp </> <<<")
print('')
pic = input ("Photo Address : ")
img = Image(open(pic,"rb"))
try:
    model = img.model
except:
    exit()
print("Model : {}".format(model))
command = "google https://www.google.com/search?q=\"{}\"".format(model)
popen(command)

#HACKER BY MONSTER_HP