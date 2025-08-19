import cv2
import numpy as np

# 1. Reading and Displaying Images

image =cv2.imread("apple.jpg")
img= cv2.resize(image, (500,500)) # resize the image but not the current one 
# print(img.shape)
# gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # change the color to bray scale 
# print(img)
# cv2.imshow("apple image",img) # show the image but make sure to add waitkey
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()

# cv2.imwrite("new.png",img) 

# 2. Drawing Shapes on Images

# rectangle on image

# cv2.rectangle(img, (50,50), (400,400), (255,0,0), 3)

# # circle on image

# cv2.circle(img, (150,150), (100), (0,255,0), 4)

# # line on image

# cv2.line(img, (50,50),(450,450),(0,0,255), 3)

# cv2.imwrite("edited.png",img)

# cv2.imshow("apple image",img) # show the image but make sure to add waitkey
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()
    

# import numpy as np

# # Create a blank image
# canvas = np.zeros((500, 500, 3), dtype="uint8")

# # Draw a rectangle
# cv2.rectangle(canvas, (50, 50), (200, 200), (0, 255, 0), 3)

# # Draw a circle
# cv2.circle(canvas, (300, 300), 50, (255, 0, 0), -1)

# # Draw a line
# cv2.line(canvas, (100, 100), (400, 400), (0, 0, 255), 5)

# cv2.imshow("Shapes", canvas)
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()


# Open webcam
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     cv2.imshow("Webcam Feed", frame)
    
#     # Press 'q' to exit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()




# # Load the pre-trained Haar cascade classifier for face detection


# 1.  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")



# # Capture video from webcam
# cap = cv2.VideoCapture(0)  # 0 = Default webcam

# while True:
#     # Read a frame from the webcam
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the grayscale frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

#     # Draw rectangles around detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Green rectangle

#     # Display the frame with detected faces
#     cv2.imshow("Live Face Detection", frame)

#     # Exit if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# cap.release()
# cv2.destroyAllWindows()



#  2. Deep Learning based (DNN Face Detector)
    # more accurate than Haar cascade classifier


# import cv2

# # Load DNN model (make sure files are in same folder)
# net = cv2.dnn.readNetFromCaffe(
#     "deploy.prototxt",
#     "res10_300x300_ssd_iter_140000.caffemodel"
# )

# # Open webcam (0 = default camera)
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     (h, w) = frame.shape[:2]

#     # Prepare input for the DNN
#     blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
#                                  (300, 300), (104.0, 177.0, 123.0))

#     net.setInput(blob)
#     detections = net.forward()

#     # Loop over detections
#     for i in range(detections.shape[2]):
#         confidence = detections[0, 0, i, 2]

#         if confidence > 0.5:  # Threshold
#             box = detections[0, 0, i, 3:7] * [w, h, w, h]
#             (startX, startY, endX, endY) = box.astype("int")

#             # Draw bounding box
#             cv2.rectangle(frame, (startX, startY), (endX, endY),
#                           (0, 255, 0), 2)
#             text = f"{confidence*100:.2f}%"
#             cv2.putText(frame, text, (startX, startY - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

#     # Show video
#     cv2.imshow("Live Face Detection", frame)

#     # Press 'q' to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# 3. Mediapipe Face Detection (Google’s Model – Faster & More Accurate)
# first add package < uv add mediapipe>


# import cv2
# import mediapipe as mp

# # Initialize mediapipe
# mp_face_detection = mp.solutions.face_detection
# mp_drawing = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0)

# with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Convert BGR to RGB
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = face_detection.process(rgb_frame)

#         # Draw detections
#         if results.detections:
#             for detection in results.detections:
#                 mp_drawing.draw_detection(frame, detection)

#         cv2.imshow("Mediapipe Face Detection", frame)

#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

# cap.release()
# cv2.destroyAllWindows()


