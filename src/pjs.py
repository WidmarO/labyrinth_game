def warrior_main1():
	matrix = [
		[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,1,2,2,1,0,0,0,0,0,0,0,0,0,0,1,2,5,1,1,0,0,0,0,0,0,0,0],
		[0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0],
		[0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0],
		[0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0],
		[0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,5,1,0,0,0,0,0,0],
		[0,0,1,2,2,5,2,1,0,0,1,1,1,1,1,1,1,1,0,2,1,2,2,2,5,1,0,0,0,0,0,0],
		[0,0,1,2,2,2,5,2,1,5,1,4,4,3,3,3,5,4,1,5,1,2,2,2,2,1,0,0,0,0,0,0],
		[0,0,0,1,2,2,2,2,1,5,1,4,4,4,3,3,3,5,4,2,1,2,2,2,1,0,0,0,0,0,0,0],
		[0,0,0,0,1,1,1,1,1,2,1,4,4,4,3,3,3,5,5,1,1,1,1,1,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,1,1,2,1,4,1,1,1,1,1,1,1,5,1,1,1,1,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,1,4,4,1,1,1,1,1,1,1,5,1,1,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,1,4,4,4,4,3,1,1,4,3,5,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,1,4,4,4,3,5,1,1,3,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,1,3,4,4,3,5,1,1,3,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,3,1,4,4,3,5,1,1,3,5,5,1,1,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,4,3,4,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,3,4,4,1,4,1,5,5,2,2,4,4,1,1,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,1,1,3,1,1,4,1,5,5,2,2,4,4,1,1,1,0,1,1,1,1,1,0,0,0,0],
		[0,0,0,0,0,1,1,1,1,1,1,4,4,1,5,5,2,4,4,1,1,1,1,1,5,5,5,5,1,1,0,0],
		[0,3,3,3,0,1,4,1,2,1,1,3,3,4,1,4,5,4,1,4,1,1,1,4,5,5,5,5,5,5,1,0],
		[0,3,1,3,5,3,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,5,1],
		[0,3,0,4,1,1,1,2,1,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,3,3,3,3,3,5,5,1],
		[0,4,4,1,0,0,0,1,2,1,2,2,2,2,2,5,5,2,2,1,0,0,0,1,5,3,3,5,5,5,1,0],
		[0,1,1,0,0,0,0,0,1,1,1,4,4,1,4,4,4,1,4,1,0,0,0,1,5,5,5,5,1,1,0,0],
		[0,0,0,0,0,0,0,0,0,1,4,3,4,1,3,3,3,1,3,1,0,0,0,1,1,1,1,1,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,1,3,3,1,1,4,4,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,4,1,1,1,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,4,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	]
	return matrix

def warrior_main2():
	matrix = [
		[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,1,2,2,1,0,0,0,0,0,0,0,0,0,0,1,2,5,1,1,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0],
		[0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0],
		[0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0],
		[0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,5,1,0,0,0,0,0,0],
		[0,0,0,1,2,2,5,2,1,0,1,1,1,1,1,1,1,1,1,2,2,1,2,2,2,5,1,0,0,0,0,0,0],
		[0,0,0,1,2,2,2,5,2,1,2,1,4,4,3,3,3,5,3,1,2,1,2,2,2,2,1,0,0,0,0,0,0],
		[0,0,0,0,1,2,2,2,2,1,2,1,4,4,4,3,3,3,5,3,1,1,2,2,2,1,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,1,1,1,1,2,1,4,4,4,3,3,3,5,5,1,1,1,1,1,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,1,1,2,1,4,1,1,1,1,1,1,1,5,1,1,1,1,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,1,1,4,4,1,1,1,1,1,1,1,5,1,1,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,1,4,4,4,4,3,1,1,4,3,5,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,1,4,4,4,3,5,1,1,3,5,5,1,1,1,1,0,0,0,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,1,1,3,3,4,3,5,1,1,3,5,5,1,3,4,4,1,0,1,4,0,0,0,0,0],
		[0,0,0,0,0,0,1,4,3,3,1,3,4,3,5,1,1,3,5,5,1,3,4,1,1,0,1,4,0,0,0,0,0],
		[0,0,0,0,0,0,3,4,3,3,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,4,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,3,4,4,1,3,1,5,5,2,2,4,4,4,1,1,1,1,1,1,4,0,0,0,0,0,0],
		[0,0,0,0,0,4,1,1,2,1,4,3,1,5,5,2,2,4,4,4,1,1,1,1,1,1,1,1,0,0,0,0,0],
		[0,0,0,0,4,1,1,1,1,1,1,4,4,1,5,5,2,4,4,4,1,1,3,5,5,5,5,5,1,1,0,0,0],
		[3,3,0,4,1,1,1,2,0,1,1,4,3,3,1,1,5,2,4,1,4,1,4,5,5,5,5,5,5,5,1,0,0],
		[3,1,3,5,3,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,5,1,0],
		[3,0,4,1,1,1,2,1,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,3,3,3,3,3,3,5,5,1,0],
		[4,4,1,0,0,0,1,2,0,0,0,1,2,2,2,2,2,2,5,5,1,0,3,5,3,3,3,3,5,5,1,0,0],
		[1,1,0,0,0,0,0,1,1,0,1,1,4,4,1,1,4,4,4,1,1,4,4,5,5,5,5,5,1,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,3,3,4,1,1,1,3,3,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,4,1,1,1,1,1,1,1,4,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,4,4,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,4,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	]
	return matrix

def warrior_main3():
	matrix = [
		[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,1,2,2,1,0,0,0,0,0,0,0,0,0,0,1,2,5,1,1,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0],
		[0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0],
		[0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0],
		[0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,5,1,0,0,0,0],
		[0,0,0,0,0,1,2,2,5,2,1,0,0,1,1,1,1,1,1,1,1,0,0,1,2,2,2,5,1,0,0,0,0],
		[0,0,0,0,0,1,2,2,2,5,2,1,5,1,4,4,3,3,3,5,3,1,5,1,2,2,2,2,1,0,0,0,0],
		[0,0,0,0,0,0,1,2,2,2,2,1,5,1,4,4,4,3,3,3,5,3,2,1,2,2,2,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,1,1,1,1,2,1,4,4,4,3,3,3,5,5,1,1,1,1,1,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,1,1,1,2,1,4,1,1,1,1,1,1,1,5,1,1,1,1,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,1,4,4,1,1,1,1,1,1,1,5,1,1,0,0,0,1,1,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,3,1,1,4,3,5,1,0,0,0,0,1,1,5,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,3,5,1,1,3,5,5,1,1,1,0,0,0,1,4,0,0,0],
		[0,0,0,0,0,0,0,0,1,1,1,1,3,3,4,3,5,1,1,3,5,5,1,3,4,1,1,0,1,4,0,0,0],
		[0,0,0,0,0,0,0,1,3,4,3,3,1,3,4,3,5,1,1,3,5,5,1,3,4,4,1,1,1,4,0,0,0],
		[0,0,0,0,0,0,1,1,3,4,3,3,4,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,4,0,0,0],
		[0,0,0,0,0,4,1,1,1,3,1,4,1,3,1,5,5,2,2,4,4,4,1,1,1,1,1,1,1,0,0,0,0],
		[0,0,0,0,4,1,0,0,1,1,1,1,4,3,1,5,5,2,2,4,4,4,1,3,5,5,5,5,5,1,1,0,0],
		[0,3,3,0,4,1,0,1,2,0,0,1,1,4,4,1,5,5,2,4,4,1,1,4,5,5,5,5,5,5,5,1,0],
		[0,3,1,3,5,3,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,5,1],
		[0,3,0,4,1,1,1,2,1,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,3,3,3,3,3,3,5,5,1],
		[0,4,4,1,0,0,0,1,2,0,0,0,0,1,1,1,1,1,1,1,1,1,1,3,5,3,3,3,5,5,5,1,0],
		[0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,2,2,2,2,5,5,2,1,4,5,5,5,5,5,1,1,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,1,4,4,1,1,4,4,4,1,1,1,1,1,1,1,1,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,4,1,1,1,3,3,1,1,1,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,4,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,4,1,1,1,1,0,0,1,1,1,1,4,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,4,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,0,0,0,0,0,0,0,0],
	]
	return matrix

def warrior_main4():
	matrix = [
		[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,1,2,2,1,0,0,0,0,0,0,0,0,0,0,1,2,5,1,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0],
		[0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0],
		[0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0],
		[0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,5,1,0,0,0,0,0,0,0,0],
		[0,0,1,2,2,5,2,1,0,1,1,1,1,1,1,1,1,1,2,2,1,2,2,2,5,1,0,0,0,0,0,0,0,0],
		[0,0,1,2,2,2,5,2,1,2,1,4,4,3,3,3,5,3,1,5,1,2,2,2,2,1,0,0,0,0,0,0,0,0],
		[0,0,0,1,2,2,2,2,1,2,1,4,4,4,3,3,3,5,3,2,1,2,2,2,1,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,1,1,1,1,2,1,4,4,4,3,3,3,5,5,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,1,1,2,1,4,1,1,1,1,1,1,1,5,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,1,4,4,1,1,1,1,1,1,1,5,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,1,4,4,4,4,3,1,1,4,3,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,1,4,4,4,3,5,1,1,3,5,5,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,1,1,3,3,4,3,5,1,1,3,5,5,1,3,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,4,3,3,1,3,4,3,5,1,1,3,5,5,1,4,4,1,0,0,1,1,0,0,0,0,0,0,0],
		[0,0,0,0,1,4,4,3,3,4,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,5,0,0,0,0,0,0,0],
		[0,0,0,0,1,3,4,4,4,1,3,1,5,5,2,2,4,4,4,1,2,1,1,1,1,4,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,1,3,3,1,4,3,1,5,5,2,2,4,4,4,1,1,1,1,1,4,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,2,1,1,1,4,1,5,5,2,2,4,4,4,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,4,1,0,0,1,1,4,4,1,5,5,2,4,4,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0],
		[0,0,0,0,4,1,0,0,0,1,1,3,3,1,1,5,4,1,1,1,0,0,0,3,5,5,5,5,5,1,1,0,0,0],
		[0,5,5,0,4,1,0,1,2,1,1,3,3,4,4,1,1,4,1,1,0,0,0,4,5,5,5,5,5,5,5,1,0,0],
		[0,5,1,3,5,3,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,5,1,0],
		[0,5,0,4,1,1,1,2,1,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,3,3,3,3,3,3,5,5,1,0],
		[0,4,4,1,0,0,0,1,2,1,3,3,1,1,3,3,3,1,3,1,0,0,0,3,5,3,3,3,5,5,5,1,0,0],
		[0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,4,5,5,5,5,5,1,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,4,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,4,1,1,1,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,4,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],		
	]
	return matrix
	def warrior_main5():
	matrix = [
		[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,1,2,2,1,0,0,0,0,0,0,0,0,0,0,1,2,5,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,2,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,5,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,2,2,5,2,1,0,1,1,1,1,1,1,1,1,1,2,2,1,2,2,2,5,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,2,2,2,5,2,1,2,1,4,4,3,3,3,5,3,1,5,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,1,2,2,2,2,1,2,1,4,4,4,3,3,3,5,3,2,1,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,1,1,1,1,2,1,4,4,4,3,3,3,5,5,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,1,1,2,1,4,1,1,1,1,1,1,1,5,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,1,4,4,1,1,1,1,1,1,1,5,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,4,4,4,4,3,1,1,4,3,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,4,4,4,3,5,1,1,3,5,5,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,1,1,3,3,5,1,1,3,5,5,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,3,3,1,3,5,1,1,3,5,5,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,4,4,4,4,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,3,3,4,1,1,5,5,2,2,4,4,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
		[0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,4,4,1,0,0,0,0,0,0,0,0,3,5,5,5,5,5,1,1,0,0],
		[0,0,0,0,3,3,1,4,1,1,1,2,1,5,2,4,4,1,0,1,1,0,0,0,0,0,4,5,5,5,5,5,5,5,1,0],
		[0,0,0,0,3,1,3,5,3,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,5,1],
		[0,0,0,0,3,0,4,1,1,1,2,1,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,3,3,3,3,3,3,5,5,1],
		[0,0,0,0,4,4,1,0,0,1,1,2,1,1,1,1,1,1,0,0,0,0,0,0,0,0,3,5,3,3,3,5,5,5,1,0],
		[0,0,0,0,1,1,0,1,1,4,1,1,2,2,5,5,2,1,0,0,0,0,0,0,0,0,4,5,5,5,5,5,1,1,0,0],
		[0,0,0,0,0,0,0,1,4,4,1,1,4,4,3,1,4,3,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
		[0,0,0,0,0,0,1,1,1,1,1,4,3,3,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,4,1,1,1,1,1,1,1,0,0,1,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,4,0,1,4,3,1,0,0,0,0,0,1,1,1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],		
	]
	return matrix

def princesa():
	matrix = [
		[0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,],
		[0,0,0,1,2,1,2,1,2,1,0,0,0,0,0,0,0,0,0,],
		[0,0,0,1,4,2,1,2,4,1,1,0,0,0,0,0,0,0,0,],
		[0,0,1,2,1,1,1,1,1,2,2,1,1,0,0,0,0,0,0,],
		[0,0,1,2,2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,],
		[0,1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,0,0,],
		[0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0,0,],
		[1,2,2,1,1,2,2,1,1,2,2,2,2,2,2,1,0,0,0,],
		[1,2,2,1,3,1,1,3,1,1,2,2,2,2,2,2,1,0,0,],
		[0,1,1,3,1,3,3,1,3,3,1,1,1,2,2,1,0,0,0,],
		[0,0,1,3,1,3,3,1,3,3,1,3,1,2,2,1,0,0,0,],
		[0,0,1,3,3,3,3,3,3,3,1,3,1,2,2,2,1,0,0,],
		[0,0,1,3,3,3,3,3,3,3,3,4,2,2,2,2,2,1,0,],
		[0,1,1,1,3,7,7,3,3,3,1,2,2,2,2,2,2,1,0,],
		[0,1,2,1,1,3,3,3,3,3,1,2,2,2,2,2,1,0,0,],
		[0,0,1,1,1,4,4,1,1,1,1,1,1,1,2,2,2,1,0,],
		[0,1,4,4,4,4,4,4,4,4,4,4,4,4,1,2,2,1,0,],
		[0,1,4,4,4,4,6,4,4,4,4,4,4,4,1,2,2,1,0,],
		[0,1,1,1,4,6,4,6,4,1,1,1,1,1,2,2,1,0,0,],
		[0,1,3,1,4,6,4,6,4,1,3,3,1,2,2,1,0,0,0,],
		[0,1,1,3,1,4,6,4,4,1,3,3,1,2,2,2,1,0,0,],
		[0,1,3,3,1,4,4,4,1,3,1,3,1,1,1,1,0,0,0,],
		[0,1,1,3,1,4,1,1,3,3,3,1,5,1,0,0,0,0,0,],
		[0,0,1,3,3,1,3,3,3,1,1,5,5,1,0,0,0,0,0,],
		[0,0,1,1,3,1,3,3,1,1,5,5,5,5,1,0,0,0,0,],
		[0,1,5,5,1,1,1,1,4,4,4,5,5,5,1,0,0,0,0,],
		[0,1,5,4,4,4,4,4,4,4,4,4,5,5,5,1,0,0,0,],
		[0,1,4,4,4,4,4,4,4,4,4,4,4,4,5,1,0,0,0,],
		[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,0,],
		[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,0,0,],
		[1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,0,0,],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,]
	]
	return matrix

def drakai():
	matrix = [
   	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0],
		[0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0],
		[0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0],
		[0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
		[0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0],
		[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0],
		[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0],
		[0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0],
		[0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0],
		[0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0],
		[0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0],
		[0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
		[0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0],
		[0,1,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0],
		[0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,0,0,0,0],
		[0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	]

def muerte(x, y, r, g, b, size):
	matrix = [
   	[0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,3,3,3,3,3,3,3,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,3,3,3,3,3,3,3,3,3,3,3,3,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,3,3,3,3,3,3,3,3,3,3,3,3,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
    [0,1,3,3,3,3,3,3,3,3,3,3,3,3,1,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0],
    [1,0,0,1,1,1,1,1,1,3,3,3,3,3,3,1,0,0,0,1,0,0,1,2,2,2,1,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,1,3,3,3,3,3,3,1,0,0,1,0,0,1,2,2,2,2,1,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,1,3,3,3,3,3,1,0,0,1,0,1,2,2,2,2,2,2,1,1,0,0],
    [1,0,1,1,0,0,1,1,1,0,0,1,3,3,3,3,1,0,1,0,1,1,1,1,2,2,2,2,1,1,0,0],
    [1,1,2,1,0,0,1,2,1,1,0,0,1,3,3,3,1,0,1,0,1,0,0,0,1,1,2,2,2,1,0,0],
    [1,1,1,1,0,0,1,1,1,1,0,0,1,3,3,3,1,0,1,0,1,0,0,0,0,0,1,2,2,1,0,0],
    [1,1,1,0,0,0,0,1,1,1,0,0,1,3,3,3,1,0,1,0,1,0,0,0,0,0,1,2,2,1,0,0],
    [1,0,0,0,1,1,0,0,0,0,0,0,1,3,3,3,3,1,1,1,0,0,0,0,0,0,0,1,2,1,0,0],
    [1,0,0,0,1,1,0,0,0,0,0,1,3,3,3,3,1,1,1,1,0,0,0,0,0,0,0,1,2,1,0,0],
    [1,0,1,0,0,0,0,0,1,0,1,3,3,3,3,3,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0],
    [1,0,1,0,1,0,1,0,1,0,1,3,3,3,3,3,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
    [1,0,1,0,1,0,1,0,1,0,1,3,3,3,3,3,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,1,1,0,1,0,1,0,1,1,3,3,3,3,3,1,1,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
    [0,0,1,0,1,0,1,0,1,3,3,3,3,3,1,1,1,1,0,0,0,0,0,0,0,0,0,2,2,2,0,0],
    [0,0,0,1,1,1,1,1,3,3,3,3,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0],
    [0,0,0,0,0,1,3,3,3,3,3,3,1,0,0,0,1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0],
    [0,0,0,0,0,1,3,3,3,3,3,3,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
    [0,0,0,0,0,1,3,3,3,3,3,3,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
    [0,0,0,0,1,3,3,3,3,3,3,1,1,3,3,3,3,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0],
    [0,0,0,0,1,3,3,3,3,3,1,1,1,3,3,3,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,3,3,3,3,3,1,1,1,3,3,3,3,3,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,3,3,3,3,3,1,1,3,3,3,3,3,3,3,3,1,0,0,0,0,1,1,1,0,0,0,0,0],
    [0,0,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,0,0,0,0,0,0,0],
    [0,0,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,0,0,0,0,0,0,0,0,0],
    [0,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,0,0,0,0,0,0,0,0,0],
    [0,1,3,3,1,1,3,3,1,1,3,3,3,3,1,1,3,3,3,3,1,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],	
	]
	return matrix

def piso1():
	
	matrix=[
		[1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,1],
		[1,1,1,1,1,1,1,1,3,2,2,2,3,1,1,1,1,1,1,1,1,3,3,3,1,1],
		[1,1,1,1,1,1,1,1,1,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,2,2,2,2,2,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1],	
		[2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1],
		[2,2,2,2,2,2,2,1,1,1,1,1,1,3,2,2,2,3,1,1,1,1,1,1,1,1],
		[2,2,2,2,2,2,2,1,1,1,1,1,1,1,3,3,3,1,1,1,1,1,1,1,1,1],
		[3,2,2,2,2,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,1,1],
		[1,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,3,1,1,3,2,2,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[2,2,2,1,1,3,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[2,2,2,2,1,3,1,1,1,3,3,3,1,1,1,2,2,2,1,1,1,1,1,1,1,2],
		[2,2,2,3,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,3,2],
		[3,3,3,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,1,1,1,1,3,2],
		[1,1,1,1,1,1,3,3,1,1,1,1,1,1,3,2,2,2,2,2,3,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,3,3,3,3,3,1,1,1,1,1,1],
		[3,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,3,3],
		[1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1],
		[1,3,2,2,2,2,3,1,1,2,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,1],
		[1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,1],
	]
	return matrix

def Pared1():
	#color_0=rgb(140, 156, 179)
	#color_1=rgb(193, 203, 224)
	#color_2=rgb(47, 60, 87)
	#color_3=rgb(91, 106, 133)
	matrix=[
		[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1],
		[0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0],
		[3,3,3,3,3,3,3,3,2,3,0,0,0,0,0,0,1,2,3,3,3,3,3,3,3,3],
		[2,2,2,2,2,2,2,2,2,3,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2],
		[1,1,1,1,1,1,1,1,2,3,0,0,0,0,0,0,1,2,1,1,1,1,1,1,1,1],
		[0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0],
		[3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,1,2,3,3,3,3,3,3,3,3],
		[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0,0,0,0,0,0],
	]

	return matrix


# def troll(): # tamanio 46 * 50
# 	matrix = [		
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,2,2,1,1,1,0,0,0,0,0,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,2,0,0,0,0,0,0,1,0,0,0,0,3,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,3,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
# 		[0,1,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,3,3,3,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,1,2,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0,1,1,2,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,4,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,4,4,0,0,0,0,0,0,1,0,0,0,0,0,0,1,4,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,1,4,4,4,4,4,4,4,4,4,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
# 		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# 	]

def Soldado1():
	matrix = [
		[0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,4,4,4,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
		[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
		[0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
		[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
		[0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0],
		[1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0],
		[1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0],
		[1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
		[1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
		[1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0],
		[0,1,0,0,0,0,0,1,3,3,3,3,1,1,1,1,1,0,0,0],
		[0,1,1,1,1,1,1,3,0,0,0,1,4,4,4,0,0,0,0,0],
		[0,1,0,1,0,0,1,0,0,0,0,0,1,4,4,4,0,0,0,0],
		[0,1,0,1,0,0,1,1,1,1,1,1,1,0,4,4,4,0,0,0],
		[0,1,0,1,0,0,0,1,3,3,3,1,0,0,4,4,4,0,0,0],
		[0,1,0,1,0,0,0,1,3,3,3,1,0,0,4,4,4,0,0,0],
		[0,1,0,0,1,1,1,1,1,1,1,1,1,1,4,4,4,4,0,0],
		[0,1,0,0,1,4,1,0,0,0,0,1,4,1,4,4,4,4,0,0],
		[0,1,0,0,1,1,1,0,0,0,0,1,1,1,4,4,4,4,0,0],
		[0,1,0,1,0,0,1,0,0,0,0,1,0,0,1,4,4,4,4,0],
		[0,1,0,1,1,1,1,3,1,1,1,1,1,1,1,4,4,4,4,0],
		[0,1,0,0,1,0,1,3,3,3,3,1,4,4,4,4,4,4,4,0],
		[0,1,0,1,0,0,1,3,3,3,3,1,4,4,4,4,4,4,4,0],
		[0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,4,4,4,4,0],
		[0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],

    ]

    return matrix