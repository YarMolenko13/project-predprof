from math import sqrt, hypot
from os import listdir

import numpy as np


def density(wheats, heights):
    p1 = []
    for i in range(len(wheats)):
        length = 2 * (heights[i] - 1.05) * np.tan(np.pi / 3)
        width = 2 * (heights[i] - 1.05) * np.tan(np.pi * 3.5 / 18)
        s = length * width

        p1.append(wheats[i] / s)

    average_density = sum(p1) / len(wheats)

    return average_density


"""
returns (densities, squares, total_wheats)
"""


def get_results(dirname_input: str, dirname_output: str):
    files_dir = listdir(dirname_output)

    densities = []
    squares = []
    total_wheats = []


    fields_num = int(sorted(files_dir, key=lambda x: int(x.split("_")[1]))[-1].split("_")[-2])
    for field in range(1, fields_num + 1):
        files_dir = listdir(dirname_output)

        wheats = []
        heights = []
        files = sorted(files, key=lambda x: int(x.split("_")[-1].replace(".txt", "")))

        for file_name in list(filter(lambda x: "BndBox" in x, files)):
            if int(file_name.split("_")[-2]) == field:
                with open(dirname_output + file_name) as f:
                    wheats.append(len(f.readline().split("\n")))
                f.close()

        files_dir = listdir(dirname_input)
        files = list(filter(lambda x: "Foto" in x, files_dir))
        files = sorted(files, key=lambda x: int(x.split("_")[-4]))

        for file_name in list(filter(lambda x: "Foto" in x and ".png" in x, files)):
            if ".png" in file_name and int(file_name.split("_")[-5]) == field:
                heights.append(int(file_name[-7:-4]))

        heights = [i / 100 for i in heights]

        densities.append(density(wheats, heights))

    def _hypot(x1, x2):
        return hypot(x2[0] - x1[0], x2[1] - x1[1])

    def parea(x1, x2, x3):
        y1, y2, y3 = _hypot(x1, x2), _hypot(x2, x3), _hypot(x1, x3)
        z = (y1 + y2 + y3) / 2
        return sqrt(z * (z - y1) * (z - y2) * (z - y3))

    fields = listdir(dirname_input)
    fields = list(filter(lambda x: "Field" in x, fields))
    fields.sort(key=lambda x: int(x.replace("Field", "").split(".")[0]))
    for file_name in fields:
        f = open(dirname_input + file_name)
        line = f.readline()
        point_list = []
        point = []
        index = 0
        is_point = False

        for s in line:
            if s == "(":
                point = []
                point.append(0)
                index = 0
                is_point = True
                continue
            if is_point and s == ",":
                index = 1
                point.append(0)
                continue
            if s == ")":
                is_point = False
                point_list.append(tuple(point))
                continue
            if s.isnumeric():
                point[index] *= 10
                point[index] += int(s)
                continue

        result = 0
        for x, y in zip(point_list[1:], point_list[2:]):
            result += parea(point_list[0], x, y)
        index = int(file_name.replace("Field", "").split(".")[0]) - 1
        squares.append(round(result, 1))
        total_wheats.append(result * densities[index])

    # for i in range(len(densities)):
    #     print(squares[i], densities[i], total_wheats[i])

    return densities, squares, total_wheats
