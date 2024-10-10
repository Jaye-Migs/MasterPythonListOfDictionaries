Products = ({
  "ID" : 1,
  "Name" : "Laptop",
  "Category" : "Electronics",
  "Price" : 750,
  "Stock" : 50,
  "Supplier Email" : "supplier1@gmail.com"
},{
  "ID" : 2,
  "Name" : "Desk Chair",
  "Category" : "Furniture",
  "Price" : 100,
  "Stock" : 200,
  "Supplier Email" : "supplier2@gmail.com"
},{
  "ID" : 3,
  "Name" : "Smartwatch",
  "Category" : "Electronics",
  "Price" : 200,
  "Stock" : 150,
  "Supplier Email" : "supplier3@gmail.com"
},{
  "ID" : 4,
  "Name" : "Notebook",
  "Category" : "Stationery",
  "Price" : 5,
  "Stock" : 500,
  "Supplier Email" : "supplier4@gmail.com"
},{
  "ID" : 5,
  "Name" : "Running Shoes",
  "Category" : "Apparel",
  "Price" : 80,
  "Stock" : 100,
  "Supplier Email" : "supplier5@gmail.com"
})
for Product in Products:
    print(f"ID: {Product['ID']}, Name: {Product['Name']}, Category: {Product['Category']}, Price: {Product['Price']}, Stock: {Product['Stock']}, Supplier Email: {Product['Supplier Email']}")