# Flush Argument - The I/Os in python is generally buffered, meaning they are used in chunks.
# This is where flush comes in as it helps users to decide if they need the written content to be buffered or not.

import time

count_sec = 3
for i in reversed(range(count_sec+1)) :
    if i > 0 :
        print(i, end=" >>> ", flush = True)
        time.sleep(1)
    else :
        print("Start")