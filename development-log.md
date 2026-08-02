# Project 1 - Temperature Calculator
**Date Completed:** 1 july 2026

## Evidence
Repository:
python-projects/project-01-temperature-converter.py

## Objective
Begin learning Python and complete the first milestone project.

## Skills Learned
- Variables
- User input
- Basic arithmetic
- Using print() to display results
- Taking input from the user

## Reflection
This project introduced the fundamentals of Python programming. Although simple, it will play a crucial role in future projects by providing me with the basic concepts of how python can be used to solve practical problems

## Next Objective
Continue advancing in python and develop a Physics Formula Calculator capable of calculating quantities such as force, speed, density, momentum, and kinetic energy.


# Project 2 – Physics Formula Calculator
**Date Completed:** 11 July 2026

## Evidence
Repository:
python-projects/project-02-Physics-Calculator

## Objective
Develop a Python program that calculates common physics equations quickly and accurately, while reinforcing my understanding of the formulas used in IGCSE Physics.

## Skills Learned
- Functions
- Conditional statements (`if`, `elif`, `else`)
- User input handling
- Mathematical calculations
- Organising code into reusable sections

## Challenges
- Preventing invalid inputs from causing errors.

## Reflection
This project strengthened my understanding of Python functions and conditional logic while reinforcing important physics concepts. It also taught me how to write programs that are organised, readable, and practical.

## Next Objective
Use the programming skills gained from this project to build more advanced scientific applications involving data analysis, graphing, and numerical simulations.


# Project 3 - Temperature Statistics Calculator
**Date Completed:** 14 July 2026

## Evidence
Repository:
python-projects/project-03-Temperature-Statistics Calculator.py

## Objectives
- Accept multiple temperature readings from the user.
- Convert text input into numerical values.
- Calculate the mean temperature.
- Determine the maximum and minimum temperatures without relying on Python's built-in functions.
- Handle invalid user input using exception handling.

## Skills Practiced
- Lists
- Functions
- Loops
- Conditional statements
- Type conversion (`float`)
- Exception handling (`try` / `except`)
- Returning values from functions
- Basic algorithm design


## Challenges 

### 1. Processing User Input
The program initially receives data as a string. I learned how to split the input into individual values and convert each value into a floating-point number for calculations.


### 2. Implementing Maximum and Minimum Algorithms
Instead of using Python's built-in `max()` and `min()` functions, I created my own algorithms to better understand how iteration works.

## Reflection
Although this project analyzes manually entered temperature data rather than collecting measurements from a sensor, it represents an important milestone in my learning journey. It demonstrates how numerical data can be processed, summarized, and validated using Python. These skills will be expanded in future projects involving automated data logging, graphing, and scientific simulations for my Newton's Law of Cooling investigation.


# Project 4 – Temperature Logger
**Date Completed:** 19 July 2026

## Evidence
Repository:
python-projects/project-04-Temperature-Logger.py

## Objective
Develop a Python program that records temperature readings over time and stores them for later analysis. This project serves as a stepping stone toward collecting real experimental data for my Newton's Law of Cooling research.

## Skills Learned
- Read CSV files using Python's built-in csv module.
- Lists
- Loops
- Functions
- User input validation
- Data storage
- Exception handling
- Organising a larger Python program

## Challenges
- Ensuring only valid numerical temperatures were accepted.
- Keeping the program organised as it became more complex.
- Recording multiple readings without losing previous data.

## Reflection
This project introduced me to the fundamentals of data collection, which is essential for scientific programming. I learned how to store and manage measurements in Python and began thinking about how software can support real experiments. These skills will be directly applied when I build my Raspberry Pi Pico temperature monitoring system for my Newton's Law of Cooling investigation.

## Next Objective
Code a program simmiler to the Physics calculator that would allow me to manually input temperature data and apply different functions to it which will enhance my idea of

# Project 5 - Temperarture Plotter
**Date Completed:** 23 July 2026

## Evidence
Repository:
python-projects/project-05-Temperature-Plotter.py

## Objective
Develop a Python program that imports temperature data from a CSV file and visualises it as a graph using Matplotlib. The program should automatically detect the column headings, plot the data, and handle invalid file names gracefully

## Skills Learned
- Use csv.DictReader() to access data by column names.
- Extract column headings automatically using fieldnames.
- Store numerical data from a CSV file into Python lists.
- Convert string data into floating-point numbers for plotting.
- Create line graphs using Matplotlib.
- Label graph axes using the CSV column headers.

## Challenges
- Understanding how csv.DictReader() stores data as dictionaries.
- Extracting values from 
- Preventing the program from crashing when an invalid file name was entered.

## Reflection
This project strengthened my understanding of file handling and data visualisation. Unlike previous projects that relied solely on user input, this program worked with external datasets, making it more representative of real scientific and engineering applications. These skills will be directly applicable to my research project, where experimental temperature data collected from sensors will be stored in CSV files and later analysed and visualised using Python.

## Next Objective
All the past projects have been another stepping stone added to help with the upcoming Newtons cooling Law simulator. Hopefully the next project will allow users to input temperature values, then used to simulate and plot temperature decay through time. 


# Project 6 – Newton's Law of Cooling Simulator
**Date completed** 2 august 2026

## Evidence
Repository:
[Newton's Cooling Law Simulator](Python%20projects/Newton's%20Cooling%20Law%20Simulator.py)

## Objective
To develop a Python program that models Newton's Law of Cooling by calculating the time required for an object to cool to a specified target temperature and visualising the cooling process using a temperature-versus-time graph.

## Skills Learned

- Used **NumPy's** `np.exp()` function to model exponential cooling.
- Used **NumPy's** `np.log()` function to calculate cooling time analytically.
- Created a reusable function with parameters and return values.
- Implemented **input validation** to prevent invalid temperature values.
- Generated simulation time steps using `numpy.arange()`.
- Stored simulated data in Python lists for plotting.
- Produced scientific graphs using **Matplotlib**.
- Combined mathematics, programming, and data visualisation into one application.

## Challenges
- Translating the mathematical equation of Newton's Law of Cooling into Python code.
- Understanding how logarithmic and exponential functions are used in scientific programming.
- Preventing invalid user inputs that would produce impossible results.
- Ensuring the simulation generated temperatures only up to the calculated cooling time.
- Making the graph accurately represent the cooling process.

## Reflection
This project was my first complete scientific simulation. It showed me how mathematical equations can be transformed into working computer programs that model real physical systems. I became more confident using NumPy for scientific calculations and gained a better understanding of how Python can be applied to engineering and physics problems. Completing this project also gave me a solid theoretical foundation for my Newton's Law of Cooling research.

## Next Objective
Develop a program that imports experimental temperature data from CSV files and compares it with the theoretical cooling model. This will allow me to estimate the cooling constant from real experiments and evaluate how accurately Newton's Law of Cooling predicts observed cooling behaviour.




