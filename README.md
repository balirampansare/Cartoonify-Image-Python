<h1 align="center">Cartoonify The Image</h1>
<p align="center">
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
<img src="https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=whit" />
</p>

1. **Libraries to Import**

    Import the Numpy and Open cv2 libraries
    
    pip commands to install numpy and opencv
    ```
    1. pip install numpy
    2. pip install opencv-python
    ```
    ```
    import cv2
    import numpy as np
    ```

2. **Read the Image**
    ```
    img = cv2.imread("image//nature.jpg")
    cv2.imshow("input-1",img)
    ```
    If you want to resize the image window, add the below code
    ```
    pic = cv2.resize(img, (width,height)) 
    ```
    ![Read Image](/image/input.PNG)

3. **Convert the image to gray**
    ```
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray-2", gray)
    ```
    ![Gray Image](/image/gray.PNG)

4. **Blur the gray converted image**

    Syntax:
    ```
    cv2.medianBlur(input_image, kernel_size)
    ```
    Code:
    ```
    gray = cv2.medianBlur(gray,3)
    cv2.imshow("blur-3", gray)
    ```
    ![Blur Image](/image/blur.PNG)
     
5. **Perform Adaptive Threshold**

    AdaptiveThreshold function performs the adaptive threshold to find dark edges

    syntax:
    ```
    adaptiveThreshold(src, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C)
    ```
    Code:
    ```
    adaptiveThreshold(src, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C)
    ```
    ![Adapative Threshold Image](/image/edges.PNG)

    Depending on the Image, change the numbers in the code in order to get best output

6. **Apply Bilateral Filter**

    A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images.
    
    Syntax:
    ```
    cv2.bilateralFilter ( src, dst, d, sigmaColor,sigmaSpace, borderType = BORDER_DEFAULT )
    ```
    To know more about bilateral Filter:
    [Link](https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html)

    Code:
    ```
    color = cv2.bilateralFilter(img,2,250,250)
    cv2.imshow("bilateral-5",color)
    ```
    ![Smooth Image](/image/bilateral.PNG)

    Depending on the Image, change the numbers in the code in order to get best output
    
7. **Final Output**

    Performing bitwise_and on blurred image and masking the edged image.

    Syntax:
    ```
    bitwise_and(source1_array, source2_array,destination_array, mask)
    ```

    Code:
    ```
    cartoon = cv2.bitwise_and(color,color,mask=edges)
    cv2.imshow("output-6",cartoon)
    ```
    ![Output](/image/output.PNG)




