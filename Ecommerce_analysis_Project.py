import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the MySQL database
connection = mysql.connector.connect(
    user='root',
    password='satyam',
    host='localhost',
    database='Ecommerce_analysis_Project'  
)

cursor = connection.cursor()

# Query data from the 'customer' table
cursor.execute('SELECT * FROM customer')
customer_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

# Query data from the 'product' table
cursor.execute('SELECT * FROM product')
product_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

# Query data from the 'order_details' table
cursor.execute('SELECT * FROM order_details')
order_data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

# Close the cursor and connection
cursor.close()
connection.close()

print("Customer Data:")
print(customer_data.head())
print("\nProduct Data:")
print(product_data.head())
print("\nOrder Details Data:")
print(order_data.head())

# ------------------ Customer Analysis ------------------ #
# Total number of customers city-wise
customers_citywise = customer_data.groupby('city').size().reset_index(name='total_customers')
print("Total number of customers city-wise:")
print(customers_citywise)

# Bar Chart for city-wise customer distribution
plt.figure(figsize=(10, 5))
plt.bar(customers_citywise['city'], customers_citywise['total_customers'], color='skyblue')
plt.title('Total Number of Customers City-wise')
plt.xlabel('City')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.show()

# Most frequent customers based on order history
customer_order_count = order_data.groupby('customer_id').size().reset_index(name='order_count')
most_frequent_customers = customer_order_count.nlargest(10, 'order_count')
print("Most frequent customers:")
print(most_frequent_customers)

# Bar Chart for Top 10 Most Frequent Customers
plt.figure(figsize=(10, 5))
plt.bar(most_frequent_customers['customer_id'], most_frequent_customers['order_count'], color='skyblue')
plt.title('Top 10 Most Frequent Customers')
plt.xlabel('Customer ID')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.show()

# ------------------ Product Analysis ------------------ #
# Total number of products by category
products_by_category = product_data.groupby('category').size().reset_index(name='total_products')
print("\nTotal number of products by category:")
print(products_by_category)

# Bar Chart for distribution of products
plt.figure(figsize=(10, 5))
plt.bar(products_by_category['category'], products_by_category['total_products'], color='skyblue')
plt.title('Distribution of Products by Category')
plt.xlabel('Category')
plt.ylabel('Number of Products')
plt.xticks(rotation=45)
plt.show()

# Products with low stock levels (assume a threshold of 10 units)
low_stock_products = product_data[product_data['stock'] < 10]
print("\nProducts with low stock levels:")
print(low_stock_products)

# Bar Chart: Low stock products
plt.figure(figsize=(10, 5))
plt.bar(low_stock_products['product_name'], low_stock_products['stock'], color='red')
plt.title('Products with Low Stock Levels')
plt.xlabel('Product Name')
plt.ylabel('Stock Level')
plt.xticks(rotation=45)
plt.show()

# Average, maximum, and minimum prices for products
price_stats = product_data['selling_price'].agg(['mean', 'max', 'min'])
print("\nProduct price statistics (average, max, min):")
print(price_stats)

# ------------------ Order Analysis ------------------ #
# Top 10 orders product-wise
top_10_orders = order_data.groupby('product_id')['total_price'].sum().nlargest(10).reset_index()
print("\nTop 10 orders product-wise:")
print(top_10_orders)

# Bar Chart for top 10 orders product-wise
plt.figure(figsize=(10, 5))
plt.bar(top_10_orders['product_id'], top_10_orders['total_price'], color='green')
plt.title('Top 10 Orders Product-wise')
plt.xlabel('Product ID')
plt.ylabel('Total Price')
plt.show()

# Order status distribution (pending, delivered, etc.)
order_status_distribution = order_data['order_status'].value_counts().reset_index(name='count')
print("\nOrder status distribution:")
print(order_status_distribution)

# Bar Chart for Order status distribution
plt.figure(figsize=(10, 5))
plt.bar(order_status_distribution['order_status'], order_status_distribution['count'], color='green')
plt.title('Order Status Distribution')
plt.xlabel('Order Status')
plt.ylabel('Number of Orders')
plt.show()

# Most popular products based on order quantity
popular_products = order_data.groupby('product_id')['quantity'].sum().nlargest(10).reset_index()
print("\nMost popular products based on order quantity:")
print(popular_products)

