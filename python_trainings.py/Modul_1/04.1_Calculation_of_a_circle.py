#from math import *, can be used to imports everything from math. 
#To avoid name conflicts, use: "import math" and "math.pi" instead in this case here.

import math

diameter = float(input("Please enter the diameter of the circle in mm. "))

area = diameter **2 * math.pi

print(f"The area of the circle is {area}mm^2.")