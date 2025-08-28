-- Question 1 Show the total payment amount for each payment date Only top 5 latest payment dates, sorted descending
SELECT paymentDate, 
       SUM(amount) AS totalAmount
FROM payments
GROUP BY paymentDate
ORDER BY paymentDate DESC
LIMIT 5;


-- Question 2 Find the average credit limit of each customer Display customer name, country, and average credit limit
SELECT customerName, 
       country, 
       AVG(creditLimit) AS averageCreditLimit
FROM customers
GROUP BY customerName, country;


-- Question 3 Find the total price of products ordered Total price = quantityOrdered * priceEach
SELECT productCode, 
       quantityOrdered, 
       (quantityOrdered * priceEach) AS totalPrice
FROM orderdetails
GROUP BY productCode, quantityOrdered, priceEach;


-- Question 4 Find the highest payment amount for each check number
SELECT checkNumber, 
       MAX(amount) AS highestAmount
FROM payments
GROUP BY checkNumber;
