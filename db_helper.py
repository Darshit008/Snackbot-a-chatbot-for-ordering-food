
# cd backend
# uvicorn main:app --reload

# from backend import db_helper
# 
import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="user",
    password="Easy2login!",
    database="pandeyji_eatery",
    auth_plugin="mysql_native_password"
)

# Function to call the MySQL stored procedure and insert an order item
def insert_order_item(food_item, quantity, order_id):
    try:
        cursor = cnx.cursor()

        # Calling the stored procedure
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))

        # Committing the changes
        cnx.commit()

        # Closing the cursor
        cursor.close()

        print("Order item inserted successfully!")

        return 1

    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")

        # Rollback changes if necessary
        cnx.rollback()

        return -1

    except Exception as e:
        print(f"An error occurred: {e}")
        # Rollback changes if necessary
        cnx.rollback()

        return -1

# Function to insert a record into the order_tracking table
def insert_order_tracking(order_id, status):
    cursor = cnx.cursor()

    # Inserting the record into the order_tracking table
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"
    cursor.execute(insert_query, (order_id, status))

    # Committing the changes
    cnx.commit()

    # Closing the cursor
    cursor.close()

def get_total_order_price(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to get the total order price
    query = f"SELECT get_total_order_price({order_id})"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    return result

# Function to get the next available order_id
def get_next_order_id():
    cursor = cnx.cursor()

    # Executing the SQL query to get the next available order_id
    query = "SELECT MAX(order_id) FROM orders"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()[0]

    # Closing the cursor
    cursor.close()

    # Returning the next available order_id
    if result is None:
        return 1
    else:
        return result + 1
    
def get_order_status(order_id):
    cursor = cnx.cursor()

    # Executing the SQL query to fetch the order status
    query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
    cursor.execute(query)

    # Fetching the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Log the result for debugging
    print(f"Result: {result}")

    # Returning the order status
    if result:
        return result[0]
    else:
        return None


# # Function to fetch the order status from the order_tracking table
# def get_order_status(order_id):
#     cursor = cnx.cursor()

#     # Executing the SQL query to fetch the order status
#     query = f"SELECT status FROM order_tracking WHERE order_id = {order_id}"
#     print(f"Result: {result}")
#     cursor.execute(query)

#     # Fetching the result
#     result = cursor.fetchone()

#     # Closing the cursor
#     cursor.close()

#     # Returning the order status
#     if result:
#         return result[0]
#     else:
#         return None

# Example db_helper function for get_order_status:
# def get_order_status(order_id: int):
#     try:
#         # Make sure you're querying the right table and columns
#         cursor = connection.cursor()
#         cursor.execute("SELECT status FROM order_tracking WHERE order_id = %s", (order_id,))
#         result = cursor.fetchone()
#         return result[0] if result else None
#     except Exception as e:
#         print(f"Error in get_order_status: {str(e)}")
#         return None

# def get_order_status_from_db(order_id):
#     if not order_id:
#         raise ValueError("Invalid order ID")
#     # Your actual database logic here, like using SQLAlchemy or raw queries
#     result = database_query(order_id)
#     if not result:
#         raise ValueError("Order not found")
#     return result


if __name__ == "__main__":
    # print(get_total_order_price(56))
    # insert_order_item('Samosa', 3, 99)
    # insert_order_item('Pav Bhaji', 1, 99)
    # insert_order_tracking(99, "in progress")
    print(get_next_order_id())
