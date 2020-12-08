import re
import numpy as np
import argparse
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import elevation_stats_functions as esf


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process two bundleout txt files for statistics')
    parser.add_argument('DTM', type=str, metavar='DTM',
                        help="Bundleout txt file from being run with a dtm and ground points EX:ground_DTM_bundleout.txt")
    parser.add_argument('noDTM', type=str, metavar='noDTM',
                        help="Bundleout txt file from being run anyway chosen EX:No_ground_noDTM_bundleout.txt")
    args = parser.parse_args()
    DTM_file = args.DTM
    noDTM_file = args.noDTM

    control_point_regex = re.compile(r'[A-Za-z_]*_\d*\s*FREE.*', re.I)
    log_file = open("log_2file.txt", 'w')

    DTM_point_array = esf.append_to_array_from_file_regex(DTM_file, control_point_regex)

    noDTM_point_array = esf.append_to_array_from_file_regex(noDTM_file, control_point_regex)


    print(f"DTM_point_array is {len(DTM_point_array)} long")
    print(f"noDTM_point_array is {len(noDTM_point_array)} long")


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    print("Getting X,Y,Z values")
    # Get x, y, z values for each array
    X_no_DTM = np.array([])
    Y_no_DTM = np.array([])
    Z_no_DTM = np.array([])
    for lists in noDTM_point_array:
        X_ = lists[1]
        Y_ = lists[2]
        Z_ = lists[3]
        X_no_DTM = np.append(X_no_DTM, float(X_))
        Y_no_DTM = np.append(Y_no_DTM, float(Y_))
        Z_no_DTM = np.append(Z_no_DTM, float(Z_))

    X_DTM = np.array([])
    Y_DTM = np.array([])
    Z_DTM = np.array([])
    for lists in DTM_point_array:
        X_ = lists[1]
        Y_ = lists[2]
        Z_ = lists[3]
        X_DTM = np.append(X_DTM, float(X_))
        Y_DTM = np.append(Y_DTM, float(Y_))
        Z_DTM = np.append(Z_DTM, float(Z_))


    # plot it out
    ax.scatter(X_DTM, Y_DTM, Z_DTM, label="DTM", c='blue', s=3)
    ax.scatter(X_no_DTM, Y_no_DTM, Z_no_DTM, label="no DTM", c='red', s=3)
    ax.set_xlabel("Latitude")
    ax.set_ylabel("Longitude")
    ax.set_zlabel("Elevation (m)")
    ax.legend()

    plt.show()

    # print out data
    print("Writing to file")
    # DTM by no DTM
    esf.file_writer(DTM_point_array, noDTM_point_array, "DTM", "no DTM", log_file)
    DTM_by_noDTM_elevation = esf.array_element_differences(DTM_point_array, noDTM_point_array, 3)


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X_DTM_noDTM = esf.array_elements_in_common(DTM_point_array, noDTM_point_array, 1)
    Y_DTM_noDTM = esf.array_elements_in_common(DTM_point_array, noDTM_point_array, 2)

    ax.scatter(X_DTM_noDTM, Y_DTM_noDTM, DTM_by_noDTM_elevation, label="DTM - no DTM", c='red', s=2)
    ax.set_xlabel("Latitude")
    ax.set_ylabel("Longitude")
    ax.set_zlabel("Elevation difference (m)")
    ax.legend()

    plt.show()
