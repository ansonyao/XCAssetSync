import os
image_path = '/Users/ansonyao/Desktop/GoogleDriveFiles/Two Tall Totems/Projects/Glyff/2-Assets/'
project_path = '/Users/ansonyao/Desktop/TestImageAssets'
for path, dirs, files in os.walk(image_path):
    for filename in files:
        print os.path.join(path, filename)
        

