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