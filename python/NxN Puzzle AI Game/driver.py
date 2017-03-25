import sys
import time
import os
import time
from time import clock
from search_algo import search_algorithms


start = time.time()

#process = psutil.Process(os.getpid())
#_1stmemory = process.memory_info().rss

#list1 = "1,2,5,3,4,0,6,7,8"

#goal = ida(list1)


if(sys.argv[1]=="bfs"):
	print("bfs")
	#from searchAlgorithms import bfs
	goal = search_algorithms.bfs(sys.argv[2])
elif(sys.argv[1]=="dfs"):
	print("dfs")
	#from searchAlgorithms import dfs
	goal = search_algorithms.dfs(sys.argv[2])
elif(sys.argv[1]=="ast"):
	print("ast")
	#from searchAlgorithms import ast
	goal = search_algorithms.ast(sys.argv[2])
elif(sys.argv[1]=="ida"):
	print("ida")
	#from searchAlgorithms import ida
	goal = search_algorithms.ida(sys.argv[2])




max_fringe_size = goal[1]
fringe_size = goal[2]
max_search_depth = goal[3]
nodes_expanded = goal[4]

path_to_goal = []
node = goal[0]
while node.parent != None:
	path_to_goal.insert(0, node.direction)
	node = node.parent


end = time.time()

running_time = end - start

memory = 0
#resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000

print("path_to_goal: ", path_to_goal)
print("cost_of_path: ", goal[0].depth)
print("nodes_expanded: ", nodes_expanded)
print("fringe_size: ", fringe_size)
print("max_fringe_size: ", max_fringe_size)
print("search_depth: ", goal[0].depth)
print("max_search_depth: ", max_search_depth)
print("running_time: ", running_time)
print("max_ram_usage: ", memory)


string = ""
string += 'path_to_goal: '+ str(path_to_goal)+'\n'
string += 'cost_of_path: '+ str(goal[0].depth)+'\n'
string += 'nodes_expanded: '+ str(nodes_expanded)+'\n'
string += 'fringe_size: '+ str(fringe_size)+'\n'
string += 'max_fringe_size: '+ str(max_fringe_size)+'\n'
string += 'search_depth: '+ str(goal[0].depth)+'\n'
string += 'max_search_depth: '+str(max_search_depth)+'\n'
string += 'running_time: '+ str(running_time)+'\n'
string += 'max_ram_usage: '+ str(memory)

file = open('output.txt', 'w')
file.write(string)

file.close()
