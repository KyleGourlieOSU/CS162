from assign_5 import lin_srch, bin_srch
import random

low = 0
high = 1000
num_int = 100
cut_off = 1000
ints = []

for i in range(num_int):
    ints.append(random.randint(low,high))
ints.sort()

rand_ele = random.randint(0,100)

def test_bi():
    """tests the binary search algorithm"""
    actual_val = ints[rand_ele]
    bi_ele = bin_srch(ints, actual_val)
    assert bi_ele == rand_ele

def test_ln():
    """tests linear search algorithm"""
    actual_val = ints[rand_ele]
    ln_ele = lin_srch(ints, actual_val)
    assert ln_ele == rand_ele

