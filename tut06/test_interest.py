import pytest
from interest import calculate_simple_interest
from interest import calculate_compound_interest

def  test_calculate_simple_interest():
	principal =  1000
	interest =  4
	years =  5
	assert(calculate_simple_interest(principal,interest,years) ==  200)

#2nd test case to test_interest.py


def  test_calculate_compount_interest():
	principal =  1000
	interest =  5
	years =  5
	assert(calculate_compound_interest(principal,interest,years) ==  276.2815625000003)

