import cv2 as cv
capturaVideo=cv.VideoCapture(1)
if not capturaVideo.isOpened():
    print("¡No se encontró una cámara!")
    exit()
while True:
    tipocamara,camara=capturaVideo.read()
    gris=cv.cvtColor(camara,cv.COLOR_BGR2GRAY)
    cv.imshow("En Vivo", gris)
    if cv.waitKey(1)==ord("q"):
        break
capturaVideo.release()
cv.destroyAllWindows()
