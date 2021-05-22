import cv2, time, os
from os import path

def createImages():
    cam = cv2.VideoCapture(0)

    if not path.exists('./images'):
        os.mkdir('./images')

    if not path.exists('./images/rgb'):
        os.mkdir('./images/rgb')

    if not path.exists('./images/jpeg'):
        os.mkdir('./images/jpeg')

    if not path.exists('./images/gray'):
        os.mkdir('./images/gray')

    img_counter = 0

    for i in range(0, 10):
        ret, frame = cam.read()

        # problem with camera
        if not ret:
            print("no frame here :(")
            break

        # show frame
        cv2.imshow("test", frame)

        # colors
        rgb = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # enter key
        k = cv2.waitKey(1)

        # close window
        if k%256 == 27:
            break

        rgb_img_name = "rgb_{}.bmp".format(img_counter)
        cv2.imwrite("./images/rgb/{}".format(rgb_img_name), rgb)

        jpeg_img_name = "jpeg_{}.jpeg".format(img_counter)
        cv2.imwrite("./images/jpeg/{}".format(jpeg_img_name), rgb)

        gray_img_name = "gray_{}.png".format(img_counter)
        cv2.imwrite("./images/gray/{}".format(gray_img_name), gray)

        img_counter += 1

        # delay before next take images
        time.sleep(1)

    cam.release()

    cv2.destroyAllWindows()