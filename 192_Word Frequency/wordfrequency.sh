#!/bin/bash

# This script reads teh file.txt text file and prints the word count

cat words.txt | xargs -n1 | sort | uniq -c | sort -nr | awk '{print $2 " " $1}'
