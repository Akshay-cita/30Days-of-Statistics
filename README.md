# 30Days-of-Statistics
Statistics with Python

## Day-1 : Mean, Median, and Mode

Calculating the mean, median, and mode

#### Mean:

We sum all elements in the array, divide the sum by
if the array {X1,X2,X3,...,Xn},Finding Mean of the array is (X1+X2+X3+...+Xn)/n

Here ' n ' is number of elements in the array,
#### Median:

To calculate the median, we need the elements of the array to be sorted in either non-increasing or non-decreasing order.
We then average the two middle elements

* If the array is odd number of length the Median will be exactly the middle element of an array

Ex: Consider an array of length 3(The length of array is odd number){X1,X2,X3},the median is X2(i.e,exactly middle element of the array)

* If the array is even number of length the Median will be sum of middle elements and devide the sum by 2

Ex: Consider an array of length 4(The length of array is even number){X1,X2,X3,X4},the median is (X2+X3)/2

#### Mode:

We can find the number of occurrences of all the elements in the array.The maximum no.of occurence element will be the mode of the array

Ex:Consider an array of length 7, {X1,X2,X2,X4,X3,X4,X4}, The mode is X4 .i,e. X4 is repeating 4 time.So the mode of the array is X4

## Day-2:Weighted Mean
Calculating a weighted mean

If the data array is { X1,X2,X3,...Xn}
Corresponding weights are { Y1,Y2,...,Yn }

Calculation of Weighted Mean is ( X1 x Y1 ) + ( X2 x Y2 ) +...+ (Xn x Yn ) / ( Y1 + Y2 +...+ Yn )
[Reference](https://www.hackerrank.com/challenges/s10-weighted-mean/tutorial)