# ------------------ Sales Analysis ------------------ #
# Total revenue generated from orders product-wise
revenue_productwise = order_data.groupby('product_id')['total_price'].sum().reset_index()
print("\nTotal revenue generated from orders product-wise:")
print(revenue_productwise)

# Bar Chart: Revenue product-wise
plt.figure(figsize=(10, 5))
plt.bar(revenue_productwise['product_id'], revenue_productwise['total_price'], color='purple')
plt.title('Revenue Generated Product-wise')
plt.xlabel('Product ID')
plt.ylabel('Total Revenue')
plt.show()

# Total revenue generated from all orders
total_revenue = order_data['total_price'].sum()
print("\nTotal revenue generated from all orders:", total_revenue)

# Total revenue by product category percentage
merged_data = pd.merge(order_data, product_data, on='product_id')
category_revenue = merged_data.groupby('category')['total_price'].sum()
category_revenue_percentage = (category_revenue / total_revenue) * 100
print("\nTotal revenue by product category (percentage):")
print(category_revenue_percentage)

# Pie Chart: Revenue by product category (percentage)
plt.figure(figsize=(8, 8))
plt.pie(category_revenue_percentage, labels=category_revenue.index, autopct='%1.1f%%', startangle=140)
plt.title('Revenue by Product Category (Percentage)')
plt.show()

# Performance of different product categories in terms of sales
category_performance = merged_data.groupby('category')['total_price'].sum().reset_index()
print("\nPerformance of different product categories:")
print(category_performance)

# Most profitable products based on the difference between original and selling prices
merged_data['profit'] = (merged_data['selling_price'] - merged_data['original_price']) * merged_data['quantity']
most_profitable_products = merged_data.groupby('product_name')['profit'].sum().nlargest(10).reset_index()
print("\nMost profitable products:")
print(most_profitable_products)

# Bar Chart: Most profitable products
plt.figure(figsize=(10, 5))
plt.bar(most_profitable_products['product_name'], most_profitable_products['profit'], color='purple')
plt.title('Most Profitable Products')
plt.xlabel('Product Name')
plt.ylabel('Profit')
plt.show()

# ------------------ Customer Order Patterns ------------------ #
# Product names with the highest and lowest order quantities
product_order_quantity = merged_data.groupby('product_name')['quantity'].sum().reset_index()
highest_ordered_product = product_order_quantity.nlargest(1, 'quantity')
lowest_ordered_product = product_order_quantity.nsmallest(1, 'quantity')
print("\nProduct with the highest order quantity:")
print(highest_ordered_product)
print("\nProduct with the lowest order quantity:")
print(lowest_ordered_product)

# Customers with the highest and lowest order quantities by name
merged_data_customers = pd.merge(order_data, customer_data, on='customer_id')
customer_order_quantity = merged_data_customers.groupby('name')['quantity'].sum().reset_index()
highest_ordered_customer = customer_order_quantity.nlargest(1, 'quantity')
lowest_ordered_customer = customer_order_quantity.nsmallest(1, 'quantity')
print("\nCustomer with the highest order quantity:")
print(highest_ordered_customer)
print("\nCustomer with the lowest order quantity:")
print(lowest_ordered_customer)

# Most preferred payment modes
preferred_payment_modes = order_data['payment_mode'].value_counts().reset_index(name='count')
print("\nMost preferred payment modes:")
print(preferred_payment_modes)

# ------------------ Time-based Analysis ------------------ #
order_data['order_date'] = pd.to_datetime(order_data['order_date'])
monthwise_sales = order_data.groupby(order_data['order_date'].dt.to_period('M'))['total_price'].sum().reset_index()
print("\nMonth-wise total sales:")

print(monthwise_sales)
plt.figure(figsize=(10, 5))
plt.plot(monthwise_sales['order_date'].astype(str), monthwise_sales['total_price'], marker='o', color='darkblue')
plt.title('Month-wise Total Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

month_year_sales = order_data.groupby(order_data['order_date'].dt.to_period('M'))['total_price'].sum().reset_index()
print("\nMonth and year-wise total sales:")
print(month_year_sales)
peak_order_date = order_data.groupby('order_date')['quantity'].sum().idxmax()
print("\n")
