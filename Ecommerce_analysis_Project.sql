CREATE DATABASE Ecommerce_analysis_Project;
USE Ecommerce_analysis_Project;

-- Create the customer table
CREATE TABLE `customer` (
    `customer_id` varchar(10) NOT NULL,
    `name` varchar(100) NOT NULL,
    `city` varchar(65) NOT NULL,
    `email` varchar(45) NOT NULL,
    `phone_no` varchar(15) NOT NULL,
    `address` varchar(100) NOT NULL,
    `pin_code` int NOT NULL,
    PRIMARY KEY (`customer_id`)
);	

-- Create the product table
CREATE TABLE `product` (
    `product_id` varchar(10) NOT NULL,
    `product_name` varchar(100) NOT NULL,
    `category` varchar(65) NOT NULL,
    `sub_category` varchar(45) NOT NULL,
    `original_price` double NOT NULL,
    `selling_price` double NOT NULL,
    `stock` int NOT NULL,
    PRIMARY KEY (`product_id`)
);

-- Create the order_details table
CREATE TABLE `order_details` (
    `order_id` int NOT NULL AUTO_INCREMENT,
    `customer_id` varchar(10) NOT NULL,
    `product_id` varchar(10) NOT NULL,
    `quantity` double NOT NULL,
    `total_price` double NOT NULL,
    `payment_mode` varchar(60) NOT NULL,
    `order_date` datetime DEFAULT NULL,
    `order_status` varchar(20) NOT NULL,
    PRIMARY KEY (`order_id`),
    KEY `customer_id` (`customer_id`),
    KEY `product_id` (`product_id`),
    CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`customer_id`)
    REFERENCES `customer` (`customer_id`),
    CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`product_id`)
    REFERENCES `product` (`product_id`)
);

-- Insert sample data into the customer table
INSERT INTO customer (customer_id, name, city, email, phone_no, address, pin_code) VALUES
('C011', 'Anna Taylor', 'Delhi', 'anna@example.com', '9812345678', '2345 Willow Way', 110002),
('C012', 'Michael Wilson', 'Mumbai', 'michael@example.com', '9812345679', '6789 Palm Street', 400002),
('C013', 'Olivia Harris', 'Bangalore', 'olivia@example.com', '9812345680', '7890 Cherry Lane', 560002),
('C014', 'Liam Lee', 'Chennai', 'liam@example.com', '9812345681', '8901 Maple Street', 600002),
('C015', 'Sophia Davis', 'Kolkata', 'sophia@example.com', '9812345682', '9012 Oak Street', 700002),
('C016', 'James Miller', 'Hyderabad', 'james@example.com', '9812345683', '1234 Pine Hill', 500002),
('C017', 'Isabella Moore', 'Pune', 'isabella@example.com', '9812345684', '5678 Cedar Drive', 411002),
('C018', 'Benjamin Taylor', 'Ahmedabad', 'benjamin@example.com', '9812345685', '9012 Birch Lane', 380002),
('C019', 'Lucas Anderson', 'Surat', 'lucas@example.com', '9812345686', '3456 Spruce Avenue', 395002),
('C020', 'Mia Thomas', 'Jaipur', 'mia@example.com', '9812345687', '7890 Fir Lane', 302002);

-- Insert sample data into the product table
INSERT INTO product (product_id, product_name, category, sub_category, original_price, selling_price, stock) VALUES
('P011', 'Gaming Laptop', 'Electronics', 'Computers', 80000, 75000, 5),
('P012', 'Wireless Headphones', 'Electronics', 'Accessories', 3000, 2700, 15),
('P013', 'Smart Speaker', 'Electronics', 'Accessories', 7000, 6500, 20),
('P014', 'Smart TV', 'Electronics', 'Televisions', 60000, 55000, 7),
('P015', 'Action Camera', 'Electronics', 'Photography', 25000, 23000, 10),
('P016', 'Gaming Console', 'Electronics', 'Gaming', 40000, 37000, 12),
('P017', 'Fitness Tracker', 'Electronics', 'Wearables', 5000, 4500, 30),
('P018', 'External Hard Drive', 'Electronics', 'Accessories', 6000, 5500, 18),
('P019', 'Smart Refrigerator', 'Appliances', 'Home', 50000, 45000, 8),
('P020', 'Washing Machine', 'Appliances', 'Home', 30000, 27000, 5);

-- Insert sample data into the order_details table
INSERT INTO order_details (customer_id, product_id, quantity, total_price, payment_mode, order_date, order_status) VALUES
('C011', 'P011', 1, 75000, 'Credit Card', '2024-10-10 10:30:00', 'Shipped'),
('C012', 'P012', 3, 8100, 'Debit Card', '2024-10-10 11:00:00', 'Processing'),
('C013', 'P013', 1, 6500, 'PayPal', '2024-10-10 11:30:00', 'Delivered'),
('C014', 'P014', 1, 55000, 'Credit Card', '2024-10-10 12:00:00', 'Shipped'),
('C015', 'P015', 2, 46000, 'Cash on Delivery', '2024-10-10 12:30:00', 'Pending'),
('C016', 'P016', 1, 37000, 'Credit Card', '2024-10-10 13:00:00', 'Shipped'),
('C017', 'P017', 4, 18000, 'Debit Card', '2024-10-10 13:30:00', 'Processing'),
('C018', 'P018', 2, 11000, 'PayPal', '2024-10-10 14:00:00', 'Delivered'),
('C019', 'P019', 1, 45000, 'Credit Card', '2024-10-10 14:30:00', 'Shipped'),
('C020', 'P020', 1, 27000, 'Cash on Delivery', '2024-10-10 15:00:00', 'Pending');

-- Select all records from the tables to verify data insertion
SELECT * FROM customer;
SELECT * FROM product;
SELECT * FROM order_details;
