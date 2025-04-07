Mikisha Aryanna Pillay - 2426761

The program getbest.py should find the top student in the class, from the results in the bestdat0.csv file.
Adding the ___init___.py file was necessary to ensure everything is read as a package through the programme/tests.

You have to have a file like the bestdat0.csv file that includes the data as such:
Course,Student Number,Mark,Comment
ELEN3020,160001,72,OK
ELEN3020,167381,90,Check
ELEN3020,143211,83,-
ELEN3020,17171,48,Redo
ELEN3020,191919,73,-


We have to run unit tests in order to see if the code works and is running fine. 
~ First unit test will check the getcols function in getbest.py, using first_test.py:
  To run first_test.py, we type this command into the terminal:
     **python -m unittest Unit-tests/first_test.py**

Running the unit test should result in this output, indicating the indexes of the Student Number and the Mark columns

Student Number column: 1
Mark column: 2
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
    
 - This accesses the first_test.py in the Unit-tests folder


To get the program (in getbest.py) running and produce a result, type this command:
        **python3 Code/getbest.py Code/bestdat0.csv**

 Which should output: The top student was student 167381 with 90

    -This accesses the getbest.py file in the "Code" folder and the same for the bestdat0.csv file.



