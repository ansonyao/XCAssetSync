import os
image_path = '/Users/ansonyao/Desktop/GoogleDriveFiles/Two Tall Totems/Projects/Glyff/2-Assets/'
project_path = '/Users/ansonyao/Desktop/TestImageAssets/TestImageAssets/Assets.xcassets'
for path, dirs, files in os.walk(image_path):
    #Create same folders in the destination
    for dir in dirs:
        if path == image_path:
            destpath = os.path.join(project_path, dir)
        else:
            relpath = os.path.relpath(path, image_path)
            mappedPath = os.path.join(project_path, relpath)
            destpath = os.path.join(mappedPath, dir)
        if not os.path.exists(destpath):
            os.makedirs(destpath)
            print(destpath)
    #Copy 

  #  	os.mkdir 
   # for filename in files:
    #    print os.path.join(path, filename)        

