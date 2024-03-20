from sql_connection import get_sql_connection

def get_all_products(connection):
    
    cursor = connection.cursor()
    query = 'SELECT products.product_id, products.product_name, products.uom_id, products.price_per_unit,uom.uom_name FROM products INNER JOIN uom ON products.uom_id=uom.uom_id'

    cursor.execute(query)
    
    response = []

    for (product_id, product_name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                
                'product_id': product_id,
                'product_name': product_name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
                
            }
        )
    


    return response
    


def add_new_products(connection):
    cursor = connection.cursor()
    add_products = ("INSERT INTO products "
                    "(product_name, uom_id, price_per_unit)"
                    "VALUES (%s, %s, %s)")
    
    data_products = ('sandwich', '1', '25')

    cursor.execute(add_products, data_products)


if __name__ == '__main__':
    
    connection = get_sql_connection()
    print(add_new_products(connection))
    print(get_all_products(connection))
    