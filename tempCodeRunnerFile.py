def add_recipe(name, description, prep_time, cook_time, servings, difficulty_level):
#     try:
#         # Connect to the MySQL database
#         connection = mysql.connector.connect(host='localhost', user='root', password='', database='food_recipie')

#         # Create a cursor object to execute SQL queries
#         cursor = connection.cursor()

#         # Define the SQL query to insert a new recipe
#         sql = "INSERT INTO recipes (name, description, prep_time, cook_time, servings, difficulty_level) VALUES (%s, %s, %s, %s, %s, %s)"

#         # Execute the SQL query with the provided parameters
#         cursor.execute(sql, (name, description, prep_time, cook_time, servings, difficulty_level))

#         # Commit the transaction to save the changes
#         connection.commit()

#         # Close the cursor and database connection
#         cursor.close()
#         connection.close()

#         print("Recipe added successfully!")

#     except mysql.connector.Error as error:
#         # Handle any MySQL errors that occur during the execution of the function
#         print("Error adding recipe:", error)
