# TartanSense-Computer-Vision-Internship-Assignment
Tartan Sense Internship Assignments

Problem Statement 1:
Max Pooling Problem

a) Given an (m × m) matrix and a (k × k) moving window, write a program to calculate the maximum value in the window for the whole image, for each position of the moving window. The output would be of size m × m.

b) Improve the performance of this implementation, by utilizing the structure of the maximum window and/or using the suitable data structures? Could you verify that your new implementation is actually faster than the previous one?

c) Provide the worst-case performance of both the versions using Big O notation.


Problem Statement 2:
Fonts
Beth is a part of the graphics designer team in a Mass Customization Company and works on enhancing the customer's artworks like Business cards, Postcards etc. He needs to choose from a variety of fonts for a document based on the context. Many times, he requires to replicate the font used in the customer's uploaded image for adding new text. Estimating the font type manually from the image is a troublesome process. We want to build a Computer Vision-based solution for easing Beth's work.

a) Font Matching: Classify the fonts used for the written text in a given image. Write a software that will take an image as input and provides recommendations of matching fonts with the confidence level.

b) Bounding Box: There can be multiple "Hello World!" written in an image with different fonts. You need to extract each one of the "Hello World!" instances and classify its font. The output should be the bounding boxes coordinates containing the "Hello World!" and the type of font with confidence score as mentioned below.
