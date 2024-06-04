Evaluate different languages for reading a large number of ints or
floats from standard input, as is common in competitive programming.
The idea is idiomatic I/O should be reasonably fast in each language.
We find that it frequently is not.

To run this you will need a computer with pypy3, python3, javac, java,
and g++ all in the path.  This should be easily possible on any of the
three main operating systems.  Just clone the repo and type

    pypy3 test.py

Ignore the lines with single values printed.  It will take a minute to
run.

These are the results I get on my Macbook Pro with M3 Max:

````
0.3945059170073364 Java buffered reader
0.5154967090056743 Java buffered reader floats
0.6778063749952707 C++ stdio float
0.7923769999761134 pypy3
0.8021133340080269 C++ stdio
0.8603551249834709 pypy3 floats
1.0798699159931857 cpython3 floats
1.300710582989268 Java scanner nextline
1.3240894589980599 cpython3
2.549021416984033 Java scanner
6.7073696670122445 Java scanner float
11.798656541010132 C++ streams with tie
11.897746583999833 C++ float streams with tie
12.039675417006947 C++ streams
12.08630212501157 C++ float streams
````

On this platform, C++ streams is absolutely crippled because of
the calls to flockfile() and funlockfile() for every single
character of I/O streams, in conjunction with slow pthread-based
Mutexes.  This is likely because of MacOS's adoption of libc++ in
conjunction with the slow spinlocks that MacOS's pthread library
uses.

This is what I get on my (older) Linux platform:

````
0.8856637440039776 Java buffered reader
0.9958639029937331 C++ stdio
1.0082314250175841 C++ streams with tie
1.1685709690209478 Java buffered reader floats
1.408276942995144 C++ stdio float
1.714199414011091 cpython3
1.7240804139873944 pypy3
1.8293919379939325 C++ float streams with tie
1.8359401040070225 cpython3 floats
1.841709150990937 pypy3 floats
3.6473909830092452 C++ streams
4.1413870609831065 Java scanner nextline
4.505658898997353 C++ float streams
7.009067420003703 Java scanner
18.32149303299957 Java scanner float
````

The Java Scanner implementation, which uses regex machinery under
the hood and lots of unneeded memory allocations, is painfully
slow on this (and all) platforms.  Don't believe me?  Check out this:
https://github.com/openjdk-mirror/jdk7u-jdk/blob/master/src/share/classes/java/util/Scanner.java

The thought of all the cycles that are burned unnecessarily on all the
computers processing input using idiomatic I/O, and all the resulting
carbon that's added to the atmosphere, is breathtaking.

Certainly as computer scientists we can do better than this.

Would anyone be willing to run this on a Windows platform?
