import numpy as np
import matplotlib.pyplot as plt
import cv2
from keras.models import load_model
from Paint import Draw

paint = Draw()
ret = paint.setting()
model = load_model("C:\\Users\\SURYA S\\Digits_Classification\\digits.h5")

img = cv2.imread(ret)
display_image = img[50:300, 0:250]
im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
im_crp = im[50:300, 0:250]
im_resize = cv2.resize(im_crp, (28, 28))
im_resize = im_resize/255
final = im_resize.reshape(1, 28*28)


pred = model.predict(final)
predicted_val = np.argmax(pred)
print(pred)
print(predicted_val)
flag = True
while flag:
    cv2.putText(img=display_image, text='Digit: '+str(predicted_val), org=(10, 50), fontFace=cv2.FONT_HERSHEY_DUPLEX, thickness=1, color=(0, 255, 0), fontScale=1)
    cv2.imshow("Image", display_image)
    k = cv2.waitKey(0) & 0xFF
    if k==27:
        flag = False
        break
    
    

cv2.destroyAllWindows()

