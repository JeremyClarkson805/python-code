import numpy as np
import cv2
IMAGE_FILE="D:\\photo\\aidaishu.jpg"
image=cv2.imread(IMAGE_FILE)#读取照片
image=cv2.resize(image,dsize=(378,504))
IMAGE=cv2.medianBlur(image,3)#均值处理这张照片
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#把图像变成灰度图
cv2.imshow("OriginGray",image)#显示照片
lap=cv2.Laplacian(image,cv2.CV_64F)#用Laplace算子对图像进行卷积运算
cv2.imshow("Laplacian-X",lap)
lap=np.uint8(np.absolute(lap))#因为有负值被当作0处理了，所以需要取绝对值
cv2.imshow("Laplacian-X-Abs",lap)
sobeLX=cv2.Sobel(image,cv2.CV_64F,1,0)#用sobel算子对图像进行卷积运算(1，0)代表x轴向(横向)
sobelY=cv2.Sobel(image,cv2.CV_64F,0,1)#用sobel算子对图像进行卷积运算(0,1)代表Y轴向(纵向)
cv2.imshow("Sobel-X",sobeLX)
cv2.imshow("Sobel-Y",sobelY)
sobelX=np.uint8(np.absolute(sobeLX))
sobelY=np.uint8(np.absolute(sobelY))
cv2.imshow("Sobel-X-Abs",sobelX)
cv2.imshow("Sobel-Y-Abs",sobelY)
sobelCombined=cv2.bitwise_or(sobelX,sobelY)
cv2.imshow("Sobel-Combine",sobelCombined)
sobelCombined=cv2.GaussianBlur(sobelCombined,(5,5),0)#高斯去噪
cv2.imshow("Sobel-Combine-Gauss",sobelCombined)
sobelCombined=cv2.Canny(sobelCombined,30,150)#画边
cv2.imshow("Sobel-Canny-Detect",sobelCombined)
cv2.waitKey(0)#按任意键
cv2.destroyAllWindows()#退出所有显示窗口
