from ant_colony import Ant_colony 
test_nodes = {0: (0, 17), 1: (3, 9), 2: (12, 4), 3: (14, 11), 4: (8, 11), 5: (15, 6), 6: (6, 45), 7: (15, 9), 8: (12, 10), 9: (10, 70)}
n=10
#n = int(input("enter the number of processes"))
	# test_nodes={}
	# print("Enter the arriving time and burst time of all the process")
	# for i in range(n):
	# 	temp=raw_input().split(",")
	# 	test_nodes[i]=(int(temp[0]),int(temp[1]))

def distance(start, end):
	x_distance = abs(start[0] - end[0])
	y_distance = abs(start[1] - end[1])
	
	import math
	return math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))

# we can make a colony of ants...
colony = Ant_colony(test_nodes, distance)

#that will find the optimal solution with ACO
answer = colony.mainloop()
print("**************************************")
print("The optimal sequence is : ")
print(answer)


def waitingTime(i):
	t=0
	time=0
	total=0
	for j in range(n):
		if time<test_nodes[answer[t]][0]:
			time=test_nodes[answer[t]][0]
		temp=time-test_nodes[answer[t]][0]
		print "waiting time for process ",t ," is ",temp
		time +=test_nodes[answer[t]][1]
		total+=temp
		t+=1
	return total

def turnAroundTime():
	t=0
	time=0
	total=0
	for j in range(n):
		if time<test_nodes[answer[t]][0]:
			time=test_nodes[answer[t]][0]
		temp=time-test_nodes[answer[t]][0]+test_nodes[answer[t]][1]
		print "turn around time of process ",t," is " ,temp
		time +=test_nodes[answer[t]][1]
		total+=temp
		t+=1
	
	return total

avgWaitingTime = waitingTime(0)/n
print("**************************************")
print("average waiting time :")
print(avgWaitingTime)
print("**************************************")
avgTurnAround = turnAroundTime()/n
print("**************************************")
print("average turn around time :")
print(avgTurnAround)
