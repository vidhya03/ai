from node import *
from Queue import *
from heapq import *
from copy import deepcopy
import math

def goalTest(node):
	if(node.state == goalBoardTest):
		return True

	return False

def initialize(lst):

	global goalBoardTest
	global N
	
	N = int(math.sqrt(len(lst)))
	goalBoardTest = tuple(range(N*N))
	
	return goalBoardTest


#Implemented algorithm from stack
#http://stackoverflow.com/questions/12526792/manhattan-distance-in-a
def manhattanCostFunction(state):
	cost = 0
	manhattanDistanceSum = 0
	row = 0
	column = 0


	while row<N:
		column = 0
		while column < N:
			position = row*N
			position += column
			value = state.index(position); # tiles array contains board elements
			if (value != 0): # we don't compute MD for element 0
				targetRow = (value ) / N; # expected x-coordinate (row)
				targetColumn = (value ) % N; # expected y-coordinate (col)
				dx = row - targetRow; # x-distance to expected coordinate
				dy = column - targetColumn; # y-distance to expected coordinate
				manhattanDistanceSum += math.fabs(dx) + math.fabs(dy); 
			column+=1
		row+=1
	cost = manhattanDistanceSum
	return cost


def expand_nodes(node):

	neighbors = []
	state = node.state
	depth = node.depth
	i = int(state.index(0))

	newState = move_up(i, state)
	newNodeUp = create_node(newState, node, "Up", depth+1, 0)
	neighbors.append(newNodeUp)

	newState = move_down(i, state)
	newNodeDown = create_node(newState, node, "Down", depth+1, 0)
	neighbors.append(newNodeDown)

	newState = move_left(i, state)
	newNodeLeft = create_node(newState, node, "Left", depth+1, 0)
	neighbors.append(newNodeLeft)

	newState = move_right(i, state)
	newNodeRight = create_node(newState, node, "Right", depth+1, 0)
	neighbors.append(newNodeRight)

	neighbors = [node for node in neighbors if node.state != None] 
	return neighbors

def expand_nodes_reverse_ida(node):

	neighbors = []
	state = node.state
	depth = node.depth
	i = int(state.index(0))

	newStateRight = move_right(i, state)
	if(newStateRight != None):
		newCostRight = manhattanCostFunction(newStateRight)
		newNodeRight = create_node(newStateRight, node, "Right", depth+1, newCostRight)
		neighbors.append(newNodeRight)

	newStateLeft = move_left(i, state)
	if(newStateLeft != None):
		newCostLeft = manhattanCostFunction(newStateLeft)
		newNodeLeft = create_node(newStateLeft, node, "Left", depth+1, newCostLeft)
		neighbors.append(newNodeLeft)

	newStateDown = move_down(i, state)
	if(newStateDown != None):
		newCostDown = manhattanCostFunction(newStateDown)
		newNodeDown = create_node(newStateDown, node, "Down", depth+1, newCostDown)
		neighbors.append(newNodeDown)

	newStateUp = move_up(i, state)
	if(newStateUp != None):
		newCostUp = manhattanCostFunction(newStateUp)
		newNodeUp = create_node(newStateUp, node, "Up", depth+1, newCostUp)
		neighbors.append(newNodeUp)

	neighbors = [node for node in neighbors if node.state != None] 
	return neighbors



def expand_nodes_ast(node):

	neighbors = []
	state = node.state
	depth = node.depth
	i = int(state.index(0))

	newStateUp = move_up(i, state)
	if(newStateUp != None):
		newCostUp = manhattanCostFunction(newStateUp)
		newNodeUp = create_node(newStateUp, node, "Up", depth+1, newCostUp)
		neighbors.append(newNodeUp)

	newStateDown = move_down(i, state)
	if(newStateDown != None):
		newCostDown = manhattanCostFunction(newStateDown)
		newNodeDown = create_node(newStateDown, node, "Down", depth+1, newCostDown)
		neighbors.append(newNodeDown)

	newStateLeft = move_left(i, state)
	if(newStateLeft != None):
		newCostLeft = manhattanCostFunction(newStateLeft)
		newNodeLeft = create_node(newStateLeft, node, "Left", depth+1, newCostLeft)
		neighbors.append(newNodeLeft)

	newStateRight = move_right(i, state)
	if(newStateRight != None):
		newCostRight = manhattanCostFunction(newStateRight)
		newNodeRight = create_node(newStateRight, node, "Right", depth+1, newCostRight)
		neighbors.append(newNodeRight)

	neighbors = [node for node in neighbors if node.state != None] 
	return neighbors


def expand_nodes_reverse(node):

	neighbors = []
	state = node.state
	depth = node.depth

	i = state.index(0)

	newStateRight = move_right(i, state)
	newNodeRight = create_node(newStateRight, node, "Right", depth+1, 0)
	neighbors.append(newNodeRight)

	newStateLeft = move_left(i, state)
	newNodeLeft = create_node(newStateLeft, node, "Left", depth+1, 0)
	neighbors.append(newNodeLeft)

	newStateDown = move_down(i, state)
	newNodeDown = create_node(newStateDown, node, "Down", depth+1, 0)
	neighbors.append(newNodeDown)

	newStateUp = move_up(i, state)
	newNodeUp = create_node(newStateUp, node, "Up", depth+1, 0)
	neighbors.append(newNodeUp)

	neighbors = [node for node in neighbors if node.state != None] 

	return neighbors


def create_node( state, parent, direction, depth, cost ):
	return Node( state, parent, direction, depth, cost )


def move_up(i, state):  
	if i-N>=0:
		changed_state = list(deepcopy(state))

		changed_state[i]= state[i-N]
		changed_state[i-N]=state[i]
		
		return tuple(changed_state)

	return None

def move_down(i, state):  

	if i+N<N*N:
		changed_state = list(deepcopy(state))

		changed_state[i]= state[i+N]
		changed_state[i+N]=state[i]
		
		return tuple(changed_state)

	return None 

def move_left(i, state):
	
	if i%N != 0:
		changed_state = list(deepcopy(state))

		changed_state[i]= state[i-1]
		changed_state[i-1]=state[i]
		
		return tuple(changed_state)

	return None 

def move_right(i, state):

	if (i+1)%N != 0:
		changed_state = list(deepcopy(state))

		changed_state[i]= state[i+1]
		changed_state[i+1]=state[i]
		
		return tuple(changed_state)

	return None 
