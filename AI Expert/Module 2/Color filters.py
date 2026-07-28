import cv2
def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image"""
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Zero out the green channel
        filtered_image[:, :, 0] = 0  # Zero out the blue channel
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Zero out the red channel
        filtered_image[:, :, 2] = 0  # Zero out the blue channel
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Zero out the red channel
        filtered_image[:, :, 2] = 0  # Zero out the green channel
    elif filter_type == "Increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)  # Increase red channel
    elif filter_type == "Increase_green":
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], 50)  # Increase green channel
    elif filter_type == "Increase_blue":
        filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], 50)  # Increase blue channel
    elif filter_type == "Decrease_red":
        filtered_image[:, :, 2] = cv2.subtract(filtered_image[:, :, 2], 50)  # Decrease red channel
    elif filter_type == "Decrease_green":
        filtered_image[:, :, 1] = cv2.subtract(filtered_image[:, :, 1], 50)  # Decrease green channel
    elif filter_type == "Decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)  # Decrease blue channel
    return filtered_image
# Load the image
image_path = "example.png"
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not load image.")
else: 
    filter_type = "original"

    print("The following keys are your keybinds:")
#Red
    print(" Q: Red Tint")
    print(" W: Increase Red")
    print(" E: Decrease Red\n")

#Green
    print(" R: Green Tint")
    print(" T: Increase Green")
    print(" Y: Decrease Green\n")

#Blue
    print(" U: Blue Tint")
    print(" I: Increase Blue")
    print(" O: Decrease Blue\n")
    print(" ESC: Exit\n")

    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.namedWindow('Filtered Image', cv2.WINDOW_NORMAL)

        cv2.resizeWindow("Filtered Image", 800, 500)
        cv2.imshow("Filtered Image", filtered_image)
        #Wait for key press
        key = cv2.waitKey(0) & 0xFF
        # map Key presses to filters
        if key == ord('q'):
            filter_type = "red_tint"
        elif key == ord('w'):
            filter_type = "Increase_red"
        elif key == ord('e'):
            filter_type = "Decrease_red"
        elif key == ord('r'):
            filter_type = "green_tint"
        elif key == ord('t'):
            filter_type = "Increase_green"
        elif key == ord('y'):
            filter_type = "Decrease_green"
        elif key == ord('u'):
            filter_type = "blue_tint"
        elif key == ord('i'):
            filter_type = "Increase_blue"
        elif key == ord('o'):
            filter_type = "Decrease_blue"
        elif key == 27:  # ESC key to exit
            break
        else:
            print("Invalid Key! Please use one of the following 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o' or 'ESC' to exit.")

cv2.destroyAllWindows()