'''
.       match any charachter
?       preceeding charachter can repeat 0 or 1 time only
+       preceeding charachter can repeat 1 or more times
*       preceeding charachter can repeat 0 or more times
[]      matches any single charachter in the list
[^]     matches any single charachter not in the list
()      combine multiple charachters into one charachter
{N}     exactly N number of charachters
{M,N}   min M and max N
|       OR between conditions
^       match start of string
$       match end of string
\       escape sequence for meta charachter

# Short hand
\d      [0-9]
\D      negate \d
\s      whitespace charachters
\S      neagte \s
\w      alpha-numeric
\b      start or end of the pattern in a word in a string
'''

import re
