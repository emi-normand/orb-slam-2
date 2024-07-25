import cv2

def feature_extractor(image):

    # Initialize the ORB detector
    orb = cv2.ORB_create()

    # Find keypoints and descriptors
    keypoints, descriptors = orb.detectAndCompute(image, None)
    return keypoints,descriptors
    

