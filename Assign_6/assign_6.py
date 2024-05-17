import random
import time
import matplotlib.pyplot as plt

def gen_list(size:int)-> list:
   """
   summary: Generate random list of integers between -1000 and 1000
   """
   _list = []
   for i in range(size):
       rand_num = random.randint(-1e3,1e3)
       _list.append(rand_num)
   return _list



def bubble(_list)-> list:
   """
   summary: Sorting algorithm for Bubble. Places array of integers
    from smallest to largest values

   The way this algorithm works is for each iteration of the entire list, each element
   is compared to the element to the right of it. If the element to the left is larger 
   than to the element to the right, then the elements are fliped. This algorithm repeats
   through the entire list over and over again until no more swapping occured. 

   returns:
    - _list(list): list of sorted integers
    - diff_time: time increment it took to run through algorithm
   """
   time_in = time.time()
   #if the counter remains non-zero, then the algorithm will keep checking elements
   while True:
       counter = 0   #resets counter every time it re-processes the loop
       for i in range(1,len(_list)):
           val = _list[i-1] <=_list[i]   #if left element is greater than right element, then is False
           if val:
               pass
           else:
               _list[i-1], _list[i] = _list[i], _list[i-1]   #swapping
               counter = counter + 1
       #ends algorithm
       if counter == 0:
           time_out = time.time()
           diff_time = time_out-time_in
           return _list, diff_time



def sel_sort(_list)-> list:
   """
   summmary: Sorting algorithm of Selection. Places array of integers
    from smallest to largest values

   The way this algorithm works is through two iterations. The first iteration will
   go through the entire array. For each element in the first iteration, a second iteration
   will occur to check to see if this specified element is the lowest element so far. If it
   is not, it will get swapped, making the swapped element now the newest lowest element. This 
   process keeps on occuring until the lowest element is now placed in the lowest index. Next, 
   the array is iterated again and this process is continued until no more elements are left to 
   pass through. With each first iteration of the array, the searchable elements decrease by 1. 

   returns:
    - _list(list): list of sorted integers
    - diff_time: time increment it took to run through algorithm
   """
   time_in = time.time()
   for i in range(len(_list)):
       for j in range(i+1, len(_list)):
           if _list[i] > _list[j]:
               _list[i], _list[j] = _list[j], _list[i]
   time_out = time.time()
   diff_time = time_out - time_in 
   return _list, diff_time



def default_sort(_list)-> list:
    """
    summary: Sorting algorithm using the default python method. Places array of integers
    from smallest to largest values

    returns:
    - _list(list): list of sorted integers
    - diff_time: time increment it took to run through algorithm
    """
    time_in = time.time()
    _list.sort()
    time_out = time.time()
    diff_time = time_out-time_in
    return _list, diff_time

     
           
def timer():
   """
   summary: Timer that takes measurements of total time taken to process through
   each algorithm, and plots the data

   return: None
   """
   sizes = []
   bb_tms = []
   sel_tms = []
   default_tms = []
   size = 1
   lim = 1000
   #computes each sorting algorithm per array size
   while size <= lim:
       _ls = gen_list(size)
       #sorting algorithms
       bb_ls, bb_tm = bubble(_ls)
       sel_ls, sel_tm = sel_sort(_ls)
       default_ls, default_tm = default_sort(_ls)
       
       #ensures all arrays agree
       if bb_ls == sel_ls and bb_ls == default_ls:
           print(f'passed at {size} iteration', end='\r',flush=True)
           sizes.append(size)
           bb_tms.append(bb_tm)
           sel_tms.append(sel_tm)
           default_tms.append(default_tm)
           size = size+1
       #just in case. Has NOT broken at all
       else:
           print(f'FAILED at {size} iteration')
           exit()
   #plots data and saves plot
   plt.title('Time vs Array Size of Sorting Algorithm')
   plt.plot(sizes, bb_tms, label='Bubble')
   plt.plot(sizes, sel_tms, label='Selector')
   plt.plot(sizes, default_tms, label='Defaut')
   plt.xlabel('Size of Array')
   plt.ylabel('Time [s]')
   plt.legend()
   plt.savefig('timed.png')
   plt.show()
   