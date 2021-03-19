<!-- markdownlint-disable-file-->

<center>

# <strong><font size = "7"> Run Time Visualizer </font></strong>

<strong><font size = "5">This Run Time Visualizer is made with python, it visualizes different run times of algorithms with different sizes of inputs</font></strong>

</center>

<br><br>

## <font size = "6"> Requirements </font>
- Python
- matplotlib

<br>

## <font size = "6"> Overall Functionality </font>

<ul>

The user would place a python file in the folder where the files for this program is kept, the user's python file should have a function named "main"(this function will be the algorithm whose time would be measured), the python file would also need to have a dictionary named "inputTimes", the dictionary would need to have numbers as the keys and any data-structure(list/tuples/integers/string etc.) as a value, The data-structure in the dictionary values should be the input for the function and the keys corresponding to each data-structure in the dictionary should be representing how large the data-structure is. The user then starts the program, A GUI(Graphical User Interface) opens up and asks the user for the file name(the python file in which there is algorithm and the "inputTimes" dictionary). Then when the user clicks on next, the program opens up a line graph representing the time it took for the algorithm according to the size of the inputs.

NOTE : The data structure given as the value in the "inputTimes" dictionary will be the only argument passed on the function, so if your algorithm needs multiple inputs/arguments then I recommend that you make a list of arguments to pass and then unpack the list inside the function. See the examples if you are still confused.

</ul>

## <font size = "6"> How does it work </font>

<ul>

The main.pyw file is the starting point of the program. When the user runs the main.pyw file, the main.pyw file shows a GUI with a textbox and two buttons, one button is the "about" button, this button shows the user some information regarding the program. The other button is the "submit" button, this button when clicked the function generateGraphFromFile from the generateGraph.py file is called, the generateGraphFromFile function takes in the file name that the user has given. This function calls another function called getData, This function takes in the file name that the user has entered and then imports it. Then it gets the "inputTimes" dictionary from the file that the user had entered. Then it creates a new dictionary, then starts to iterate through the keys and values(arguments for the user's function). for each key and value, it runs the main function of the file by giving it the value and then measures its time. After that it maps the keys to the time and then continues the loop. It returns  the new dictionary after the loop has ended.

Then once the getData function has returned the dictionary, we come back to the generateGraphFromFile function. After getting the run times of all the values it stores it in a variable called, "runTimes" then it calls another function named "createGraph", this function takes in the runTimes and creates a graph out of it using the matplotlib library.  

NOTE : The file name should be passed without the ".py" extension.

NOTE : the program might lag a little when generating the graph. The best thing to do is to wait for the graph to be generated and then once the graph is closed then the program will starting performing perfectly again. 

</ul>


<br>

## <font size = "6"> What can it be used for ? </font>

<ul>

it can be used for estimating the Big O Notation of Algorithms.

</ul>

<br>


<font size = "4"> 

> This project was made By [Ved Rathi](https://ved-programmer.github.io/Ved-programmer/) for a Timathon Code Jam


***-Thank you***

</font>


