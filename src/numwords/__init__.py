"""
numwords.py 

Interconvert english phrases with whole numbers.
https://github.com/ramueller11/py-numwords.git

Example:
    int2words('555') = 'five hundred fifty five'
    
    words2int('one') = 1
    words2int('first') = 1 
    words2int('a hundred') = 100
    words2int('none') = 0
    words2int('negative ten') = -10
"""

version = '0.1'

from .numwords import (int2words, words2int,)