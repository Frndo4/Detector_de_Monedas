from cv2 import cv2
imagen=cv2.imread(r"C:\Users\fer-j\Pictures\contorno1.jpg")
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
tipo_umbral,umbral=cv2.threshold(grises,100,255,cv2.THRESH_BINARY)
contorno,jerarquia=cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contorno,-1,(255,0,52),3)

#Mostrar
cv2.imshow('Imagen original',imagen)
cv2.imshow('Imagen en grises',grises)
cv2.imshow('Imagen con umbral',umbral)
print(tipo_umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()