from cv2 import cv2
import numpy as np

valorGauss=1
valorKernel=7
original=cv2.imread(r"C:\Users\fer-j\Pictures\MonedasMexico.jpg")
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
gauss_suavizado=cv2.GaussianBlur(gris,(valorGauss,valorGauss),0)
canny=cv2.Canny(gauss_suavizado,60,100)

kernel=np.ones((valorKernel,valorKernel),np.uint8)
cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
contornos,jerarquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("Monedas encontradas: {}".format(len(contornos)))
cv2.drawContours(original,contornos,-1,(0,0,255),2)

#Mostrar resultados
cv2.imshow("Monedas en escala de grises", gris)
cv2.imshow("Imagen suavizada", gauss_suavizado)
cv2.imshow("Canny", canny)
cv2.imshow("Cierre", cierre)
cv2.imshow("Resultado", original)
cv2.waitKey(0)


