
def Weighted_Mean(x,y,j):
	sum_y=0
	sum_xy=0
	
	for i in range(0,j):
		sum_xy+=x[i]*y[i]
		sum_y+=y[i]

	mean=sum_xy/sum_y

	return float(mean)






Data_List=[]
Weight_List=[]
n=int(input())
Numeric_Data = input().split()
Numeric_weight = input().split()
if len(Numeric_Data)<=n and len(Numeric_weight)<=n :
	for i in range(0,n):
		Data_List.append(int(Numeric_Data[i]))
		Weight_List.append(int(Numeric_weight[i]))
	print(Data_List)
	print(Weight_List)
else:
	print("The length of list is exceed!!")

result_mean=Weighted_Mean(Data_List,Weight_List,n)

print("{:.1f}".format(result_mean))
# while len(Numeric_Data)<n:

# 	Data_List.append(Numeric_Data[i])
# print(Data_List)


# d2M2Y2 = input().split()
# d2 = int(d2M2Y2[0])
# m2 = int(d2M2Y2[1])
# y2 = int(d2M2Y2[2])

# result = server_cost(d1, m1, y1, d2, m2, y2)
# print(str(result) + '\n')