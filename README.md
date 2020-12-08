# LROC-Elelvation-Stats
This project is about visualizing the differences in LROC mosiac control methods and returing some basic statics of the differences

You will need bundleout text files from mosaics to run this script. If you do you can either run it between two or three files by using the appropriate script

# Basic Backround 

no ground no DTM is the least accurate 
no DTM is moderatly accurate 
DTM is the highest accuracy 

This script will then graph all the measure points from each type out giving a visual of what the mosaic looks like. 
Then it will find various statistical differces between the images.
Then it will plot a measure of how many meters each point is off from highest accuracy.

# USAGE
    2 files
usage: LROC_elevation_stats_2_file.py [-h] DTM noDTM

Process two bundleout txt files for statistics

positional arguments:

  DTM:         Bundleout txt file from being run with a dtm and ground points
              EX: ground_DTM_bundleout.txt
              
  noDTM:       Bundleout txt file from being run anyway chosen
              EX: No_ground_noDTM_bundleout.txt

optional arguments:
  -h, --help  show this help message and exit
  
    3 files
usage: LROC_elevation_stats_3_file.py [-h] DTM noDTM no_ground_noDTM

Process three bundleout txt files for statistics

positional arguments:

  DTM:              Bundleout txt file from being run with a dtm and ground
                   points EX: ground_DTM_bundleout.txt
                   
  noDTM:            Bundleout txt file from being run without a dtm but ground
                   points EX: ground_noDTM_bundleout.txt
                   
  no_ground_noDTM:  Bundleout txt file from being run without a dtm or ground
                   points EX: No_ground_No_DTM_bundleout.txt

optional arguments:
  -h, --help       show this help message and exit


# Elvation Stats functions
This file contains all the functions used in the main scripts, a description of each function follows.

*append_to_array_from_file_regex(file, regex)*

Given a file and a regex this function will parse each matched line and take out relevent data (full_id, latitude, longitude, elevation, id_number).
Then will return an array of every detailing every match 

        an example of one of the lists in the array
        ['grdD_00002', 19.45977657, 31.03212227, 1736598.16432, 2]
        
*absolute_difference(value1, value2)*

This function simply returns the absolute difference between two numbers rounded to 5 decimal places

*array_elements_in_common(array_1, array_2, element_to_get)*

Given two arrays and a certain element, this function checks that two points have the same id number then returns an array of the element for matching points 

        EX: X_DTM_noDTM = esf.array_elements_in_common(DTM_point_array, noDTM_point_array, 1) This returns the latitude for each point given that they match
        
        WARNING: because the latitude of two same points will never be exactly the same this will return the average between the two elements. 
        In practice this would rarely cause any noticable differences  
        
        Also as such should never be used on elevation data, ONLY latitude and longitude data
