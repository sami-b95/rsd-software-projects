import pandas as pd

def compute_means(filename):
	means = []
	available_values = []
	with open(filename, "r") as f:
		while True:
			line = f.readline()
			if line.strip() == "":
				break
			new_numbers = [ float(x.strip()) for x in line.split(",") ]
			print ("new new_numbers: {}".format(new_numbers))
			if len(new_numbers) > len(means):
				available_values.extend([0] * (len(new_numbers) - len(means)))
				means.extend([0] * (len(new_numbers) - len(means)))
			for i in range(len(new_numbers)):
				means[i] = (available_values[i] * means[i] + new_numbers[i]) / (available_values[i] + 1)
			for i in range(len(new_numbers)):
				available_values[i] += 1
	return means, available_values

def save_means(filename, means):
	with open(filename, "w") as f:
		f.write(", ".join([ str(x) for x in means ]))