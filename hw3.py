import pandas as pd

file = pd.read_csv("cmg.csv")

#print(type(file["Return"].get(1)))

file['True Label'] = ''

#a = file.iloc[[0]]
#print(a)

#file.at[0, "True Label"] = "+"

#a = file.iloc[-5:]

#print(len(file.index))


# Question 1.1 ==========================================================================================================
i = 0
file_length = len(file.index)
while i < file_length:
	r_balance = file["Return"].get(i)
	if r_balance < 0:
		file.at[i, "True Label"] = "-"
	else:
		file.at[i, "True Label"] = "+"
	i += 1


# Question 1.2 ==========================================================================================================
#test = file["Date"].get(0)
#print(test.split("/")[2])
#if test.split("/")[2] == "17":
#	print("yuh")
i = 0
l_val = 0
l_pos = 0
l_neg = 0
while i < file_length:
	temp = file["Date"].get(i)
	if temp.split("/")[2] == "20":
		i = file_length
	else:
		l_val += 1
	if file["True Label"].get(i) == "+":
		l_pos += 1
	elif file["True Label"].get(i) == "-":
		l_neg += 1
	i += 1

print("The probability that the first day of year 4 will be an up day is " + 
	str(round((l_pos/l_val) * 100, 2)) + "%")



# Question 1.3 & 1.4 ====================================================================================================

def q13(symbol):
	# Below is k value followed by total pattern found then pos pattern found
	k = [[1, 0, 0], [2, 0, 0], [3, 0, 0]]

	k_step = 0
	while k_step < len(k):
		i = k[k_step][0]
		while i < file_length:
			temp = file["Date"].get(i)
			if temp.split("/")[2] == "20":
				i = file_length
			found_pat = True
			prev = i - 1


			while i - prev < k[k_step][0] + 1:
				if file["True Label"].get(prev) == symbol:
					found_pat = False
				prev -= 1
			if found_pat:
				k[k_step][1] += 1
				if file["True Label"].get(i) == "+":
					k[k_step][2] += 1
			# if the k previous elements are "-"
				# add one to total pattern found for this k
				# if next is "+"
					# add one to pos pattern for this k
			i += 1
		k_step += 1
	return k

k = q13("-")
print("For the down day patterns, k = 1, there is a " + str( round((k[0][2]/k[0][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the down day patterns, k = 2, there is a " + str( round((k[1][2]/k[1][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the down day patterns, k = 3, there is a " + str( round((k[2][2]/k[2][1])*100, 2) ) + 
	"% probability the following day will be an up day")

k2 = q13("+")
print("For the up day patterns, k = 1, there is a " + str( round((k2[0][2]/k2[0][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the up day patterns, k = 2, there is a " + str( round((k2[1][2]/k2[1][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the up day patterns, k = 3, there is a " + str( round((k2[2][2]/k2[2][1])*100, 2) ) + 
	"% probability the following day will be an up day")


# Question 2.1 ==========================================================================================================
# Starting in year 4, looking at the last W days (including the current day)
# How many times did the same pattern show up and was follow by "+" vs "-"?
# W = 2, 3, 4



# Add column for predicted labels w2, w3, w4

# From day 1 of year 4
# Look at the last W days (including the current date) and see how
# many times that pattern occurs and is followed with a "+" vs "-"




print("\n\n\n")