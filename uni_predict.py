from PIL import Image
from yolo import YOLO

if __name__ == "__main__":
    mode = "predict"
    crop = True
    count = False
    yolo = YOLO()
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.uni_detect_image(image, crop=crop, count=count)
            r_image.show()
