import asyncio
import websockets
import serial
import sqlite3
import cv2


def capture_frame_on_click(event, x, y, flags, param):
    global collected_images
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.imwrite(f"pic {collected_images}" + ".jpg", param)
        print("Screenshot taken")
        print(f"Left button clicked at x: {x}px, y: {y}px")
        collected_images += 1
        current_pic = f"current_pic_{collected_images}"
        if current_pic not in images_dict.keys():
            images_dict[current_pic] = []
        images_dict[current_pic] = [x, y]


async def printing_dictionary(im_dict):
    last_count = 0
    while True:
        current_count = len(im_dict)
        if current_count > last_count:
            print(f"Updated dictionary" + "\n" + im_dict)
            last_count = current_count
        await asyncio.sleep(1)


images_dict = {}
printing_dict_object = printing_dictionary(images_dict)
asyncio.run(printing_dict_object)

# taking pic from WebCam
camera = cv2.VideoCapture(0)
collected_images = 0

while True:
    success, frame = camera.read()
    if not success:
        print("Failed to grab frame")
        break
    # camera windows is labeled "test"
    cv2.imshow("test", frame)
    # waitKey(1) -> continuous video stream, waitKey(0) -> for a second
    key = cv2.waitKey(1)
    # if "esc" -> exit
    if key % 256 == 27:
        print('escape pressed, closing the app')
        break
    cv2.setMouseCallback("test", capture_frame_on_click, frame)

camera.release()

# # mouse detection and movement
# screen_width, screen_height = pyautogui.size()
# mouse_current_position = pyautogui.position()
# mouse_position_x, mouse_position_y = mouse_current_position
# print(f"x: {mouse_position_x}px")
# print(f"y: {mouse_position_y}px")
