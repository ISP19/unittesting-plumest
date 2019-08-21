## Unit Testing Assignment

by Bill Gates.


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
| both parameter are 0   |  raise ValueError   |
| both parameter are inf or -inf |  raise ValueError   |
| one parameter is not int or float |  raise TypeError  |
| both parameter are not int or float |  raise TypeError    |
| numerator is inf or -inf  |  inf or -inf    |
|   numerator is not 0 denominator is 0   |  inf or -inf  |
|   numerator is 0 denominator is not 0   |     0     |

### String Representation

| Test case              |  Expected Result    |
|------------------------|---------------------|
| both parameter are positive   |  numerator / demominator     |
| both parameter are negative   |  numerator / demominator     |
| one parameter is negative     | - numerator / demominator    |
| have only one parameter       |  numerator (default of demominator is 1) |
| demominator is 1       |  numerator          |
| demominator is 0 and numerator > 0   |  infinity   |
| demominator is 0 and numerator < 0   | negarive infinity   |
| numerator is infinity and demominator >= 0  |  infinity  |
| numerator is infinity and demominator < 0  | negarive infinity  |
| demominator is +/- infinity and demominator is not +/- infinity  |  0  |

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
| addition zero  |  same fraction as a proper form  |
| summation is full number   |  Fraction class that denominator = 1 and numerator is the result of sumation (which is full number)    |
|  one fraction is inf or -inf  |  inf or -inf    |

### Subtraction Operator

| Test case              |  Expected Result    |
|------------------------|---------------------|
| two positive fraction  |  Positive Fraction  |
| two negative fraction  |  Negative Fraction  |
| one positive one negative fraction  |  proper form of them summation  |
| subtraction with zero  |  same fraction as a proper form  |
| both fraction are the same  |  zero  |
| sumation is full number   |  Fraction class that denominator = 1 and numerator is the result of sumation (which is full number)    |
|  one fraction is inf or -inf  |  inf or -inf    |

### Multiplication Operator

| Test case              |  Expected Result    |
|------------------------|---------------------|
| two positive fraction  |  Positive Fraction  |
| two negative fraction  |  Positive Fraction  |
| one positive one negative fraction  |  Negative Fraction  |
| Multiplication zero  | zero  |
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