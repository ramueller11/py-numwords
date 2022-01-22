# py-numwords
https://github.com/ramueller11/py-numwords

A simple implementation of a whole number to written English form interconverter. 
However, other languages maybe supported with some modification.

The use case for this package includes parsing configuration files written by humans 
that speak English.

## Examples
Converting into words:
```
from numwords import *

int2words(555) = 'five hundred fifty five'
int2words(0)   = 'zero'
int2words(-1245) = 'negative one thousand, two hundred fourty five'
```

Converted from words:
```
words2int('one') = 1
words2int('first') = 1 
words2int('a hundred') = 100
words2int('none') = 0
words2int('negative ten') = -10
```

# Dependencies 
There are no other dependencies other than the python standard library.
It should work in both python 2.7 and python 3 environments.

# Tests 
To perform testing using `pytest` of the project in the local cloned directory, type:
```
pytest
```

Or equivalently, 
```
python -m pytest
```

# Installation
A setup.py file is defined for this project. 
In the cloned directory, type: 
```
pip install .
```

Note, there is only one source code module and can be copied into other codebases directly without 
requiring another package dependency. This module is located at `./src/numwords/numwords.py`


