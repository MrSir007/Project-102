import cv2
import time
import random
import dropbox

start_time = time.time()

def capture () :
  number = random.randint(100000,999999)
  videocaptureobject = cv2.VideoCapture(0)
  result = True
  while (result) :
    # To read the frames while the camera is on
    ret, frame = videocaptureobject.read()
    # To save an image to any storage device
    nameGenerate = "image" + str(number) + ".png"
    cv2.imwrite(nameGenerate, frame)
    start_time = time.time()
    result = False
  return nameGenerate

  # To release the camera
  videocaptureobject.release()
  # To close all windows
  cv2.destroyAllWindows()

def upload (name) :
  accesstoken = "kaVthpU4dy4AAAAAAAAAAXlefTW7jIMyeYDaxFkVBTiBUxp8bhCHtmBbvpoXI6_D"
  file = name
  filefrom = file
  fileto = "/Class 102/" + (name)
  dbx = dropbox.Dropbox(accesstoken)
  with open (filefrom, 'rb') as f :
    dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
    print("File Uploaded")

def main () :
  while(True) :
    if (time.time()-start_time) >= 300 :
      picture = capture()
      upload(picture)

main()