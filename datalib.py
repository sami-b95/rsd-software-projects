import pandas as pd

def compute_means(filename):
	df = pd.read_csv(filename, header=None)
	return list(df.mean(axis=0))

def save_means(filename, means):
	with open(filename, "w") as f:
		f.write(", ".join([ str(x) for x in means ]))