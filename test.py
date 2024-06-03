#
#   Test some various methods of doing I/O.
#
n = 10000000
import os, timeit
def ccompile(s):
   os.system(f"g++ -std=c++17 -O2 -o {s} {s}.cpp")
def jcompile(s):
   os.system(f"javac {s}.java")
a = []
def timeexe(s, desc=""):
   t = timeit.default_timer()
   os.system(s)
   t = timeit.default_timer() - t
   if desc != "":
      a.append([t, desc])
ccompile("gen")
os.system(f"./gen {n} > t.in")
timeexe("pypy3 input.py < t.in")
timeexe("pypy3 input.py < t.in", "pypy3")
timeexe("pypy3 inputfloat.py < t.in", "pypy3 floats")
timeexe("python3 input.py < t.in", "cpython3")
timeexe("python3 inputfloat.py < t.in", "cpython3 floats")
ccompile("stream")
timeexe("./stream </dev/null")
timeexe("./stream <t.in", "C++ streams")
ccompile("streamfloat")
timeexe("./streamfloat </dev/null")
timeexe("./streamfloat <t.in", "C++ float streams")
ccompile("streamtie")
timeexe("./streamtie </dev/null")
timeexe("./streamtie <t.in", "C++ streams with tie")
ccompile("streamfloattie")
timeexe("./streamfloattie </dev/null")
timeexe("./streamfloattie <t.in", "C++ float streams with tie")
ccompile("stdio")
timeexe("./stdio </dev/null")
timeexe("./stdio <t.in", "C++ stdio")
jcompile("scanner")
timeexe("java scanner < t.in", "Java scanner")
jcompile("scannerfloat")
timeexe("java scannerfloat < t.in", "Java scanner float")
jcompile("bufreader")
timeexe("java bufreader < t.in", "Java buffered reader")
jcompile("nextline")
timeexe("java nextline < t.in", "Java scanner nextline")
a.sort()
for t,s in a:
   print(t, s)
