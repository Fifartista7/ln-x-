# CMSC389O Spring 2020
# HW3: Searching & Sorting -- Implement Natural Logarithm

# Description:
# Implement the ln() function, but don't use the library log functions or integration functions.
# Other library functions are fine
# Solutions should be within 1e-6 of the actual value (i.e. |student_ln(x) - ln(x)| < 1e-6)

# Hints:
# - This is for the sorting and searching section of the course. Don't use integration or bit manipulation.
# - What if you were given a sorted list of values where at least one of them were guaranteed to be acceptable?
# - ln() is (strictly) monotonically increasing -- i.e. for x < y in the domain, ln(x) < ln(y)

# Examples:
# 2.718281828459045 -> 1 (or anything within 1e-6 of 1)
# 20.085536923187668 -> 3 (or anything within 1e-6 of 3)

# Edge cases:
# ln(0) should return the floating point negative infinity float('-inf')
# ln(x) for negative x should raise ValueError (it's an invalid input)

# Running the public tests:
# python3 PublicTests.py

# Submit server notes:
# 2 of the release tests (9 and 10) are performance tests.
# Failing either of the last 2 tests (red box) is probably not due to
# correctness issues if you are passing the other tests.

# for student use
import math 

EPSILON: float = 1e-6

#idea: e to the what exponent gives x
def student_ln(x: float) -> float:
 
    mid = 0.00000   #value to return 

    #check edge cases
    if x == 0:  
        return float('-inf')
    elif x < 0:
        raise ValueError("it's an invalid input")

    #use binary search to find the desired number
    else:  
        #if value is very small the answer will return a negative value, 
        # therefore, we need a negative lower bound
        if x < 1:
            lower = -1*math.pow(10,300)
            #upper = 0-EPSILON
        else:  #if value is greater than 1 we will have a positive lower bound
            lower = 0.0

        #declare the variables to use
        upper = x-EPSILON
        mid = upper/2
        range_start = x-EPSILON
        range_ends = x+EPSILON
       
        #binary search part, compare lower and upper bound to the e^result value
        while lower <= upper:
                
                #used if given value is very large or very small.
            if x < 1 or x > 1000:  
                curr = math.e**mid
            else:   #use exp to run faster with small numbers (1:1000)
                curr = math.exp(mid)

            if curr > (range_ends):  #reduce upper bound
                upper = mid 
                mid -= (upper-lower)/2
            elif curr < (range_start):  #increase lower bound
                lower = mid 
                mid += (upper-lower)/2 

            elif curr >= range_start and curr <= range_ends:   #if in range
                return mid

        return mid

    # Writeup: This algorithm consists of a series of if statements and binary search to obtain the value of ln(x). 
    # First, we start by checking the edge cases when the given value is 0 or a negative number. Then we set the upper bound, 
    # lower bound, middle value and accepted precision range (EPSILON). The lower bound is determined based on the given value,
    # if the value is less thas than 1 the lower bound is negative and positive otherwise. Followed by a binarry search algorithm
    # to fnd the value between the lower and upper bound. "math.exp(x)" is ussed to represent e^x and I use it when the range of 
    # numbers is not under one or above 1k so the algorithm is faster since .exp can ve very expensive when very small or large numbers. 
    # In addition, I use e**x which to bypass the math range overflow unlike the math.exp and math.pow. 

    # Observations: the algorightm seems to fail in precision of more than EPSILON when the value is very small (e.g. less than 0.1)
    # and some other values like 0.4 and 0.6, even though it works for 0.3 and 0.5, for some reason. Any feedback is appreciated. 

    # Time Complexity: O(logn) - because of the binary search 
    # Space Complexity: O(1) - no additional memory used besides local variables
    # By Josue Arana