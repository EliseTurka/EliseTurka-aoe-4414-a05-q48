# pool_ops.py
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
#  Determines the output shape and operation count of a convolution layer
#  See "Fundamentals of Astrodynamics and Applications, Fourth Edition" by
#  David A. Vallado, pages 172-173
# Parameters:
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# h_pool: avg pooling kernel height count
# w_pool: avg pooling kernel width count
# s: stride of avg pooling kernel
# p: amount of padding on each of the four input map sides
#
# Output:
#  Prints the output channel count, output height count, output width count, # of + 
#  performed, # of x performed, # of / performed
#
# Written by Elise Turka
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import math # math module
import sys  # argv

# initialize script arguments
c_in = float('nan') 
h_in = float('nan') 
w_in = float('nan')
h_pool = float('nan') 
w_pool = float('nan') 
s = float('nan') 
p = float('nan')

# parse script arguments
if len(sys.argv)==8:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
  w_in = float(sys.argv[3])
  h_pool = float(sys.argv[4])
  w_pool = float(sys.argv[5])
  s = float(sys.argv[6])
  p = float(sys.argv[7])
else:
  print(\
   'Usage: '\
   ' python3 conv_ops.py c_in h_in w_in h_pool w_pool s p'\
  )
  exit()


#calculating
h_out = (h_in+2*p-h_pool)/s+1
w_out = (w_in+2*p-w_pool)/s+1
muls = 0
adds = c_in*h_out*w_out*(h_pool*w_pool-1)
c_out = c_in
divs = c_in*h_out*w_out


#printing output
print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs))