import cv2
import face_recognition
import time
import logging

# Setup logging to log action times and events
logging.basicConfig(filename='face_recognition_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Load the reference image and encode the face
img = cv2.imread(r'D:\New folder\images\face-2.jpg')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
face_encodings = face_recognition.face_encodings(rgb_img)

if len(face_encodings) > 0:
    img_encoded = face_encodings[0]  # Store the encoding of the reference image

# Initialize the video capture
video_capture = cv2.VideoCapture(r'D:\New folder\video\task-video.mp4')

# Get the frame rate of the video to calculate the timestamp
fps = video_capture.get(cv2.CAP_PROP_FPS)

# Start the frame processing
frame_count = 0  # Keep track of the frame number
matched_timestamps = []  # Store the timestamps where the face is detected

while True:
    # Capture frame-by-frame
    start_time = time.time()  # Log the start time for performance measurement
    ret, frame = video_capture.read()

    if not ret:
        break  # Exit the loop if there's an issue with the video stream

    # Increment frame count
    frame_count += 1

    # Convert the frame from BGR (OpenCV format) to RGB (face_recognition format)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces and record detection time
    detection_start_time = time.time()  # Start time for face detection
    face_frame_encodings = face_recognition.face_encodings(rgb_frame)
    face_locations = face_recognition.face_locations(rgb_frame)
    detection_end_time = time.time()  # End time for face detection

    # Log the time taken for face detection
    logging.info(f'Frame {frame_count}: Face detection time: {detection_end_time - detection_start_time:.4f} seconds')

    # Loop through the face encodings in the frame
    for face_encoding, (top, right, bottom, left) in zip(face_frame_encodings, face_locations):
        # Compare the face encoding from the frame with the reference image's encoding
        similarity_start_time = time.time()  # Start time for similarity check
        compare = face_recognition.compare_faces([img_encoded], face_encoding)
        similarity_end_time = time.time()  # End time for similarity check

        # Log the time taken for face comparison
        logging.info(f'Frame {frame_count}: Similarity check time: {similarity_end_time - similarity_start_time:.4f} seconds')

        if compare[0]:  # If a match is found
            # Draw a green rectangle around the matched face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            
            # Calculate the timestamp of the frame and save it
            timestamp = frame_count / fps
            matched_timestamps.append(timestamp)
            
            # Log the match and timestamp
            logging.info(f'Frame {frame_count}: Match found at timestamp {timestamp:.2f} seconds')

        else:
            # Draw a red rectangle around unmatched faces
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1):
        break

    # Log the overall processing time for the current frame
    end_time = time.time()
    logging.info(f'Frame {frame_count}: Total processing time: {end_time - start_time:.4f} seconds')

# Release the video capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()

# Save the timestamps of detected faces to a file
with open('detected_timestamps.txt', 'w') as f:
    for timestamp in matched_timestamps:
        f.write(f'Timestamp: {timestamp:.2f} seconds\n')

# Log the summary of detection
logging.info(f'Total number of frames processed: {frame_count}')
logging.info(f'Number of times the face was detected: {len(matched_timestamps)}')
