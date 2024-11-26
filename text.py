sql_query = """
SELECT 
    product.id, 
    product.title, 
    product.description, 
    product.stock, 
    product.price, 
    product.thumbnail, 
    category.name AS category_name
FROM product
LEFT JOIN category ON product.category_id = category.id
WHERE product.id = %s;
"""


