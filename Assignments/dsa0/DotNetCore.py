import os

import clr
import sys

clr.FindAssembly("ClassLibrary1.dll")
parent_path = os.path.dirname(sys.path[0])
if parent_path not in sys.path:
    sys.path.append(parent_path)
clr.FindAssembly("ClassLibrary1.dll")
a = clr.AddReference("ClassLibrary1")
from ClassLibrary1 import Class1

helloworld = Class1()
helloworld.HelloWorld()
