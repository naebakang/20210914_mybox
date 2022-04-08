# File encoding: UTF-8

import numpy


def get_bunch_min_max_coor(bunch_xywh):
    num, row, col = bunch_xywh.shape
    bunch_min_max = numpy.zeros((num, row, col), dtype=numpy.float32)
    for i in range(row):
        xywh = bunch_xywh[0, i, :]
        min_max_coor = get_min_max_coor_from_xywh(xywh=xywh)
        bunch_min_max[:, i, :] = min_max_coor

    return bunch_min_max


def get_min_max_coor_from_xywh(xywh):
    x_center = xywh[0]
    y_center = xywh[1]
    width = xywh[2]
    height = xywh[3]

    y_min = y_center - height/2
    x_min = x_center - width/2
    y_max = y_center + height/2
    x_max = x_center + width/2

    return numpy.array([y_min, x_min, y_max, x_max], dtype=numpy.float32)
