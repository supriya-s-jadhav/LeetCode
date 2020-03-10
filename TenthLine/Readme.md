# TenthLine

## Problem statement
Given a text file called file.txt, print just the 10th line of the file.

## Expected output

file.txt
```
line 1
line 2
.
.
line 10
```

expected output:
```
line 10
```

## Consider cases :

1. If the file.txt has less than 10 lines.
2. If the file.txt has million rows. Out of all possible solutions, check which one will be time efficient.

## Solution
There are different ways to solve this problem. Following are the possible one line solutions, use time command to time each solution and see which is the most time efficient. My preferred solution is in tenthLine.sh file

### Solution 1

Use awk
```
awk 'NR==10' file.txt
```
### Solution 2

Use combination of head and tail command
```
head -n 10 file.txt | tail -n +10
```

### Solution 3

Use sed
```
sed -n 10p file.txt
```