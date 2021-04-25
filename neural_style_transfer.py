import imutils
import cv2
import numpy as np

def get_model_from_path(style_model_path):
    model = cv2.dnn.readNetFromTorch(style_model_path)
    return model

def style_transfer(image, model):
    (h, w) = image.shape[:2]
    # image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) #PIL Jpeg to Opencv image

    blob = cv2.dnn.blobFromImage(image, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
    model.setInput(blob)
    output = model.forward()

    output = output.reshape((3, output.shape[2], output.shape[3]))
    output[0] += 103.939
    output[1] += 116.779
    output[2] += 123.680
    output /= 255.0
    output = output.transpose(1, 2, 0)
    output = np.clip(output, 0.0, 1.0)
    output = imutils.resize(output, width=500)
    return output
