<!-- markdownlint-disable-file-->

<center>

# <strong><font size = "7"> Run Time Visualizer </font></strong>

<strong><font size = "5">This Run Time Visualizer is made with python, it visualizes different run times of algorithms</font></strong>

</center>

<br><br>

## <font size = "6"> Requirements </font>
- Python
- matplotlib

<br>

## <font size = "6"> Overall Functionality </font>
The user would place a python file in the folder where the files for this program is kept, the user's python file should have a function named "main"(this function will be the algorithm whose time would be measured), the python file would also need to have a dictionary named "inputTimes", the dictionary would need to have numbers as the keys and any data-structure(list/tuples/integers/string etc.) as a value, The data-structure in the dictionary values should be the input for the function and the keys corresponding to each data-structure in the dictionary should be representing how large the data-structure is. The user then starts the program, A GUI(Graphical User Interface) opens up and asks the user for the file name(the python file in which there is algorithm and the "inputTimes" dictionary). Then when the user clicks on next, the program opens up a line graph representing the time it took for the algorithm according to the size of the inputs.

NOTE : The data structure given as the value in the "inputTimes" dictionary will only be passed, so if your algorithm needs multiple inputs then I recommend that you make a list of arguments to pass and then unpack the list and get the arguments needed for the function that way. See the examples if you are still confused.
