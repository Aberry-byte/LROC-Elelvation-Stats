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
usage: LROC_elevation_stats_2_file.py [-h] DTM noDTM

Process two bundleout txt files for statistics

positional arguments:
  DTM:         Bundleout txt file from being run with a dtm and ground points
              EX:ground_DTM_bundleout.txt
  noDTM:       Bundleout txt file from being run anyway chosen
              EX:No_ground_noDTM_bundleout.txt

optional arguments:
  -h, --help  show this help message and exit
  

usage: LROC_elevation_stats_3_file.py [-h] DTM noDTM no_ground_noDTM

Process three bundleout txt files for statistics

positional arguments:
  DTM:              Bundleout txt file from being run with a dtm and ground
                   points EX:ground_DTM_bundleout.txt
  noDTM:            Bundleout txt file from being run without a dtm but ground
                   points EX:ground_noDTM_bundleout.txt
  no_ground_noDTM:  Bundleout txt file from being run without a dtm or ground
                   points EX:No_ground_No_DTM_bundleout.txt

optional arguments:
  -h, --help       show this help message and exit

