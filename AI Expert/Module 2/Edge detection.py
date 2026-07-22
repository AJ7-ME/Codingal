import cv2 
import numpy as np
import matplotlib.pyplot as plt
def display_image(title, image):
    """Utility function to display an image using matplotlib."""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    """Interactive activity for edge prot detection and filtering."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("OG Gray img", gray_image)
    
    print ("Select an edge detection method:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Edge Detection")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            # Sobel Edge Detection
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
            combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
            display_image("Sobel Edge Detection", combined_sobel)

        elif choice == '2':
            # Canny Edge Detection
            print("Enter lower and upper thresholds for Canny Edge Detection (e.g., 100 200):")
            lower_thresh = int(input("Lower threshold: "))
            upper_thresh = int(input("Upper threshold: "))
            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display_image("Canny Edge Detection", edges)

        elif choice == '3':
            # Laplacian Edge Detection
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", laplacian.astype(np.uint8))

        elif choice == '4':
            # Gaussian Edge Detection
            print("Enter kernel size for Gaussian Blur (odd integer, e.g., 5):")
            kernel_size = int(input("Kernel size: "))
            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
            display_image("Gaussian Blur", blurred)

        elif choice == '5':
            # Median Filtering
            print("Enter kernel size for Median Filtering (odd integer, e.g., 5):")
            kernel_size = int(input("Kernel size: "))
            median_filtered = cv2.medianBlur(image, kernel_size)
            display_image("Median Filtering", median_filtered)

        elif choice == '6':
            #Exit
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option (1-6).")
#provide the path to an image for the activity
interactive_edge_detection('Example.png')