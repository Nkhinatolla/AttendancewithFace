import os,shutil

folderPath = './pics'
croppedFol = "./Cropped_faces"
if os.path.exists(croppedFol):
    print(croppedFol)
    shutil.rmtree(croppedFol)
else:
    os.makedirs(croppedFol)
os.system("python take_image.py")
os.system("python train.py")
os.system("python spreadsheet.py")
for image in os.listdir(folderPath):
    os.system("python detect.py " + os.path.join(folderPath, image))
    os.system("python identify.py")
