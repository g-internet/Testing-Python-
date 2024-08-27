from tqdm import tqdm
import time

for i in tqdm (range (2500), 
			desc="Loading…", 
			ascii=False, ncols=75):
	time.sleep(0.1)
	
print("Complete.")