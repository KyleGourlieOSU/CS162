from assign_6 import gen_list, bubble, sel_sort

_sample_list = gen_list(2000)

def bub_test():
    """
    Test to make sure Bubbles algorithm correctly sorts 2000-array data
    """
    og_list = _sample_list[:] #copy of origonal list
    bub_list = bubble(og_list)
    expected_list = og_list.sort()
    _bool = bub_list == expected_list
    assert _bool


def sort_test():
    """
    Test to make sure selection sorting algorithm correctly sorts 2000-array data
    """
    og_list = _sample_list[:] #copy of origonal list
    sel_list = sel_sort(og_list)
    expected_list = og_list.sort()
    _bool = sel_list == expected_list
    assert _bool


