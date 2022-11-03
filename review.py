data = []
count = 1
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 1:
			print(len(data))
print(len(data))
print(data[0])