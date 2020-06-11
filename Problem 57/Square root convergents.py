#square root of 2 can be represented by a continuous fraction [1;2,2,2,....]
#I selected these specific values from an example on wikipedia
from time import time
start = time()

pre_prev_numo = 1
pre_prev_deno = 0
prev_numo     = 1       #numo = a0
prev_deno     = 1
curr_numo     = 1
curr_deno     = 1
iterations    = 1000
count         = 0
for i in range(iterations-1):
    curr_numo     = prev_numo*2 + pre_prev_numo
    curr_deno     = prev_deno*2 + pre_prev_deno
    pre_prev_numo = prev_numo
    pre_prev_deno = prev_deno
    prev_numo     = curr_numo
    prev_deno     = curr_deno
    #print(curr_numo,curr_deno)
    if len(list(str(curr_numo))) > len(list(str(curr_deno))):
        count += 1

print(count)

end = time()
print("=====================================")
print("time taken : " + str(end-start) + " s")
print("=====================================")
