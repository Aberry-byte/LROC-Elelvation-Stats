import numpy as np
import re


def append_to_array_from_file_regex(file, regex):
    array = []
    with open(file) as file:
        for i, line in enumerate(file):
            for match in re.finditer(regex, line):
                # print(f'Found on line {i+1}: {match.group()}')
                match_line_list = MatchRegexLine(list(match.group()))
                line_data = [match_line_list.point_id(), match_line_list.lat(), match_line_list.long(),
                             round(match_line_list.elevation(1000), 5), match_line_list.point_id_num()]
                array.append(line_data)
                del match_line_list
                del line_data
    return array


def absolute_difference(value1, value2):
    return abs(round(value1 - value2, 5))


def array_elements_in_common(array_1, array_2, element_to_get):
    """Returns an array with the mean of the elements in common"""
    common = np.array([])
    for iteration in range(0, len(array_1)):
        for iteration_2 in range(0, len(array_2)):
            if str(array_1[iteration][4]) == str(array_2[iteration_2][4]):
                mean = (array_1[iteration][element_to_get] + array_2[iteration_2][element_to_get]) / 2
                common = np.append(common , mean)
    return common


def dtm_array_differences_stats(array_1, array_2, element_to_get):
    """Returns an array of the absolute differences between two arrays and a specific element"""
    differences = np.array([])
    for iteration in range(0, len(array_1)):
        for iteration_2 in range(0, len(array_2)):
            if str(array_1[iteration][4]) == str(array_2[iteration_2][4]):
                differences = np.append(differences , absolute_difference(array_1[iteration][element_to_get], array_2[iteration_2][element_to_get]))
    return differences


def percent_difference(value1, value2):
    """Returns the percent difference between two numbers"""
    return round((((abs(value1 - value2)) / ((value1 + value2) / 2)) * 100), 5)


def file_writer(array1, array2, array_name1, array_name2, output_file):
    """Expected inputs are two numpy array to get statistics from and the names of each array and the file to write to"""
    output_file.write(f"{str(array_name1)} by {str(array_name2)}\n")

    output_file.write("Lat\n")
    array1_by_array2_lat = dtm_array_differences_stats(array1, array2, 1)
    output_file.write(f"\tPoint to point    : {array1_by_array2_lat.ptp()}\n")
    output_file.write(f"\tMean              : {array1_by_array2_lat.mean()}\n")
    output_file.write(f"\tStandard Deviation: {array1_by_array2_lat.std()}\n")

    output_file.write("Long\n")
    array1_by_array2_long = dtm_array_differences_stats(array1, array2, 2)
    output_file.write(f"\tPoint to point    : {array1_by_array2_long.ptp()}\n")
    output_file.write(f"\tMean              : {array1_by_array2_long.mean()}\n")
    output_file.write(f"\tStandard Deviation: {array1_by_array2_long.std()}\n")

    output_file.write("Elevation\n")
    array1_by_array2_elevation = dtm_array_differences_stats(array1, array2, 3)
    output_file.write(f"\tPoint to point    : {array1_by_array2_elevation.ptp()}\n")
    output_file.write(f"\tMean              : {array1_by_array2_elevation.mean()}\n")
    output_file.write(f"\tStandard Deviation: {array1_by_array2_elevation.std()}\n")

    output_file.write("\n\n")

    # clean up memory usage
    del array1_by_array2_lat
    del array1_by_array2_long
    del array1_by_array2_elevation


class MatchRegexLine:
    def __init__(self, matchlist_):
        self.__matchlist = matchlist_

    def point_id(self):
        """Returns the point ID also know as the Label from bundleout file"""
        point_ID = ''
        point_list_position = 0
        point_list_position_max = 9
        while point_list_position <= point_list_position_max:
            point_ID = point_ID + str(self.__matchlist[point_list_position])
            point_list_position += 1
        return str(point_ID)

    def point_id_num(self):
        """Returns the point ID final 4 numbers from bundleout file"""
        point_ID_num = ''
        point_list_position = 5
        point_list_position_max = 9
        while point_list_position <= point_list_position_max:
            point_ID_num = point_ID_num + str(self.__matchlist[point_list_position])
            point_list_position += 1
        return str(point_ID_num)

    def lat(self):
        """Returns the latitude of control point from given list from bundleout file"""
        lat = ''
        lat_list_position = 46
        lat_list_position_max = 56
        while lat_list_position <= lat_list_position_max:
            lat = lat + str(self.__matchlist[lat_list_position])
            lat_list_position += 1
        return float(lat)

    def long(self):
        """Returns the longitude of control point from given list from bundleout file"""
        long = ''
        long_list_position = 62
        long_list_position_max = 73
        while long_list_position <= long_list_position_max:
            long = long + str(self.__matchlist[long_list_position])
            long_list_position += 1
        return float(long)

    def elevation(self, multiplier=1):
        """Returns the elevation of control point from given list from bundleout file;
        :param multiplier: multiply your elevation data by any value to get your desired result"""
        elev = ''
        elev_list_position = 76
        elev_list_position_max = 88
        while elev_list_position <= elev_list_position_max:
            elev = elev + str(self.__matchlist[elev_list_position])
            elev_list_position += 1
        return (float(elev) * multiplier)