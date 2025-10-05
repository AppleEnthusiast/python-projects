import matplotlib.pyplot as plt

products = ["Apple","Banana","Cherry","Orange","Strawberry"]
sales    = [120,90,60,30,150]

plt.barh(products,sales,color="skyblue")

plt.title("Units Sold")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.grid(axis="x",linestyle="--",alpha=0.6)

for index,value in enumerate(sales):
	plt.text(value+3,index,str(value))

plt.show()

