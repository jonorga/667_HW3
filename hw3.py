###
### CS667 Data Science with Python, Homework 3, Jon Organ
###

import pandas as pd
from os.path import exists
import matplotlib.pyplot as plt
import numpy as np


file = pd.read_csv("cmg.csv")
file_spy = pd.read_csv("spy.csv")

file['True Label'] = ''
file_spy['True Label'] = ''


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
print("\nQuestion 1.3")
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
# Add column for predicted labels w2, w3, w4
file['W2'] = ''
file_spy['W2'] = ''
file['W3'] = ''
file_spy['W3'] = ''
file['W4'] = ''
file_spy['W4'] = ''


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
def q31(file_len, working_file):
	working_file['Ensemble Label'] = ''
	i = 0
	while i < file_len:
		pluses = 0
		minuses = 0
		if working_file["W2"].get(i) == "+":
			pluses += 1
		elif working_file["W2"].get(i) == "-":
			minuses += 1
		if working_file["W3"].get(i) == "+":
			pluses += 1
		elif working_file["W3"].get(i) == "-":
			minuses += 1
		if working_file["W4"].get(i) == "+":
			pluses += 1
		elif working_file["W4"].get(i) == "-":
			minuses += 1

		if pluses > minuses:
			working_file.at[i, "Ensemble Label"] = "+"
		elif minuses > pluses:
			working_file.at[i, "Ensemble Label"] = "-"
		i += 1
	return working_file

file = q31(file_length, file)
file_spy = q31(file_length_2, file_spy)
print("Ensemble labels computed for Chipotle and Spy stock.\n")



# Question 3.2 ==========================================================================================================
print("Question 3.2")
def q32(file_len, working_file, file_name):
	i = 0
	total_ensem_labels = 0
	correct_ensem_labels = 0
	while i < file_len:
		if working_file["Ensemble Label"].get(i) == "+" or working_file["Ensemble Label"].get(i) == "-":
			total_ensem_labels += 1
			if working_file["Ensemble Label"].get(i) == working_file["True Label"].get(i):
				correct_ensem_labels += 1
		i += 1
	ensem_accuracy = round((correct_ensem_labels/total_ensem_labels) * 100, 2)
	print("For the " + file_name + " stock, the Ensemble Label predicted the correct output " 
		+ str(ensem_accuracy) + "% of the time")

q32(file_length, file, "Chipotle")
q32(file_length_2, file_spy, "Spy")



# Question 3.3 ==========================================================================================================
print("\nQuestion 3.3")
def q334(file_len, working_file, file_name, symbol):
	if symbol == "+":
		antisymbol = "-"
	else:
		antisymbol = "+"
	i = 0
	w2_total = 0
	w2_correct = 0
	w3_total = 0
	w3_correct = 0
	w4_total = 0
	w4_correct  = 0
	ensem_total = 0
	ensem_correct = 0
	while i < file_len:
		# Compute accuracy for "-" labels against W = 2, 3, 4, and Ensemble Labels
		if working_file["True Label"].get(i) == symbol:
			if working_file["Ensemble Label"].get(i) == antisymbol:
				ensem_total += 1
			elif working_file["Ensemble Label"].get(i) == symbol:
				ensem_total += 1
				ensem_correct += 1

			if working_file["W2"].get(i) == antisymbol:
				w2_total += 1
			elif working_file["W2"].get(i) == symbol:
				w2_total += 1
				w2_correct += 1

			if working_file["W3"].get(i) == antisymbol:
				w3_total += 1
			elif working_file["W3"].get(i) == symbol:
				w3_total += 1
				w3_correct += 1

			if working_file["W4"].get(i) == antisymbol:
				w4_total += 1
			elif working_file["W4"].get(i) == symbol:
				w4_total += 1
				w4_correct += 1
		i += 1

	ensem_accuracy = round((ensem_correct / ensem_total) * 100, 2)
	w2_accuracy = round((w2_correct / w2_total) * 100, 2)
	w3_accuracy = round((w3_correct / w3_total) * 100, 2)
	w4_accuracy = round((w4_correct / w4_total) * 100, 2)
	if ensem_accuracy > w2_accuracy and ensem_accuracy > w3_accuracy and ensem_accuracy > w4_accuracy:
		result = "more"
	else:
		result = "less"
	print("For the " + file_name + " stock, the Ensemble Label was " + result + " accurate (" + str(ensem_accuracy)
	 + "%) for \"" + symbol + "\" labels than W = 2 (" + str(w2_accuracy) + "%), W = 3 (" + str(w3_accuracy)
	 + "%), and W = 4 (" + str(w4_accuracy) + "%)")

