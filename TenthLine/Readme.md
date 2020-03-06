# TenthLine

## Problem statement
Given a text file called file.txt, print just the 10th line of the file.

## Solution
There are different ways to solve this problem. Following are the one line solution which are not the efficient ones, we can know the time command to time each solution. My preferred solution is in TenthLine.sh file

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