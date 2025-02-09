# import cv2 as cv
# import argparse
# import time

# parser = argparse.ArgumentParser()
# parser.add_argument('--input', help='Path to input image.')
# parser.add_argument('--proto', help='Path to .prototxt')
# parser.add_argument('--model', help='Path to .caffemodel')
# parser.add_argument('--dataset', help='Specify what kind of model was trained. '
#                                       'It could be (COCO, MPI) depends on dataset.')
# parser.add_argument('--thr', default=0.1, type=float, help='Threshold value for pose parts heat map')
# parser.add_argument('--width', default=368, type=int, help='Resize input to specific width.')
# parser.add_argument('--height', default=368, type=int, help='Resize input to specific height.')

# args = parser.parse_args()

# if args.dataset == 'COCO':
#     BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
#                   "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
#                   "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
#                   "LEye": 15, "REar": 16, "LEar": 17, "Background": 18}

#     POSE_PAIRS = [["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
#                   ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
#                   ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
#                   ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
#                   ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]]
# elif args.dataset == 'MPI':
#     BODY_PARTS = {"Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
#                   "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
#                   "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
#                   "Background": 15}

#     POSE_PAIRS = [["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
#                   ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
#                   ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
#                   ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"]]
# else:
    
#     BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4, "LShoulder": 5,
#                   "LElbow": 6, "LWrist": 7, "MidHip": 8, "RHip": 9, "RKnee": 10, "RAnkle": 11, "LHip": 12,
#                   "LKnee": 13, "LAnkle": 14, "REye": 15, "LEye": 16, "REar": 17, "LEar": 18, "LBigToe": 19,
#                   "LSmallToe": 20, "LHeel": 21, "RBigToe": 22, "RSmallToe": 23, "RHeel": 24, "Background": 25}

#     POSE_PAIRS = [["Neck", "MidHip"], ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
#                   ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"], ["MidHip", "RHip"],
#                   ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["MidHip", "LHip"], ["LHip", "LKnee"],
#                   ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"], ["REye", "REar"], ["Nose", "LEye"],
#                   ["LEye", "LEar"], ["RShoulder", "REar"], ["LShoulder", "LEar"], ["LAnkle", "LBigToe"],
#                   ["LBigToe", "LSmallToe"], ["LAnkle", "LHeel"], ["RAnkle", "RBigToe"], ["RBigToe", "RSmallToe"],
#                   ["RAnkle", "RHeel"]]

# inWidth = args.width
# inHeight = args.height

# net = cv.dnn.readNetFromCaffe(args.proto, args.model)

    
# frame = cv.imread(args.input)
# frameWidth = frame.shape[1]
# frameHeight = frame.shape[0]

# inp = cv.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
# net.setInput(inp)
# start_t = time.time()
# out = net.forward()
    
# print("time is ", time.time()-start_t)
# Name = "Human Pose Estimation"
# cv.namedWindow(Name, cv.WINDOW_AUTOSIZE)

# points = []
# for i in range(len(BODY_PARTS)):
#     # Slice heatmap of corresponding body's part.
#     heatMap = out[0, i, :, :]

#     # Originally, we try to find all the local maximums. To simplify a sample
#     # we just find a global one. However only a single pose at the same time
#     # could be detected this way.
#     _, conf, _, point = cv.minMaxLoc(heatMap)
#     x = (frameWidth * point[0]) / out.shape[3]
#     y = (frameHeight * point[1]) / out.shape[2]

#     # Add a point if it's confidence is higher than threshold.
#     points.append((int(x), int(y)) if conf > args.thr else None)

# for pair in POSE_PAIRS:
#     partFrom = pair[0]
#     partTo = pair[1]
#     assert(partFrom in BODY_PARTS)
#     assert(partTo in BODY_PARTS)

#     idFrom = BODY_PARTS[partFrom]
#     idTo = BODY_PARTS[partTo]
#     if points[idFrom] and points[idTo]:
#         cv.line(frame, points[idFrom], points[idTo], (255, 74, 0), 3)
#         cv.ellipse(frame, points[idFrom], (4, 4), 0, 0, 360, (255, 255, 255), cv.FILLED)
#         cv.ellipse(frame, points[idTo], (4, 4), 0, 0, 360, (255, 255, 255), cv.FILLED)
#         cv.putText(frame, str(idFrom), points[idFrom], cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv.LINE_AA)
#         cv.putText(frame, str(idTo), points[idTo], cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv.LINE_AA)
       
# t, _ = net.getPerfProfile()
# freq = cv.getTickFrequency() / 1000
# cv.putText(frame, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv.LINE_AA)

# cv.imshow(Name, frame)
# cv.imwrite('result_'+args.input, frame)




