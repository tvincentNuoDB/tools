###About
These are just some simple and useful scripts I've wrote to automate things

###Beautifier
This is a tool which replaces any number of key value string pairs from the command line. 
I created it with the intent to automate the replacement of colors in python doc.

To run it use
```bash
javac Beautifier.java
java Beautifier [COLOR=NEW_COLOR] ... [FILENAME]
```

For example let's transform some ugly python documentation to use beautiful flat colors!
```bash
java Beautifier ffc8d8=af7ac5 7799ee=3498db ee77aa=8e44ad 55aa55=2ecc71 module.html 
```

###Benchmarker
Currently this is hard coded, although it compairs the preformance of the NuoDB Python, Ruby and JDBC drivers without bias.
