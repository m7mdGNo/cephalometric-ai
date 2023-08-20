import cv2
import math


def get_middle(x1, y1, w, h):
    newx = (2 * x1 + w) / 2
    newy = (2 * y1 + h) / 2
    return [int(newx), int(newy)]

def draw_circle(img,center,color):
    cv2.circle(img, (center[0], center[1]), 5, color, -1)
    cv2.circle(img, (center[0], center[1]), 5, (0, 0, 0), 2)
    return img

def get_distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def calculate_angle(line1, line2):
    # Calculate the direction vectors of the lines
    direction_vector1 = [line1[1][0] - line1[0][0], line1[1][1] - line1[0][1]]
    direction_vector2 = [line2[1][0] - line2[0][0], line2[1][1] - line2[0][1]]

    # Calculate the dot product of the direction vectors
    dot_product = direction_vector1[0] * direction_vector2[0] + direction_vector1[1] * direction_vector2[1]

    # Calculate the magnitudes of the direction vectors
    magnitude1 = math.sqrt(direction_vector1[0] ** 2 + direction_vector1[1] ** 2)
    magnitude2 = math.sqrt(direction_vector2[0] ** 2 + direction_vector2[1] ** 2)

    # Calculate the cosine of the angle between the lines
    cosine_angle = dot_product / (magnitude1 * magnitude2)

    # Calculate the angle in radians
    angle_radians = math.acos(cosine_angle)

    # Convert the angle to degrees
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees
