CREATE TABLE Brands (
	brand_id INT PRIMARY KEY,
	name_ TEXT,
	country TEXT,
	classification INT
);

CREATE TABLE Categories (
	category_id INT PRIMARY KEY,
	description VARCHAR(255)
);

CREATE TABLE Customers (
	customer_id INT PRIMARY KEY,
	name_ TEXT,
	email VARCHAR(255),
	phone VARCHAR(255),
	address TEXT
);

CREATE TABLE Products (
	product_id INT PRIMARY KEY,
	name_ TEXT,
	description VARCHAR(255),
	price INT,
	color TEXT,
	brand_id INT,
	category_id INT,
	Foreign key(brand_id) REFERENCES Brands(brand_id),
	Foreign key(category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Orders (
	order_id INT PRIMARY KEY,
	customer_id INT,
	orderDate DATE,
	FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Ordered_Product (
	orderedProduct_id INT PRIMARY KEY,
	order_id INT,
	product_id INT,
	PR_count INT,
	FOREIGN KEY(order_id) REFERENCES Orders(order_id),
	FOREIGN KEY(product_id) REFERENCES Products(product_id)
);

CREATE TABLE WareHouses ( 
	warehouse_id INT PRIMARY KEY,
	capable bool,
	location_ TEXT
);

CREATE TABLE Inventory ( 
	inventory_id INT PRIMARY KEY,
	product_id INT,
	warehouse_id INT,
	INVT_count INT,
	FOREIGN KEY(product_id) REFERENCES Products(product_id),
	FOREIGN KEY(warehouse_id) REFERENCES WareHouses(warehouse_id)
);

CREATE TABLE Discounts (
	discount_id INT PRIMARY KEY,
	product_id INT,
	DateStart DATE,
	DateFinish DATE,
	Season TEXT,
	Discount_percent INT,
	FOREIGN KEY(product_id) REFERENCES Products(product_id)
);

CREATE TABLE Deliveries (
	delivery_id INT PRIMARY KEY,
	order_id INT,
	shipDate DATE,
	status BOOL,
	FOREIGN KEY(order_id) REFERENCES Orders(order_id)
);

CREATE TABLE FeedBacks (
	feedback_id INT PRIMARY KEY,
	customer_id INT,
	product_id SERIAL,
	mark FLOAT,
	comm VARCHAR(255),
	FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
	FOREIGN KEY(product_id) REFERENCES Products(product_id)
);

CREATE TABLE CartProduct (
	cart_id INT PRIMARY KEY,
	product_id INT,
	customer_id INT,
	cartCount INT,
	FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
	FOREIGN KEY(product_id) REFERENCES Products(product_id)
);