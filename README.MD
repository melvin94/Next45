# Mars Rover
A basic implementation of a navigation system for a Mars Rover.

# Project Setup 
There are no package dependencies in this project, other than a requirement for Python 3. To run the scripts in this project:
1. Open a console in this directory
2. Run the main script:
    ```shell
    python main.py --input-path "inputs/input0.txt"
    ```
3. Run the unittest script:
    ```shell
    python test_rover_unittest.py
    ```

# Project Assumptions:
1. A predefined grid is established as the `safe zone` for exploration.
2. Navigation coordinates are provided in single characters.
3. The rover maps out its path before moving.
4. The `safe zone` grid is 2-dimensional, viewed from top-down.
5. The rover navigates by moving 1 block at a time, in either a horizontal or vertical direction.
6. The rover navigates turning in a clockwise manner.
7. If the path causes the rover to exit the `safe zone` at any point in its predfined path, the rover will not move.
8. The rover receives its instructions from a text file, in the following format:
    ```
    WH
    XY Z
    MLR...
    ```
    - `WH` refers to the grid size of the `safe zone`, where `W` is the total number of horizontal blocks on the grid, and `H` is the total number of vertical blocks on the grid. Because of assumption `2` above, the grid cannot be larger than 10 blocks, where `0` refers to the first block coordinate in either direction. 
        ```
        0 <= W <= 9
        0 <= H <= 9
        ```
    - `XY` refers to the starting block coordinates on the grid for the rover, where `X` is the horizontal positional coordinate along the grid, and `Y` is the vertical positional coordinate along the grid. The starting `(X, Y)` coordinate of the rover must be within the `safe zone`.
        ```
        0 <= X <= W
        0 <= Y <= H
        ```
    - `Z` refers to the starting orientation of the rover. This indicates in which direction or orientation the rover is initially facing. The valid orientations of the rover are limited to:
        - `N` (North)
        - `E` (East)
        - `S` (South)
        - `W` (West)
    - `MLR...` refers to the movement instructions for the rover. The valid instructions are:
        - `M` (Move) Move the rover one block in the direction it is currently facing.
        - `L` (Left) Turn left, or rotate the rover anticlockwise by one orientation.
        - `R` (Right) Turn right, or rotate the rover clockwise by one orientation.
    - A sample instruction file:
        ```
        56
        23 N
        MMLMRMM
        ```
        This sample instruction means the following:
        - The `safe zone` grid is (5x6) blocks in size.
        - The starting grid coordinate of the rover is (2, 3).
        - The starting orientation of the rover is North-facing.
        - The movement instructions are as follows:
            - Move one block North.
            - Move one block North.
            - Left turn or rotate anti-clockwise (now facing West).
            - Move one block West.
            - Right turn or rotate clockwise (now facing North).
            - Move one block North.
            - Move one block North.