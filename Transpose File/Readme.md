# Transpose File

## Problem statement

Given a text file file.txt, transpose its content.

You may assume that each row has the same number of columns and each field is separated by the ' ' character.

Example:

## Expected output

file.txt
```
name age
alice 31
ryan 90
```

expected output:
```
name alice ryan
age 31 90
```

## Solution

My preferred solution is using awk command which can be found in transposefile.sh script.