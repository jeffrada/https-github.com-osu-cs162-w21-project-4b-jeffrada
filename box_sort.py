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
    vol_list = []
    for box in box_list:
        vol_list.append(box.volume())
    print(vol_list)
    """
    Sorts vol_list in ascending order
    """
    for index in range(1, len(vol_list)):
        value = vol_list[index]
        pos = index - 1
        while pos >= 0 and vol_list[pos] > value:
            vol_list[pos + 1] = vol_list[pos]
            pos -= 1
        vol_list[pos + 1] = value
    print(vol_list)
    sorted_box_list = []
    for volume in vol_list:
        for box in box_list:
            if box.volume() == volume:
                sorted_box_list.append(box)
    return sorted_box_list

# Below is testing code
b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)
box_list = [b1, b2, b3]
box_sort(box_list)
