list = []
for i in range(1,1000):
	if i%3==0 or i%5==0:
		list.append(i)
sum=0
for obj in list:
	sum+=obj
print(sum)
