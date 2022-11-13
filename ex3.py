# pillow使うやつ
import cv2
from PIL import Image

original_face_image = "images/face_img.png"
original_eye_image = "images/eye_img.png"


def find_eye(original_face_image):
    cascade_file = "haarcascade_eye.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    img = cv2.imread(original_face_image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eye_list = cascade.detectMultiScale(img_gray)

    return eye_list


def paste_img(eye_list):
    r_x = eye_list[2][0]  # X座標
    r_y = eye_list[2][1]  # Y座標
    r_w = eye_list[2][2]  # 横幅
    r_h = eye_list[2][3]  # 縦幅
    print(r_x, r_y, r_w, r_h)

    l_x = eye_list[1][0]  # X座標
    l_y = eye_list[1][1]  # Y座標
    l_w = eye_list[1][2]  # 横幅
    l_h = eye_list[1][3]  # 縦幅
    print(l_x, l_y, l_w, l_h)

    face_img = Image.open(original_face_image)
    eye_img = Image.open(original_eye_image)

    new_r_eye_img = eye_img.resize((r_w, r_h))
    new_l_eye_img = eye_img.resize((l_w, l_h))
    new_r_eye_img.save("images/resized_r_eye_img.png")
    new_l_eye_img.save("images/resized_l_eye_img.png")

    face_img.paste(new_r_eye_img, (r_x, r_y), new_r_eye_img.split()[3])
    face_img.paste(new_l_eye_img, (l_x, l_y), new_l_eye_img.split()[3])

    face_img.save("images/pasted_face_img.png")


def show_img(face_img):
    cv2.imshow("face", face_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


eye_list = find_eye(original_face_image)
paste_img(eye_list)
face_img = cv2.imread("images/pasted_face_img.png")
show_img(face_img)
