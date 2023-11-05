import math
import random


class GameMath:
    @staticmethod
    def get_angle(first_pos, second_pos):
        h = second_pos[1] - first_pos[1]
        d = second_pos[0] - first_pos[0]
        if d == 0:
            d = 0.00001  # Avoid division by zero
        r = math.sqrt(d * d + h * h)
        angle = math.acos((d * d + r * r - h * h) / (2 * d * r))
        if h < 0:
            angle = 2 * math.pi - angle
        return angle

    @staticmethod
    def get_distance(first_pos, second_pos):
        h = second_pos[1] - first_pos[1]
        d = second_pos[0] - first_pos[0]
        return math.sqrt(d * d + h * h)

    @staticmethod
    def get_harmonic_motion(length, duration, current_time, initial_phase=0.5):
        return length * math.cos(math.pi / duration * current_time + math.pi * initial_phase)

    @staticmethod
    def get_moving_equation(first_pos, second_pos, duration, current_time):
        x = first_pos[0] + (second_pos[0] - first_pos[0]) * current_time / duration
        y = first_pos[1] + (second_pos[1] - first_pos[1]) * current_time / duration
        return [x, y]

    @staticmethod
    def rad_to_degree(angle):
        return angle * 180 / math.pi

    @staticmethod
    def degree_to_rad(angle):
        return angle * math.pi / 180

    @staticmethod
    def get_random(start, end):
        return random.randint(start, end)