import cv2 as cv
import argparse
import time
import os

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Path to input image.')
parser.add_argument('--proto', help='Path to .prototxt')
parser.add_argument('--model', help='Path to .caffemodel')
parser.add_argument('--dataset', help='Specify what kind of model was trained. It could be (COCO, MPI, BODY_25) depends on dataset.')
parser.add_argument('--thr', default=0.1, type=float, help='Threshold value for pose parts heat map')
parser.add_argument('--width', default=368, type=int, help='Resize input to specific width.')
parser.add_argument('--height', default=368, type=int, help='Resize input to specific height.')

args = parser.parse_args()

# Define BODY_PARTS and POSE_PAIRS based on the dataset
if args.dataset == 'COCO':
    BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                  "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                  "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
                  "LEye": 15, "REar": 16, "LEar": 17, "Background": 18}

    POSE_PAIRS = [["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
                  ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
                  ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
                  ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
                  ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]]

elif args.dataset == 'MPI':
    BODY_PARTS = {"Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                  "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                  "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
                  "Background": 15}

    POSE_PAIRS = [["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                  ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                  ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                  ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"]]

elif args.dataset == 'BODY_25':
    BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4, "LShoulder": 5,
                  "LElbow": 6, "LWrist": 7, "MidHip": 8, "RHip": 9, "RKnee": 10, "RAnkle": 11, "LHip": 12,
                  "LKnee": 13, "LAnkle": 14, "REye": 15, "LEye": 16, "REar": 17, "LEar": 18, "LBigToe": 19,
                  "LSmallToe": 20, "LHeel": 21, "RBigToe": 22, "RSmallToe": 23, "RHeel": 24, "Background": 25}

    POSE_PAIRS = [["Neck", "MidHip"], ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
                  ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"], ["MidHip", "RHip"],
                  ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["MidHip", "LHip"], ["LHip", "LKnee"],
                  ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"], ["REye", "REar"], ["Nose", "LEye"],
                  ["LEye", "LEar"], ["RShoulder", "REar"], ["LShoulder", "LEar"], ["LAnkle", "LBigToe"],
                  ["LBigToe", "LSmallToe"], ["LAnkle", "LHeel"], ["RAnkle", "RBigToe"], ["RBigToe", "RSmallToe"],
                  ["RAnkle", "RHeel"]]

else:
    raise ValueError("Invalid dataset specified. Use 'COCO', 'MPI', or 'BODY_25'.")

# Set input dimensions
inWidth = args.width
inHeight = args.height

# Load the network
net = cv.dnn.readNetFromCaffe(args.proto, args.model)

# Read the input image
frame = cv.imread(args.input)
if frame is None:
    raise ValueError("Could not read the input image. Check the file path.")

frameWidth = frame.shape[1]
frameHeight = frame.shape[0]

# Prepare the input blob
inp = cv.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)
net.setInput(inp)

# Perform forward pass
start_t = time.time()
out = net.forward()
print("Inference time: ", time.time() - start_t)

# Create a window to display the result
window_name = "Human Pose Estimation"
cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

# Extract keypoints
points = []
for i in range(len(BODY_PARTS)):
    heatMap = out[0, i, :, :]
    _, conf, _, point = cv.minMaxLoc(heatMap)
    x = (frameWidth * point[0]) / out.shape[3]
    y = (frameHeight * point[1]) / out.shape[2]
    points.append((int(x), int(y)) if conf > args.thr else None)

# Draw the skeleton
for pair in POSE_PAIRS:
    partFrom = pair[0]
    partTo = pair[1]
    assert partFrom in BODY_PARTS
    assert partTo in BODY_PARTS

    idFrom = BODY_PARTS[partFrom]
    idTo = BODY_PARTS[partTo]
    if points[idFrom] and points[idTo]:
        cv.line(frame, points[idFrom], points[idTo], (255, 74, 0), 3)
        cv.ellipse(frame, points[idFrom], (4, 4), 0, 0, 360, (255, 255, 255), cv.FILLED)
        cv.ellipse(frame, points[idTo], (4, 4), 0, 0, 360, (255, 255, 255), cv.FILLED)
        cv.putText(frame, str(idFrom), points[idFrom], cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv.LINE_AA)
        cv.putText(frame, str(idTo), points[idTo], cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv.LINE_AA)

# Display inference time
t, _ = net.getPerfProfile()
freq = cv.getTickFrequency() / 1000
cv.putText(frame, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv.LINE_AA)

# Show and save the result
cv.imshow(window_name, frame)
cv.imwrite('result_' + args.input, frame)
cv.waitKey(0)
cv.destroyAllWindows()