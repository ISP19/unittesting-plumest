## Unit Testing Assignment

[![Build Status](https://travis-ci.com/plumest/unittesting-plumest.svg?branch=master)](https://travis-ci.com/plumest/unittesting-plumest)
  
by Chayathon Khuttiyanon.  


## Test Cases for unique

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| one nest list  |  list with 1 list inside    |
| one nest list many times  |  list with 1 list inside       |
| 2 nest lists many times many orders  |  2 nested list in the same order     |
| parameter is not list  |  raise TypeError    |


## Test Cases for Fraction

### Initialize

| Test case              |  Expected Result    |
|------------------------|---------------------|
| one parameter is not int or float |  raise TypeError  |
| both parameter are not int or float |  raise TypeError    |
| numerator is inf or -inf  |  inf or -inf    |
| both parameter are 0   |  nan as 0/0 fraction  |
| both parameter are inf or -inf |  nan as 0/0 fraction   |
|   numerator is not 0 denominator is 0   |  inf or -inf  |
|   numerator is 0 denominator is not 0   |     0     |

### String Representation

| Test case              |  Expected Result    |
|------------------------|---------------------|
| both parameter are positive   |  numerator / demominator     |
| both parameter are negative   |  numerator / demominator     |
| one parameter is negative     | - numerator / demominator    |
| have only one parameter       |  numerator  |
| both parameter are zero   |   nan    |
| demominator is 1       |  numerator          |
| demominator is 0 and numerator > 0   |  inf   |
| demominator is 0 and numerator < 0   | -inf  |
| numerator is infinity/-infinity |  inf or -inf  |
| demominator is +/- infinity and numerator is not +/- infinity  |  0  |

### Equal Operator

| Test case              |  Expected Result    |
|------------------------|:-------------------:|
| same proper form       |        True         |
| is not the same proper form       |        False        |

### Addition Operator

| Test case              |  Expected Result    |
|------------------------|---------------------|
| two positive fraction  |  Positive Fraction  |
| two negative fraction  |  Negative Fraction  |
| one positive one negative fraction  |  proper form of them summation  |
| addition with zero  |  same fraction as a proper form  |
|  one fraction is inf or -inf  |  inf or -inf    |
|  one fraction is inf other -inf  |  nan    |
| at less one fraction nan  |  nan  |

### Subtraction Operator

| Test case              |  Expected Result    |
|------------------------|---------------------|
| two positive fraction  |  Positive Fraction  |
| two negative fraction  |  Negative Fraction  |
| one positive one negative fraction  |  proper form of them summation  |
| subtraction with zero  |  same fraction as a proper form  |
| both fraction are the same  |  zero  |
|  one fraction is inf or -inf  |  inf or -inf    |
|  both fraction is inf  |  nan    |
| at less one fraction nan  |  nan  |

### Multiplication Operator

| Test case              |  Expected Result    |
|------------------------|---------------------|
| two positive fraction  |  Positive Fraction  |
| two negative fraction  |  Positive Fraction  |
| one positive one negative fraction  |  Negative Fraction  |
| Multiplication zero  | zero  |
| Multiplication nan  | nan  |
| one fraction is inf/-inf one fraction is non-zero | inf or -inf  |
| one fraction is inf/-inf one fraction is zero | Zero  |

### Negative Operator

| Test case              |  Expected Result    |
|------------------------|---------------------|
| positive fraction  |  Negative Fraction  |
| negativetive fraction  |  Positive Fraction  |
| zero  |  zero  |

### Greater Than

| Test case              |  Expected Result    |
|------------------------|---------------------|
| first fraction greater than other fraction   |  True   |
| first fraction less than other fraction   |  False   |
| two fraction are equal   |  False   |
