#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:37:48 2018

@author: Kenneth Comollo
"""

#tested on Ubuntu VM Version xxxxx
#
# 1. Looks in files modified within a user-specified timeframe
# 2. Prints lines containing a user-specified string
  

import os, datetime, glob, re

# define epoch time
t0 = datetime.datetime.utcfromtimestamp(0)

def get_startTime():
    
    startTime = input("Please enter start time of search: MM-DD-YY HH:MM\n")
    try:
        startTime = (datetime.datetime.strptime(startTime, "%m-%d-%y %H:%M") - t0).total_seconds()
    except ValueError:
            raise ValueError("Incorrect format - should be MM-DD-YY HH:MM")
    return startTime
    

def get_endTime():
    
    endTime = input("Please enter end time of search: MM-DD-YY HH:MM\n")
    try:
        endTime = (datetime.datetime.strptime(endTime, "%m-%d-%y %H:%M") - t0).total_seconds()
    except ValueError:
            raise ValueError("Incorrect format - should be MM-DD-YY HH:MM")
    return endTime


def get_username():
    
    username = input("Please enter the username you would like to search for:\n")
    return username


def find_files(startTime_input, endTime_input):

    path = "/home/kcadmin/test"
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            search_files = '/'.join([dirpath,filename])
            searchTimeFrame = os.stat(search_files)[-1]
            if searchTimeFrame>=startTime_input and searchTimeFrame <=endTime_input:
                file_list.append(search_files)
    return file_list


def find_string(username_input):
    path = glob.glob("/home/kcadmin/test/*")
    matches = []
    for filename in path:
        with open (filename, "r") as target:
            for line in target:
                if re.search(username_input, line):
                    matches.append(line.rstrip())
    return matches

                               
startTime_input = get_startTime()
endTime_input = get_endTime()
username_input = get_username()
files_to_search = find_files(startTime_input, endTime_input)
matching_lines = find_string(username_input)
print(matching_lines)

