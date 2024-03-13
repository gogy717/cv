import cv2
from cv2 import VideoCapture
def capture_from_webcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to the HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for the RGB color you want to recognize
        lower_rgb = (155, 210, 180)  # Replace with the lower RGB values
        upper_rgb = (179, 255, 255)  # Replace with the upper RGB values

        # Create a mask based on the RGB color range
        mask = cv2.inRange(hsv_frame, lower_rgb, upper_rgb)

        # Calculate the moments of the mask
        M = cv2.moments(mask)

        # Using moments to calculate the centroid (center point) coordinates
        # Note to prevent division by zero
        if M["m00"] != 0:
            centerX = int(M["m10"] / M["m00"])
            centerY = int(M["m01"] / M["m00"])
            print(centerX, centerY)
            cv2.circle(frame, (centerX, centerY), 5, (0, 255, 0), -1)
        else:
            centerX, centerY = -1, -1  # Or any other default value that indicates failure or absence
            print("No centroid found due to zero division.")


        # Apply the mask to the original frame
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Display the result
        cv2.imshow('RGB Recognition', result)

        # Check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to capture from webcam
capture_from_webcam()




# def main():
#     # Load the RGB image
#     image = cv2.imread('colors.png', cv2.IMREAD_COLOR)

#     # Convert the image to the HSV color space
#     hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#     # Define the lower and upper bounds for the RGB color you want to recognize
#     lower_rgb = (0, 0, 0)  # Replace with the lower RGB values
#     upper_rgb = (255, 255, 255)  # Replace with the upper RGB values

#     # Create a mask based on the RGB color range
#     mask = cv2.inRange(hsv_image, lower_rgb, upper_rgb)

#     # Apply the mask to the original image
#     result = cv2.bitwise_and(image, image, mask=mask)

#     # Display the result
#     cv2.imshow('RGB Recognition', result)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# if __name__ == '__main__':
#     main()