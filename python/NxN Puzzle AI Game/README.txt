I created an AI agent to solve the n-puzzle game. You may visit "mypuzzle.org/sliding" to see the rules.

I compiled my program using a version of python 2.7.X. To execute the program run:

$ python driver.py <method argument> <board argument>

The <method argument> can be one of the following: 
<bfs> (Breadth-First Search)
<dfs> (Depth-First Search)
<ast> (A-Star Search)
<ida> (IDA-Star Search)

The <board argument> will be a comma-separated list of integers containing no spaces. It must be 
of length NxN array for there to be no compile errors, 0 must be included for that will be the empty
space in the board. 

For example, to use the bread-first search strategy to solve a 3X3 board, the input board would be
given by the starting configuration {0,8,7,6,5,4,3,2,1}, the program will be executed like so (with no
spaces between commas):

$ python driver.py bfs 0,8,7,6,5,4,3,2,1

The program will write out to an output.txt file with the following statistics:

path_to_goal: the sequence of moves taken to reach the goal
cost_of_path: the number of moves taken to reach the goal
nodes_expanded: the number of nodes that have been expanded
fringe_size: the size of the frontier set when the goal node is found
max_fringe_size: the maximum size of the frontier set in the lifetime of the algorithm
search_depth: the depth within the search tree when the goal node is found
max_search_depth: the maximum depth of the search tree in the lifetime of the algorithm
running_time: the total running time of the search instance, reported in seconds
max_ram_usage: the maximum RAM usage in the lifetime of the process as measured by
the ru_maxrss attribute in the resource module, reported in megabytes