data_csv = open('CupcakeInvoices.csv')

for row in data_csv:
   print (row)

data_csv.close()

data_csv = open('CupcakeInvoices.csv')

for row in data_csv:
    values = row.split(',')
    print(values[2])
data_csv.close()



data_csv = open('CupcakeInvoices.csv')
for row in data_csv:
  values = row.split(',')
  total_price = int(values[3]) * float(values[4])
  print(total_price)


  for row in data_csv:
    values = row.split(',')
    total_price = total_price + (int(values[3]) * float(values[4]))

    print(total_price)


print(round(total_price))

data_csv.close()





labels = ["Vanilla", "Chocolate", "Strawberry"]

data_csv = open('CupcakeInvoices.csv')



# for row in data_csv:
#     values = row.split(',')
#     if values[2] == 'Vanilla':
#         total_price = int((values[2],3)) * float((values[2],4))
#         print(total_price)
#     elif values[2] == 'Chocolate':
#          total_price = int((values[2]),3) * float((values[2], 4))
#          print(total_price)
#     elif values[2 == "Strawberry"]:
#         total_price == int((values[2],3)) * float((values[2], 4))
#         print(total_price)

# print(total_price)



labels = ["Vanilla", "Chocolate", "Strawberry"]

chocolate =[]
vanilla = []
strawberry = []


data_csv = open('CupcakeInvoices.csv')
for row in data_csv:
    values = row.split(',')
    if values[2] == 'Vanilla':
        vanilla.append((int(values[-2]) * float(values[-1])))
    elif values[2] == 'Chocolate':
         chocolate.append((int(values[-2]) * float(values[-1])))
    elif values[2] == "Strawberry":
        strawberry.append((int(values[-2]) * float(values[-1])))

total = []

total.append(round(sum(vanilla),2))
total.append(round(sum(chocolate),2))
total.append(round(sum(strawberry),2))

print (total)

import matplotlib.pyplot as plt

names = ['Vanilla', 'Chocolate', 'Strawberry']
#values_total = [1, 10, 100]

plt.figure(figsize=(5, 4))
plt.subplot()
plt.plot(names, total)
plt.suptitle("Cupcakes")
plt.xlabel("Type")
plt.ylabel("Total Price")
plt.show()

   
data_csv.close()