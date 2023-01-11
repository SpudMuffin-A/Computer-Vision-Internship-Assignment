# Internship Assignment
Internship Assignments

## Problem Statement 1: Max Pooling Problem

#### a) Given an (m × m) matrix and a (k × k) moving window, write a program to calculate the maximum value in the window for the whole image, for each position of the moving window. The output would be of size m × m.   

-> Solution provided in Max Pooling/maxPool1.py   
To run the program, download the file and enter the values of the matrix as a numpy array and the dimension of the sliding window as a tuple of 2 values.   
The program can then be compiled using any python compiler.  
The output will be the pooled matrix.   

#### b) Improve the performance of this implementation, by utilizing the structure of the maximum window and/or using the suitable data structures? Could you verify that your new implementation is actually faster than the previous one?   

-> Solution provided in Max Pooling/maxPoolUpdated.py   
To run the program, download the file and enter the values of the matrix as a numpy array and the dimension of the sliding window as an integer value.   
The program can then be compiled using any python compiler.  
The output will be the pooled matrix.  

To verify that the new updated solution was actually faster I used a common 4x4 matrix and sliding window dimension of 2x2 with each of the programs and found the total time they both took to fully run:  
Total run time of solution (a) = 0.34s.  
Total run time of solution (b) = 0.303s.  

#### c) Provide the worst-case performance of both the versions using Big O notation.   

-> Solution (a): Time complexity of O(log(m)).  
   Solution (b): Time complexity of O(m<sup>2</sup>).  


## Problem Statement 2: Fonts
Beth is a part of the graphics designer team in a Mass Customization Company and works on enhancing the customer's artworks like Business cards, Postcards etc. He needs to choose from a variety of fonts for a document based on the context. Many times, he requires to replicate the font used in the customer's uploaded image for adding new text. Estimating the font type manually from the image is a troublesome process. We want to build a Computer Vision-based solution for easing Beth's work.

#### a) Font Matching: Classify the fonts used for the written text in a given image. Write a software that will take an image as input and provides recommendations of matching fonts with the confidence level.   

-> I couldn't manage to come up with a solution in time for this problem.  

#### b) Bounding Box: There can be multiple "Hello World!" written in an image with different fonts. You need to extract each one of the "Hello World!" instances and classify its font. The output should be the bounding boxes coordinates containing the "Hello World!" and the type of font with confidence score as mentioned below.  

-> Solution provided in Fonts/fontMatch.py   
A folder containing sample images of the required fonts is also provided.  
To run the program, download the file and plug in the image to be matched in the 'url' variable.  
The program will give an image of the input with a bounding box around the 'Hello, World!' text along with the x, y, height and width values of the box.