q334(file_length, file, "Chipotle", "-")
q334(file_length_2, file_spy, "Spy", "-")

# Question 3.4 ==========================================================================================================
print("\nQuestion 3.4")
q334(file_length, file, "Chipotle", "+")
q334(file_length_2, file_spy, "Spy", "+")




# Question 4 ============================================================================================================
def q4(file_len, working_file, file_name):
	i = 0

	true_pos_2 = 0
	true_pos_3 = 0
	true_pos_4 = 0
	true_pos_ensem = 0

	false_pos_2 = 0
	false_pos_3 = 0
	false_pos_4 = 0
	false_pos_ensem = 0

	true_neg_2 = 0
	true_neg_3 = 0
	true_neg_4 = 0
	true_neg_ensem = 0

	false_neg_2 = 0
	false_neg_3 = 0
	false_neg_4 = 0
	false_neg_ensem = 0

	while i < file_len:
		if working_file["True Label"].get(i) == "+" and working_file["W2"].get(i) == "+":
			true_pos_2 += 1
		if working_file["True Label"].get(i) == "+" and working_file["W3"].get(i) == "+":
			true_pos_3 += 1
		if working_file["True Label"].get(i) == "+" and working_file["W4"].get(i) == "+":
			true_pos_4 += 1
		if working_file["True Label"].get(i) == "+" and working_file["Ensemble Label"].get(i) == "+":
			true_pos_ensem += 1

		if working_file["True Label"].get(i) == "-" and working_file["W2"].get(i) == "+":
			false_pos_2 += 1
		if working_file["True Label"].get(i) == "-" and working_file["W3"].get(i) == "+":
			false_pos_3 += 1
		if working_file["True Label"].get(i) == "-" and working_file["W4"].get(i) == "+":
			false_pos_4 += 1
		if working_file["True Label"].get(i) == "-" and working_file["Ensemble Label"].get(i) == "+":
			false_pos_ensem += 1

		if working_file["True Label"].get(i) == "-" and working_file["W2"].get(i) == "-":
			true_neg_2 += 1
		if working_file["True Label"].get(i) == "-" and working_file["W3"].get(i) == "-":
			true_neg_3 += 1
		if working_file["True Label"].get(i) == "-" and working_file["W4"].get(i) == "-":
			true_neg_4 += 1
		if working_file["True Label"].get(i) == "-" and working_file["Ensemble Label"].get(i) == "-":
			true_neg_ensem += 1

		if working_file["True Label"].get(i) == "+" and working_file["W2"].get(i) == "-":
			false_neg_2 += 1
		if working_file["True Label"].get(i) == "+" and working_file["W3"].get(i) == "-":
			false_neg_3 += 1
		if working_file["True Label"].get(i) == "+" and working_file["W4"].get(i) == "-":
			false_neg_4 += 1
		if working_file["True Label"].get(i) == "+" and working_file["Ensemble Label"].get(i) == "-":
			false_neg_ensem += 1

		i += 1

	true_pos_rate_2 = true_pos_2 / (true_pos_2 + false_neg_2)
	true_pos_rate_3 = true_pos_3 / (true_pos_3 + false_neg_3)
	true_pos_rate_4 = true_pos_4 / (true_pos_4 + false_neg_4)
	true_pos_rate_ensem = true_pos_ensem / (true_pos_ensem + false_neg_ensem)

	true_neg_rate_2 = true_neg_2 / (true_neg_2 + false_pos_2)
	true_neg_rate_3 = true_neg_3 / (true_neg_3 + false_pos_3)
	true_neg_rate_4 = true_neg_4 / (true_neg_4 + false_pos_4)
	true_neg_rate_ensem = true_neg_ensem / (true_neg_ensem + false_pos_ensem)

	result = [[true_pos_2, true_pos_3, true_pos_4, true_pos_ensem], 
			  [false_pos_2, false_pos_3, false_pos_4, false_pos_ensem],
			  [true_neg_2, true_neg_3, true_neg_4, true_neg_ensem],
			  [false_neg_2, false_neg_3, false_neg_4, false_neg_ensem],
			  [true_pos_rate_2, true_pos_rate_3, true_pos_rate_4, true_pos_rate_ensem],
			  [true_neg_rate_2, true_neg_rate_3, true_neg_rate_4, true_neg_rate_ensem]]
	return result



