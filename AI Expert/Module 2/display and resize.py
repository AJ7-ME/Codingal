import cv2

image = cv2.imread('Example.png')

cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)  # Create a resizable window

cv2.resizeWindow('Loaded Image', 800, 500)  # Set the window size to 800x500 (width x height)


# Display the image in the resized window

cv2.imshow('Loaded Image', image)

cv2.waitKey(0)  # Wait for a key press

cv2.destroyAllWindows()  # Close the window
print(f"Image dimensions: {image.shape}")  # Print the dimensions of the image (height, width, channels)