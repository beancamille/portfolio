# Code Samples from Coursework

### Systems Development
The following code samples were written for homework assignments as part of a course in systems development. The course explored practical development methods with an emphasis on scientific applications. Topics covered included version control, data structures, and object-oriented programming. 

`heap_build.py` implements a binary heap structure, creating each node using the class `Heap`, and building the heap with the function `heapify`. `heapify` uses helper functions to organize the heap, comparing each node to the ones around it and swapping positions accordingly. A string conversion method in `to_string` represents the heap as a printable tree. Subclasses `MinHeap` and `MaxHeap` allow parent nodes to be lesser or greater than child nodes, respectively.

The folder `markov` contains a Markov chain implementation from class methods, along with a demonstration of the class. `markov.py` defines the class `Markov`. This class implements a Markov chain, which is a stochastic model in which current states probabilistically determine next states. In particular, in `Markov`, the current weather is used to predict the next day’s weather, and so on. `markov_demo.py` demonstrates the class by predicting the weather for seven cities. It loads from `weather.csv`, which provides the probabilities for sunny, cloudy, rainy, snowy, windy, or hailing weather, given that the “day zero” weather is one of those weather types. `markov_demo.py` initializes Markov chains for each city. Then, using the function `get_weather_for_day` from `Markov`, it simulates the weather after 7 days, 100 times for each city. It prints both the results of the simulations and the most likely final weather for each city. 

### Computational Science
The following code samples were written for homework assignments as part of a course in computational science. The course explored methods and infrastructure for big data and big compute needs. Emphasis was given to applications in computational and data science.  

The folder `stock_MapReduce` contains an example of the MapReduce model, which is used to handle big data in the file `stocks.csv`. Each line of `stocks.csv` provides closing daily stock prices for a company, starting from 2009. `stock_mapper.py` loads in data from the csv, outputting lines composed of keys (years) and values (prices). `stock_reducer.py` finds the average closing price for each year and prints the result. The code can be run with the Linux command  ` ./stock_mapper.py < stocks.csv | sort | ./stock_reducer.py` . 

The folder `ratings_spark` includes a Spark example that uses resilient distributed datasets (RDDs) to organize movies into groups based on their average rating. First, ratings are loaded in from `ratings.csv` and RDDs are created that map movie IDs to their ratings and to the number of times they appear on the list. These RDDs are joined to find the average ratings for each movie, and then filters are used to divide movies into 5 ratings brackets. The results are saved to the file `ratings_spark.txt`. This code requires Scala, Python, Java, and Apache Spark 2, and can be run using a spark-submit method with the command `spark-submit ratings_spark.py`. The output can be read with the command `cat ratings_spark.txt/*` .

### Computing Hardware
The following code sample was written as a homework assignment in a course in computing hardware. The course explored topics such as combinational and sequential logic, computer architecture and microarchitecture, and machine code. Coding components for the course were written to be executed on an FPGA. 

The code contained in the folder `ALU` implements an arithmetic logic unit (ALU) that can be converted to a bitstream for use on a Nexys A7 FPGA. The code was tested and written using the Xilinx Vivado design suite, hosted on a VMWare Linux virtual machine. This code was written in collaboration with one other student. 

The contents of the folder `tcl` are tcl scripts, provided by the instructor, that allow the code to be built and opened to Vivado from the command line. `tcl.sh` is the shell script used to run these tcl scripts. 

The contents of the folder `constraints` are the constraints, provided by the instructor, that are necessary for formatting on the Nexys A7.

The folder `hdl` includes the SystemVerilog files that implement the ALU. `alu.sv` is the main module of the alu, and it calls on some helper modules. `alu.sv` takes two 32-bit inputs `x` and `y` and a 3-bit op-code to select the operation. It outputs one 32-bit output `z` and three 1-bit flags `zero`, `equal`, and `overflow`. `zero` is high when `z` is 0, `equal` is high when `x` and `y` are equal, and `overflow` is high when the operation produces an overflow. `x`, `y`, and `z` are all two’s-complement integers. 

The ALU is capable of the following functions: and, add, sub, set if less than, shift right logical, shift right arithmetic, and shift left logical. It finds the solution for each of these functions in `alu.sv`, calling on the helper modules `add.sv` (a ripple carry adder), `sll.sv` (shift left logical), `slt.sv` (set if less than), `sra.sv` (shift right arithmetic), and `srl.sv` (shift right logical). `sra.sv` and `srl.sv` call on `rshifter.sv`, which is a right-shift helper module. `alu.svh` defines the 3-bit opcodes used by the ALU. `alu_top.sv` defines what parts of the FPGA will be used when the bitstream is uploaded. It calls on helper modules `hex_to_sseg.sv` and `disp_mux.sv`. `alu_top.sv` and its helpers were provided by the instructor. `alu_tb.sv` is a testbench used on the ALU, for confirming validity during simulation in Vivado.

The folder `synth_output` includes `alu.bit`, which is the synthesized bitstream that can be uploaded to the FPGA. It also includes a report on the synthesis created by Vivado, `post_route_util.rpt`. 
