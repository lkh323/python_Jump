# import mod1
# print(mod1.add(1,2))
# print(mod1.sub(1,2))

# from mod1 import add, sub
from mod1 import *
add(3,4)
sub(3,1)

mod1.__name__

# if __name__ == "__main__":의 의미


import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))


import sys
sys.path
sys.path.append("C:\Dev\python_Jump\mymod")

import mod2
print(mod2.add)


import sys
sys.path
sys.path.append("C:\Dev\python_Jump")





