TO RUN:
0. Python 2.7/3 must be installed on your system
1. Open a console in this directory
2. Run the main script: python main.py "./inputs/input0.txt"
3. Run the unittest script: python test_rover_unittest.py

DESIGN DECISIONS:

A) Given the format of the sample input provided in the problem statement, I assumed that a grid can only be as large as (9,9). 
Without a delimiter to separate the horizontal and vertical coordinate, the coordinates are only differentiable if they consist of single-digit coordinates.

B) The rover must remain within the boundaries for safe exploration. 
Therefore, if the instructions provided cause the rover to go out of bounds at any point, the rover will not execute the movement instructions, and will remain at the starting location.
Note that this means even if the final resulting coordinate is within bounds, so long as the rover goes out of bounds in the process leading up to the final result, then the rover will not execute the motion.
