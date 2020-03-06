#!/bin/bash

# This bash script reads file.txt file and prints just the 10th line of the file.

if [ -f file.txt ]; then
    echo "file.txt exist"
    file_len=($(wc -l < file.txt))
    echo $file_len
    if [ $file_len -lt 10 ]; then
        echo "file.txt has less than 10 lines."
        exit 0
    else
        echo "$(head -n 10 file.txt | tail -n +10)"
    fi
fi