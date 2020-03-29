# Implement Natural Logarithm

Description:
- Implement the ln() function, but don't use the library log functions or integration functions. 
- Solutions should be within 1e-6 of the actual value (i.e. |student_ln(x) - ln(x)| < 1e-6)

Hints:
- This is for the sorting and searching section of the course. Don't use integration or bit manipulation.
- What if you were given a sorted list of values where at least one of them were guaranteed to be acceptable?
- ln() is (strictly) monotonically increasing -- i.e. for x < y in the domain, ln(x) < ln(y)

Examples:
- 2.718281828459045 -> 1 (or anything within 1e-6 of 1)
- 20.085536923187668 -> 3 (or anything within 1e-6 of 3)

Edge cases:
- ln(0) should return the floating point negative infinity float('-inf')
- ln(x) for negative x should raise ValueError (it's an invalid input)
