import os
import shutil
from os.path import join
import time

pa=str(input("Enter path of directory -> "))
ext=str(input("Enter ext -> "))
choice=str(input("Would you like to keep the content in folder ?"))
l=[]
for (dirname, dirs, files) in os.walk(pa):
   for filename in files:
      if filename.endswith(ext) :
         thefile = os.path.join(dirname,filename)
         #print(thefile)
         l.append(thefile)
for f in l:
   shutil.copy(f,'D:\\commandPro')
print(l)

if choice=='no':
   time.sleep(30)
   folder = 'D:\\commandPro'
   for the_file in os.listdir(folder):
      file_path = os.path.join(folder, the_file)
      try:
         if os.path.isfile(file_path):
            os.unlink(file_path)
      except Exception as e:
         print(e)
   print("content deleted")
else:
   print("ok")

