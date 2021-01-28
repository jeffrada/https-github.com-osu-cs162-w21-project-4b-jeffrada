# Author: Adam Jeffries
# Date: 1/27/2021
# Description: A class named Box which takes 3 data members and finds the volume of the box then sorts
# a list of the volumes from greatest volume to least.

class Box:
    """
    Represents a list of boxes that have a given volume calculated using length, width and height.
    """

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        return self._length * self._width * self._height

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height


def box_sort(box_list):
    """
  Sorts box_list in descending order
    """
    for index in range(1, len(box_list)):
        box = box_list[index]
        box_volume = box.volume()
        pos = index - 1
        while pos >= 0 and box_list[pos].volume() > box_volume:
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = box
    box_list.reverse()
