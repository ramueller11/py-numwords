# py-numwords
A simple implementation of a whole number to written English form interconverter. 
However, other languages maybe supported with some modification.

The use case for this package includes parsing configuration files written by humans 
that speak English.

## Examples
Converting into words:
```
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
