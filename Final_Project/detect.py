import cv2
import numpy as np
import tflite_runtime.interpreter as tflite

class Detector:
    def __init__(self, model_path="detect.tflite"):
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def detect(self, frame):
        input_shape = self.input_details[0]['shape']
        h, w = input_shape[1], input_shape[2]

        img = cv2.resize(frame, (w, h))
        img = np.expand_dims(img, axis=0).astype(np.uint8)

        self.interpreter.set_tensor(self.input_details[0]['index'], img)
        self.interpreter.invoke()

        boxes = self.interpreter.get_tensor(self.output_details[0]['index'])[0]
        classes = self.interpreter.get_tensor(self.output_details[1]['index'])[0]
        scores = self.interpreter.get_tensor(self.output_details[2]['index'])[0]

        detections = []

        for i in range(len(scores)):
            if scores[i] > 0.4 and int(classes[i]) == 0:
                y1, x1, y2, x2 = boxes[i]

                x1 = int(x1 * frame.shape[1])
                y1 = int(y1 * frame.shape[0])
                x2 = int(x2 * frame.shape[1])
                y2 = int(y2 * frame.shape[0])

                detections.append([x1, y1, x2, y2, float(scores[i])])

        return detections