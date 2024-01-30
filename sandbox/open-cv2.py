import cv2
import numpy as np

# image = cv2.imread('screenshot.png')
image = cv2.imread('canvas3.png')
# Преобразование изображения в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Создание маски по белому цвету
# mask = cv2.inRange(image, (255, 255, 255), (255, 255, 255))
# создание маски
mask = cv2.inRange(image, (0, 200, 0), (255, 255, 255))
# удаление шумов
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((1, 1), np.uint8))



# Нахождение контуров в маске
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)

# # выведем на екран все контуры
# cv2.imshow('Result', mask)
cv2.waitKey(0)

# Обводим все белые контуры
cv2.drawContours(image, contours, -1, (0, 75, 255), 2)

# Вывод координат контуров текстом
for contour in contours:
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        print(f"Координаты центра контура: ({cX}, {cY})")
        # печать всех координат
        print(f"Координаты контура: {contour}")

#
# Нахождение самого большого элемента
max_contour = max(contours, key=cv2.contourArea)
# Поиск второго по величине элемента из tuple
max_contour = sorted(contours, key=cv2.contourArea)[-2]
M = cv2.moments(max_contour)
if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print(f"Координаты !!!! центра контура: ({cX}, {cY})")


# max_contour = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(max_contour)
print(f"Координаты самого большого элемента: ({x}, {y}, {w}, {h})")

# Вывод графического представления самого большого элемента
cv2.drawContours(image, [max_contour], -1, (0, 255, 0), 2)
# cv2.drawContours(mask, [max_contour], -1, (0, 255, 0), 2)

cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Вывод изображения с контурами и прямоугольником
cv2.imshow('Result', image)
# cv2.imshow('Result', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
