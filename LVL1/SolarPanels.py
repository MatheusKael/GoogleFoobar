import math


def solution(area):
    total_area = area
    square_root = math.sqrt(area)
    solar_panels = []
    biggest_area = 0

    if(square_root % 1 == 0):
        solar_panels.append(int(math.sqrt(total_area))
                            * int(math.sqrt(total_area)))

        return solar_panels
    else:
        while(total_area > 0):
            biggest_area = int(square_root) * \
                int(square_root)

            total_area = total_area - biggest_area
            solar_panels.append(biggest_area)
            biggest_area = 0

        return solar_panels