data = [["2", "3", "4", "Ensemble", "2", "3", "4", "Ensemble"], 
	["S&P-500", "S&P-500", "S&P-500", "S&P-500", "Chipotle", "Chipotle", "Chipotle", "Chipotle"]]


print("\nQuestion 4")
cmg_val = q4(file_length, file, "Chipotle")
spy_val = q4(file_length_2, file_spy, "Spy")


for cmg_item, spy_item in zip(cmg_val, spy_val):
	temp_item = cmg_item + spy_item
	data.append(temp_item)
data = zip(*data)


df = pd.DataFrame(data, columns=['W', 'ticker', 'TP', 'FP', 'TN', 'FN', 'TPR', 'TNR'])
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.table(cellText=df.values, colLabels=df.columns, loc='center')

print("Saving table for question 4.7, this may take some time ...... ")
fig.savefig("Question_4.7_Table.png", dpi=1200)

# Question 4.8 ==========================================================================================================
print("\nQuestion 4.8")
print("Although there was a high amount of false positives for both Spy and Chipotle for W = 2, the true positive"
	+ " rate was very good. On the flipside the true negative rate would be a very poor indicator to work off of.")



# Question 4.8 ==========================================================================================================
print("\nQuestion 5.2")


i = 0
count = 0
balance = 100
bal_w = 100
bal_ensem = 100
first_day = True
daily_balance = []
daily_w = []
daily_ensem = []
while i < file_length:
	temp = file["Date"].get(i)
	if temp.split("/")[2] == "20":
		count += 1
		if first_day:
			your_stock = 100 / file["Close"].get(i)
			daily_balance.append(100)
			first_day = False
		else:
			daily_balance.append(your_stock * file["Close"].get(i))
		if bal_w > 0:
			if file["W2"].get(i + 1) == "+":
				stock_w = 100 / file["Close"].get(i)
				bal_w = stock_w * file["Close"].get(i + 1)
				daily_w.append(bal_w)
			else:
				daily_w.append(bal_w)
		else:
			daily_w.append(0)
		if bal_ensem > 0:
			if file["Ensemble Label"].get(i + 1) == "+":
				stock_ensem = 100 / file["Close"].get(i)
				bal_ensem = stock_ensem * file["Close"].get(i + 1)
				daily_ensem.append(bal_ensem)
			else:
				daily_ensem.append(bal_ensem)
		else:
			daily_ensem.append(0)

	i += 1

days = np.arange(0, count, 1)

fig1, ax1 = plt.subplots()
ax1.plot(days, daily_balance, color='g', label="Buy and hold")
ax1.plot(days, daily_w, color='c', label="W = 2")
ax1.plot(days, daily_ensem, color='r', label="Ensemble")
ax1.legend(loc="upper right")
ax1.set(xlabel='Day', ylabel='Account balance (dollars)',
       title='Account balance by day for CMG (Trading balance)')
ax1.grid()

print("Saving graph for question 5.2, this may take some time ...... ")
fig1.savefig("Question_5.2.png")

print("There aren't any particular patterns that emerge from W = 2 or the ensemble label. Once again "
	+ "buy and hold results in the highest account value.\n")

print("Question 6")
print("Answer: C, Pinocchio plagiarized and violated academic code")


print("\n\n\n")