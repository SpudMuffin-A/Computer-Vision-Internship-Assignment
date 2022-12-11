import cv2 as cv
from google.colab.patches import cv2_imshow
import pytesseract
from PIL import Image
url = "/content/ubuntu.png"
img = cv.imread(url)
im = Image.open(url)
im = im.resize((600,250))
# img.save('sample.png')
text = pytesseract.image_to_string(im)
# print(text[:-1])
if(text=='Hello, World!'):
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

  ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_OTSU |
                                              cv.THRESH_BINARY_INV)
  cv.imwrite('thresh_img.jpg',thresh)

  rect_kern = cv.getStructuringElement(cv.MORPH_RECT, (12, 12))

  dil = cv.dilate(thresh, rect_kern, iterations = 5)
  cv.imwrite('dil_img.jpg',dil)

  contour, hierarchy = cv.findContours(dil, cv.RETR_EXTERNAL,
                                                cv.CHAIN_APPROX_NONE)

  im2 = img.copy()
  for cnt in contour:
      x, y, w, h = cv.boundingRect(cnt)
        
        # Draw the bounding box on the text area
      rect=cv.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Crop the bounding box area
      crop = im2[y:y + h, x:x + w]
        
      cv.imwrite('boundingBox.jpg',rect)
        
        # open the text file
      file = open("textOp.txt", "a")
        
        # Using tesseract on the cropped image area to get text
        # text = pytesseract.image_to_string(cropped)
        
        # Adding the text to the file
      file.write(text)
      file.write("\n")
        
        # Closing the file
      file.close
        # cv2_imshow('rectBox.jpg')
      op = {"detectedFonts":[
          {"boundingBox":{
              "x":x,
              "y":y,
              "width":w,
              "height":h
          }    
          }]}

  print(op)
