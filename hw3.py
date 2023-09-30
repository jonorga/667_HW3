import pandas as pd
from os.path import exists


file = pd.read_csv("cmg.csv")
file_spy = pd.read_csv("spy.csv")

#print(type(file["Return"].get(1)))

file['True Label'] = ''
file_spy['True Label'] = ''

#a = file.iloc[[0]]
#print(a)

#file.at[0, "True Label"] = "+"

#a = file.iloc[-5:]

#print(len(file.index))


# Question 1.1 ==========================================================================================================
file_length = len(file.index)
file_length_2 = len(file_spy.index)

def q11(file_len, working_file):
	i = 0
	while i < file_len:
		r_balance = working_file["Return"].get(i)
		if r_balance < 0:
			working_file.at[i, "True Label"] = "-"
		else:
			working_file.at[i, "True Label"] = "+"
		i += 1
	return working_file

file = q11(file_length, file)
file_spy = q11(file_length_2, file_spy)

# Question 1.2 ==========================================================================================================
print("Question 1.2")
def q12(file_len, working_file):
	i = 0
	l_val = 0
	l_pos = 0
	l_neg = 0
	while i < file_len:
		temp = working_file["Date"].get(i)
		if temp.split("/")[2] == "20":
			i = file_len
		else:
			l_val += 1
		if working_file["True Label"].get(i) == "+":
			l_pos += 1
		elif working_file["True Label"].get(i) == "-":
			l_neg += 1
		i += 1
	return l_pos, l_val

l_pos, l_val = q12(file_length, file)
print("The probability that the first day of year 4 for Chipotle will be an up day is " + 
	str(round((l_pos/l_val) * 100, 2)) + "%")
l_pos2, l_val2 = q12(file_length_2, file_spy)
print("The probability that the first day of year 4 for Spy will be an up day is " + 
	str(round((l_pos2/l_val2) * 100, 2)) + "%")

# Question 1.3 & 1.4 ====================================================================================================
print("Question 1.3")
def q13(symbol, file_len, working_file):
	# Below is k value followed by total pattern found then pos pattern found
	k = [[1, 0, 0], [2, 0, 0], [3, 0, 0]]

	k_step = 0
	while k_step < len(k):
		i = k[k_step][0]
		while i < file_len:
			temp = working_file["Date"].get(i)
			if temp.split("/")[2] == "20":
				i = file_len
			found_pat = True
			prev = i - 1


			while i - prev < k[k_step][0] + 1:
				if working_file["True Label"].get(prev) == symbol:
					found_pat = False
				prev -= 1
			if found_pat:
				k[k_step][1] += 1
				if working_file["True Label"].get(i) == "+":
					k[k_step][2] += 1
			# if the k previous elements are "-"
				# add one to total pattern found for this k
				# if next is "+"
					# add one to pos pattern for this k
			i += 1
		k_step += 1
	return k

