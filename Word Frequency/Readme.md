# Word Frequency

## Problem statement
Write a bash script to calculate the frequency of each word in a text file words.txt.

## Expected output

words.txt
```
Hello world
This world is a beautiful place to be
```

expected output:
```
world 2
to 1
place 1
is 1
beautiful 1
be 1
a 1
This 1
Hello 1
```

## Solution

My preferred solution can be found in wordfrequency.sh file.

approach:

* cat read words.txt file
* tokenize with line by line output
* sort the words to prepare for count -c
* output unique words with count (-c)
* sort in natural order (-n) descending (-r reverse)
* tokenize with awk to remove whitespace formatting and reverse the order given by count -c