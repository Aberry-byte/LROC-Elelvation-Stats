import re
import numpy as np
import argparse
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import elevation_stats_functions as esf


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process three bundleout txt files for statistics')
    parser.add_argument('DTM', type=str, metavar='DTM',
                        help="Bundleout txt file from being run with a dtm and ground points EX:ground_DTM_bundleout.txt")
    parser.add_argument('noDTM', type=str, metavar='noDTM',
                        help="Bundleout txt file from being run without a dtm but ground points EX:ground_noDTM_bundleout.txt")
    parser.add_argument('no_ground_noDTM', type=str, metavar='no_ground_noDTM',
                        help="Bundleout txt file from being run without a dtm or ground points EX:No_ground_No_DTM_bundleout.txt")
    args = parser.parse_args()
    DTM_file = args.DTM
    noDTM_file = args.noDTM
    no_ground_noDTM_file = args.no_ground_noDTM

    control_point_regex = re.compile(r'[A-Za-z_]*_\d*\s*FREE.*', re.I)
    log_file = open("log.txt", 'w')

    DTM_point_array = esf.append_to_array_from_file_regex(DTM_file, control_point_regex)

    noDTM_point_array = esf.append_to_array_from_file_regex(noDTM_file, control_point_regex)

    no_ground_noDTM_array = esf.append_to_array_from_file_regex(no_ground_noDTM_file, control_point_regex)

    print(f"noDTM_point_array is {len(noDTM_point_array)} long")
    print(f"DTM_point_array is {len(DTM_point_array)} long")
    print(f"no_ground_noDTM_array is {len(no_ground_noDTM_array)} long")

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

    no_X_no_DTM = np.array([])
    no_Y_no_DTM = np.array([])
    no_Z_no_DTM = np.array([])
    for lists in no_ground_noDTM_array:
        X_ = lists[1]
        Y_ = lists[2]
        Z_ = lists[3]
        no_X_no_DTM = np.append(no_X_no_DTM, float(X_))
        no_Y_no_DTM = np.append(no_Y_no_DTM, float(Y_))
        no_Z_no_DTM = np.append(no_Z_no_DTM, float(Z_))


    # plot it out
    ax.scatter(X_DTM, Y_DTM, Z_DTM, label="DTM", c='blue', s=3)
    ax.scatter(X_no_DTM, Y_no_DTM, Z_no_DTM, label="no DTM", c='green', s=3)
    ax.scatter(no_X_no_DTM, no_Y_no_DTM, no_Z_no_DTM, label="no ground no DTM", c='red', s=3)
    ax.set_xlabel("Latitude")
    ax.set_ylabel("Longitude")
    ax.set_zlabel("Elevation (m)")
    ax.legend()

    plt.show()

    # print out data
    print("Writing to file")
    # DTM by no DTM
    esf.file_writer(DTM_point_array, noDTM_point_array, "DTM", "no DTM", log_file)
    DTM_by_noDTM_elevation = esf.dtm_array_differences_stats(DTM_point_array, noDTM_point_array, 3)


    # DTM by noDTM_no_ground
    esf.file_writer(DTM_point_array, no_ground_noDTM_array, "DTM", "no DTM and no ground", log_file)
    DTM_by_noDTM_no_ground_elevation = esf.dtm_array_differences_stats(DTM_point_array, no_ground_noDTM_array, 3)


    # noDTM by noDTM_no_ground
    esf.file_writer(noDTM_point_array, no_ground_noDTM_array, "no DTM", "no DTM and no ground", log_file)
    noDTM_by_noDTM_no_ground_elevation = esf.dtm_array_differences_stats(noDTM_point_array, no_ground_noDTM_array, 3)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X_DTM_no_ground_no_DTM = esf.array_elements_in_common(DTM_point_array, no_ground_noDTM_array, 1)
    Y_DTM_no_ground_no_DTM = esf.array_elements_in_common(DTM_point_array, no_ground_noDTM_array, 2)

    X_DTM_noDTM = esf.array_elements_in_common(DTM_point_array, noDTM_point_array, 1)
    Y_DTM_noDTM = esf.array_elements_in_common(DTM_point_array, noDTM_point_array, 2)

    ax.scatter(X_DTM_no_ground_no_DTM, Y_DTM_no_ground_no_DTM, DTM_by_noDTM_no_ground_elevation, label="DTM - no ground no DTM", c='blue', s=2)
    ax.scatter(X_DTM_noDTM, Y_DTM_noDTM, DTM_by_noDTM_elevation, label="DTM - no DTM", c='red', s=2)
    ax.set_xlabel("Latitude")
    ax.set_ylabel("Longitude")
    ax.set_zlabel("Elevation difference (m)")
    ax.legend()

    plt.show()