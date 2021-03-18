import clr
import sys
clr.FindAssembly("ClassLibrary1.dll")

from ClassLibrary1 import Class1
helloworld = Class1()
helloworld.HelloWorld()

