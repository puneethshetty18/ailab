import math
import random
MIN,MAX= -1000,1000
def MINMAX(depth,nodeIndex,maximizingPlayer,values,alpha,beta):
	if depth==3:
		return values[nodeIndex]
	if maximizingPlayer:
		best=MIN
		for i in range(0,2):
			val = MINMAX(depth+1,nodeIndex*2+i,False,values,alpha,beta)
			best=max(best,val)
			alpha=max(alpha,best)
			if beta<=alpha:
				break
		return best
	else:
		best=MAX
		for i in range(0,2):
			val = MINMAX(depth+1,nodeIndex*2+i,True,values,alpha,beta)
			best=min(best,val)
			alpha=min(alpha,best)
			if beta<=alpha:
				break
		return best
values = random.sample(range(1, 50), 8)
print(str(values))
print("Optimal value:",MINMAX(0,0,True,values,MIN,MAX))
