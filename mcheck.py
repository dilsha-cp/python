import math

import module


module.test(10)
module.test(0)
check = module.test
check(-1)
print(__name__)
# there nme print main bec it is main file
# also call tahe module like from module import test
from module import test
test(40)
# to chek the os
import platform
print(platform.system())
print(platform.processor())
print(platform.python_compiler())
print(math.factorial(3))