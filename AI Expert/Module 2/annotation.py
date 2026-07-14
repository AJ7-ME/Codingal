import cv2 
import matplotlib.pyplot as plt
image_path = 'example.png'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, _ = image_rgb.shape

#Step 2: draw 2 rectangles on the image
#Rectangle 1
rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3) #Yellow

#Rectangle 2
rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20) #20 pixel padding
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255), 3) #Magenta
#Step 3: Draw Circles at the centers of both circles
center1x = top_left1[0] + rect1_width // 2
center1y = top_left1[1] + rect1_height // 2
center2x = top_left2[0] + rect2_width // 2
center2y = top_left2[1] + rect2_height // 2
cv2.circle(image_rgb, (center1x, center1y), 15 , (0, 255, 0), -1) # Green
cv2.circle(image_rgb, (center2x, center2y), 15 , (255, 0, 0), -1) # Red

#Step 4: Display the image with rectangles and circles
cv2.line(image_rgb, (center1x, center1y), (center2x, center2y), (0, 255, 0), 3)

#Step 5
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Region 1', (top_left1[0], top_left1[1] - 10), font, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region 2', (top_left2[0], top_left2[1] - 10), font, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 1', (center1x - 20, center1y - 10), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 2', (center2x - 20, center2y - 10), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

#6
arrow_start = (width - 50, 20) 
arrow_end = (width - 50, height - 20)

#Both directions
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)

#7 Height
heighta = (arrow_start[0] - 150, (arrow_start[1] + arrow_end[1]) // 2)
cv2.putText(image_rgb, f'Height:, {height}px', heighta, font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)
#8 display
plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title('Annotated Image with Rectangles, Circles, and Arrows')
plt.axis('off')
plt.show()