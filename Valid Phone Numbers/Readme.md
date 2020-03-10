# Valid Phone Numbers

## Problem statement
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

## Expected output

file.txt
```
(123) 456-9899
123 123 123
123-456-8888
```

expected output:
```
(123) 456-9899
123-456-8888
```

## Solution

Possible solutions include using sed or combination of grep and regexp. My preferred solution can be found in the bash file in current directory.