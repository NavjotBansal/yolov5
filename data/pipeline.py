import os 

LABEL_DIR = os.cwd()+"/labels/train/"

for el in os.listdir(LABEL_DIR):
	print(el)