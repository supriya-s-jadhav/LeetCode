#!/bin/bash

# This script will print the valid phone numbers from  file.txt file. The file.txt file has list of phone numbers, one phone number per line. The valid phone number format is (xxx) xxx-xxxx or xxx-xxx-xxxx where x means digit.

cat file.txt | grep -E '^(:?[0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$'

