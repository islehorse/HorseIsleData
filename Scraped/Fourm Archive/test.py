import os

a = os.listdir(".")
for aa in a:
	os.rename(aa, aa.replace("MOD_", ""))