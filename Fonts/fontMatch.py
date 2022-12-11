import cv2 as cv
from google.colab.patches import cv2_imshow
import pytesseract
from PIL import Image
url = "/content/ubuntu.png" #Input Image
img = cv.imread(url)
im = Image.open(url)
im = im.resize((600,250))
text = pytesseract.image_to_string(im)
# print(text[:-1]) #Prints the text found in the image using Google Tesseract OCR
if(text=='Hello, World!'):
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #Converting the image into grayscale to enhance the text processing

  ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
  cv.imwrite('thresh_img.jpg',thresh) #Saves the threshold image 

  rect_kern = cv.getStructuringElement(cv.MORPH_RECT, (12, 12))

  dil = cv.dilate(thresh, rect_kern, iterations = 5) #Generating the dilation amount to get the boundaries of the text
  cv.imwrite('dil_img.jpg',dil)

  contour, hierarchy = cv.findContours(dil, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) #Used to get the area of the white pixels 

  im2 = img.copy()
  for cnt in contour:
      x, y, w, h = cv.boundingRect(cnt)
       
      rect=cv.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) #Draw the bounding box on the text area
        
      crop = im2[y:y + h, x:x + w]  #Crop the bounding box area
        
      cv.imwrite('boundingBox.jpg',rect)

      file = open("textOp.txt", "a")

      file.write(text)  #Adding the text to a file
      file.write("\n")
      file.close
      
      op = {"detectedFonts":[
          {"boundingBox":{
              "x":x,
              "y":y,
              "width":w,
              "height":h
          }    
          }]}  #Output Array

  print(op)
