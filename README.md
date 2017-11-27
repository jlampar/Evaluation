# Evaluation
CSV-based evaluation.

Program takes 3 files as the input:
- products.csv - products table (price,currency,quantity,corresponding_id
- currency_ratio.csv - currencies and their ratio to PLN
- correspondence.csv - limits of products count in cateogories

Program reads all files and converts them to dictionaries. Then from products dictionary with particular corresponding ID it takes those with the highest total price (price * quantity), limiting data set by limit and aggregates prices.
Results are saved to finest.csv with five columns: id, in_total, avgerage, currency,ignored. It summarizes the total and average price of products of each category and moreover how many products are ignored due to the limits.
Output is placed into the same directory as input
