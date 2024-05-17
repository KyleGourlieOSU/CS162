from assign_6 import gen_list, bubble, sel_sort, timer

if __name__ == "__main__":
    size = 100
    rand_list = gen_list(size=size)
    og_list = rand_list[:] #copy because algorithm affects orginal rand_list
    bb_ls, bb_tm = bubble(rand_list)
    sel_ls, sel_tm = sel_sort(rand_list)
    print(f'List Before Sorting:\n{og_list}\n')
    print(f'List After Bubble Sorting:\n{bb_ls}\n')
    print(f'List After Selection Sorting:\n{sel_ls}\n')
    timer()