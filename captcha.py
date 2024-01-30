from PIL import Image, ImageEnhance
import cv2
import numpy as np


def get_rectangle(path):
    image = Image.open(path)
    scale_value = 2
    image = ImageEnhance.Contrast(image).enhance(scale_value)
    image = image.crop((
        50, 0,
        image.width, image.height
    ))

    image = np.array(image)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
    mid = np.mean(image)
    _, thresh = cv2.threshold(
        image, mid // 2.2, mid,
        cv2.THRESH_BINARY_INV
    )
    thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # перебираем все найденные контуры в цикле
    for cnt in sorted(contours, key=lambda x: x[0][0][0]):
        rect = cv2.minAreaRect(cnt)  # пытаемся вписать прямоугольник
        box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int8(box)  # округление координат
        area = int(rect[1][0] * rect[1][1])  # вычисление площади
        angle = rect[-1]
        ratio = max(rect[1][1], rect[1][0]) / min(rect[1][1], rect[1][0]) if area else 0
        if (400 < area < 10000) and (-5 < angle < 5 or 85 < angle < 95) and ratio < 1.5:
            cv2.drawContours(image, [box], 0, (255, 0, 0), 2)  # рисуем прямоугольник
            cv2.imshow('image', image)  # вывод обработанного кадра в окно
            cv2.imshow('thresh', thresh)
            cv2.waitKey(1)
            input()
            cv2.destroyAllWindows()
            return box[0][0] + 50
    return None


if __name__ == '__main__':
    x = get_rectangle('Screenshot_3.jpg')
    print(x)
    exit()
# for i in range(1, 13):
#     x = get_rectangle(f'images\\{i}.png')