k = q13("-", file_length, file)
k3 = q13("-", file_length_2, file_spy)
print("For the Chipotle down day patterns, k = 1, there is a " + str( round((k[0][2]/k[0][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the Chipotle down day patterns, k = 2, there is a " + str( round((k[1][2]/k[1][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the Chipotle down day patterns, k = 3, there is a " + str( round((k[2][2]/k[2][1])*100, 2) ) + 
	"% probability the following day will be an up day")

print("For the Spy down day patterns, k = 1, there is a " + str( round((k3[0][2]/k3[0][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the Spy down day patterns, k = 2, there is a " + str( round((k3[1][2]/k3[1][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the Spy down day patterns, k = 3, there is a " + str( round((k3[2][2]/k3[2][1])*100, 2) ) + 
	"% probability the following day will be an up day\n")

print("Question 1.4")
k2 = q13("+", file_length, file)
k4 = q13("+", file_length_2, file_spy)
print("For the Chipotle up day patterns, k = 1, there is a " + str( round((k2[0][2]/k2[0][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the Chipotle up day patterns, k = 2, there is a " + str( round((k2[1][2]/k2[1][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the Chipotle up day patterns, k = 3, there is a " + str( round((k2[2][2]/k2[2][1])*100, 2) ) + 
	"% probability the following day will be an up day")

print("For the Spy up day patterns, k = 1, there is a " + str( round((k4[0][2]/k4[0][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the Spy up day patterns, k = 2, there is a " + str( round((k4[1][2]/k4[1][1])*100, 2) ) + 
	"% probability the following day will be an up day")
print("For the Spy up day patterns, k = 3, there is a " + str( round((k4[2][2]/k4[2][1])*100, 2) ) + 
	"% probability the following day will be an up day\n")


# Question 2.1 ==========================================================================================================
# Starting in year 4, looking at the last W days (including the current day)
# How many times did the same pattern show up and was follow by "+" vs "-"?
# W = 2, 3, 4



# Add column for predicted labels w2, w3, w4
file['W2'] = ''
file_spy['W2'] = ''
file['W3'] = ''
file_spy['W3'] = ''
file['W4'] = ''
file_spy['W4'] = ''

# From day 1 of year 4
# Look at the last W days (including the current date) and see how
# many times that pattern occurs and is followed with a "+" vs "-"
def q21(file_len, working_file, file_name):
	i = 0
	found_year_4 = False
	while i < file_len:
		print("Predicting values for " + file_name + " ....... "
		 + str(round((i/file_len)*100, 2)) + "%", end="\r", flush=True)
		temp = working_file["Date"].get(i)
		if temp.split("/")[2] == "20":
			found_year_4 = True
		if found_year_4:
			w = [2, 3, 4]
			for val in w:
				pos_val = 0
				neg_val = 0
				j = i
				pattern = []
				temp_val = val
				while temp_val > 0:
					pattern.append(working_file["True Label"].get(j))
					temp_val -= 1
					j -= 1
				while j > val:
					pattern_check = []
					count = 0
					while count < val:
						pattern_check.append(working_file["True Label"].get(j - count))
						count += 1
					if pattern == pattern_check:
						if working_file["True Label"].get(j + 1) == "+":
							pos_val += 1
						elif working_file["True Label"].get(j + 1) == "-":
							neg_val += 1
					# TODO this needs to be added back into the working file
					j -= 1
				if val == 2:
					if pos_val > neg_val:
						working_file.at[i + 1, "W2"] = "+"
					else:
						working_file.at[i + 1, "W2"] = "-"
				elif val == 3:
					if pos_val > neg_val:
						working_file.at[i + 1, "W3"] = "+"
					else:
						working_file.at[i + 1, "W3"] = "-"
				elif val == 4:
					if pos_val > neg_val:
						working_file.at[i + 1, "W4"] = "+"
					else:
						working_file.at[i + 1, "W4"] = "-"
		i += 1
	print("Predicting values for " + file_name + " ....... 100.00%")
	return working_file

print("Question 2.1")
if exists("cmg_frame.csv"):
	file = pd.read_csv("cmg_frame.csv")
	print("Read previously predicted Chipotle file")
else:
	file = q21(file_length, file, "Chipotle")
	file.to_csv("cmg_frame.csv")

if exists("spy_frame.csv"):
	file_spy = pd.read_csv("spy_frame.csv")
	print("Read previously predicted Spy file")
else:
	file_spy = q21(file_length_2, file_spy, "Spy")
	file_spy.to_csv("spy_frame.csv")



# Question 2.2 ==========================================================================================================
def q22(file_len, working_file, file_name):
	i = 0
	w2_correct = 0
	w2_total = 0
	w3_correct = 0
	w3_total = 0
	w4_correct = 0
	w4_total = 0
	while i < file_len:
		if working_file["W2"].get(i) == "+" or working_file["W2"].get(i) == "-":
			w2_total += 1
			if working_file["W2"].get(i) == working_file["True Label"].get(i):
				w2_correct += 1
		if working_file["W3"].get(i) == "+" or working_file["W3"].get(i) == "-":
			w3_total += 1
			if working_file["W3"].get(i) == working_file["True Label"].get(i):
				w3_correct += 1
		if working_file["W4"].get(i) == "+" or working_file["W4"].get(i) == "-":
			w4_total += 1
			if working_file["W4"].get(i) == working_file["True Label"].get(i):
				w4_correct += 1
		i += 1

	w2_accuracy = round((w2_correct/w2_total) * 100, 2)
	w3_accuracy = round((w3_correct/w3_total) * 100, 2)
	w4_accuracy = round((w4_correct/w4_total) * 100, 2)
	print("For the " + file_name + " stock, W = 2 predicted the label correctly " + str(w2_accuracy) + "% of the time")
	print("For the " + file_name + " stock, W = 3 predicted the label correctly " + str(w3_accuracy) + "% of the time")
	print("For the " + file_name + " stock, W = 4 predicted the label correctly " + str(w4_accuracy) + "% of the time")
	return [w2_accuracy, w3_accuracy, w4_accuracy]

print("\nQuestion 2.2")
w_accuracy_cmg = q22(file_length, file, "Chipotle")
w_accuracy_spy = q22(file_length_2, file_spy, "Spy")
print("")


# Question 2.3 ==========================================================================================================
print("Question 2.3")
if w_accuracy_cmg[0] > w_accuracy_cmg[1] and w_accuracy_cmg[0] > w_accuracy_cmg[2]:
	print("For Chipotle, W = 2 gave the highest accuracy")
if w_accuracy_cmg[1] > w_accuracy_cmg[0] and w_accuracy_cmg[1] > w_accuracy_cmg[2]:
	print("For Chipotle, W = 3 gave the highest accuracy")
if w_accuracy_cmg[2] > w_accuracy_cmg[1] and w_accuracy_cmg[2] > w_accuracy_cmg[0]:
	print("For Chipotle, W = 4 gave the highest accuracy")

if w_accuracy_spy[0] > w_accuracy_spy[1] and w_accuracy_spy[0] > w_accuracy_spy[2]:
	print("For Spy, W = 2 gave the highest accuracy")
if w_accuracy_spy[1] > w_accuracy_spy[0] and w_accuracy_spy[1] > w_accuracy_spy[2]:
	print("For Spy, W = 3 gave the highest accuracy")
if w_accuracy_spy[2] > w_accuracy_spy[1] and w_accuracy_spy[2] > w_accuracy_spy[0]:
	print("For Spy, W = 4 gave the highest accuracy")

print("")


# Question 3.1 ==========================================================================================================
print("Question 3.1")



print("\n\n\n")