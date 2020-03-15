import os

def get_uploaded_images():
    rootdir = os.getcwd()
    print (rootdir)
    imageList=[]

    for subdir, dirs, files in os.walk(rootdir + './app/static/uploads'):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                imageList.append(file)
    return imageList