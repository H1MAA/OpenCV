import cv2
import numpy as np

circ, rect = 0, 0

# def getShape(length):
#     # if len(approx) == 4:
#     #     x1, y1, w, h = cv2.boundingRect(approx)
#     #     aspectRatio = float(w) / h
#     #     if 0.95 <= aspectRatio <= 1.05:
#     #         return "Square"
#     #     else:
#     #         return "Rectangle"
#     # else:
#     if len(approx) > 4:
#         return int(len(approx))

sum1 = 0

for i in range(100):
    img = cv2.imread(f"lagoris/lagori_0{i:02d}.jpg")
    canny = cv2.Canny(cv2.GaussianBlur(img, (5, 5), 1), 50, 170)
    cv2.imshow("C", canny)

    # find all contours
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
    #     # to filter the small rectangles
    #     if cv2.contourArea(contour) > 1000:
            approx = cv2.approxPolyDP(contour, 4, True)
            # cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5

            x1, y1, w, h = cv2.boundingRect(contour)
            # cv2.rectangle(img, (center_x, center_y), (x1 + w, y1 + h), (0, 255, 0), 2)
            # cv2.imshow('cutted contour', img[y1:y1 + h, x1:x1 + w])
            # print('Average color (BGR): ', np.array(cv2.mean(img[y1:y1 + h, x1:x1 + w])).astype(np.uint8))
            length = len(approx)
    #
    #         # shape = getShape(length)
    #         # print(type(length))
    #
    #         sum1 += length
    #
    #         j = cv2.cvtColor(img[y1:y1 + h, x1:x1 + w], cv2.COLOR_BGR2HSV)
    #         if length > 34:
    #             cv2.putText(img, str(length), (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255))
    #             cv2.imshow(f"{i}", cv2.Canny(cv2.GaussianBlur(img, (5, 5), 1), 80, 80))
    #             cv2.waitKey(0)
    # cv2.imshow(f"{i}", img)
    # cv2.imshow("FFS", canny)
    cv2.waitKey(0)

print(sum1/100)