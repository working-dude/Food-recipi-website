import flask
from flask import request, jsonify
import mysql.connector
from flask import render_template, make_response
import json


app = flask.Flask(__name__)
app.config["DEBUG"] = True

page=[
  { "no": 1, "name": "index" },
  { "no": 2, "name": "second" } 
]
def initialize_database():
    connection = mysql.connector.connect(host='localhost', user='root', password='')
    cursor = connection.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS food_recipie")
    connection.commit()

    # Connect to the created database
    connection = mysql.connector.connect(host='localhost', user='root', password='', database='food_recipie')
    cursor = connection.cursor()

    # Define SQL queries for creating tables
    user_data = "CREATE TABLE IF NOT EXISTS user_data (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), phone_number VARCHAR(255), address VARCHAR(255))"
    recipes = "CREATE TABLE IF NOT EXISTS recipes (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), description VARCHAR(255), prep_time VARCHAR(255), cook_time VARCHAR(255), servingss VARCHAR(255), difficulty_level VARCHAR(255), image_url VARCHAR(255))"
    ingredients = "CREATE TABLE IF NOT EXISTS ingredients (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
    recipe_ingredients = "CREATE TABLE IF NOT EXISTS recipe_ingredients (recipe_id INT, ingredient_id INT, quantity VARCHAR(255), measurement_unit VARCHAR(255), FOREIGN KEY (recipe_id) REFERENCES recipes(id), FOREIGN KEY (ingredient_id) REFERENCES ingredients(id))"
    steps = "CREATE TABLE IF NOT EXISTS steps (id INT AUTO_INCREMENT PRIMARY KEY, recipe_id INT, step_number INT, description VARCHAR(255), FOREIGN KEY (recipe_id) REFERENCES recipes(id))"
    categories = "CREATE TABLE IF NOT EXISTS categories (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
    recipe_categories = "CREATE TABLE IF NOT EXISTS recipe_categories (recipe_id INT, category_id INT, FOREIGN KEY (recipe_id) REFERENCES recipes(id), FOREIGN KEY (category_id) REFERENCES categories(id))"

    # Execute SQL queries to create tables
    cursor.execute(user_data)
    cursor.execute(recipes)
    cursor.execute(ingredients)
    cursor.execute(recipe_ingredients)
    cursor.execute(steps)
    cursor.execute(categories)
    cursor.execute(recipe_categories)
    connection.commit()
    cursor.close()
    connection.close()

# # Call the function to initialize the database
initialize_database()

def dataentry():
    user='''INSERT ignore INTO user_data (name, email, password, phone_number, address) VALUES
    ('John Doe', 'john@example.com', 'password123', '+1234567890', '123 Main St'),
    ('Alice Smith', 'alice@example.com', 'secret456', '+1987654321', '456 Oak St'),
    ('Bob Johnson', 'bob@example.com', 'bobspassword', '+1122334455', '789 Elm St');'''
    
    recipes='''INSERT INTO recipes (name, description, prep_time, cook_time, servingss, difficulty_level, image_url) VALUES
    -- Japanese Dish
    ('Sushi Rolls', 'Traditional Japanese sushi rolls filled with fresh fish, vegetables, and rice', '30 minutes', '0 minutes', '4', 'Easy', 'https://example.com/sushi_rolls.jpg'),
    -- American Dishes
    ('Classic Cheeseburger', 'Iconic American cheeseburger with a juicy beef patty, cheese, lettuce, and tomato', '15 minutes', '10 minutes', '4', 'Easy', 'https://example.com/cheeseburger.jpg'),
    ('Homemade Mac and Cheese', 'Creamy and cheesy American comfort food made with macaroni and a rich cheese sauce', '20 minutes', '25 minutes', '6', 'Easy', 'https://example.com/mac_and_cheese.jpg'),
    -- Desert Dishes
    ('Chocolate Brownies', 'Rich and fudgy chocolate brownies, perfect for dessert', '15 minutes', '30 minutes', '12', 'Intermediate', 'https://example.com/chocolate_brownies.jpg'),
    ('Vanilla Cupcakes', 'Classic vanilla cupcakes topped with creamy frosting', '20 minutes', '20 minutes', '12', 'Intermediate', 'https://example.com/vanilla_cupcakes.jpg'),
    -- Mexican Dish
    ('Chicken Quesadillas', 'Mexican-style quesadillas filled with shredded chicken, cheese, and salsa', '15 minutes', '10 minutes', '4', 'Easy', 'https://example.com/chicken_quesadillas.jpg'),
    -- Indian Dishes
    ('Butter Chicken', 'Creamy and flavorful chicken curry made with butter, tomatoes, and spices', '20 minutes', '30 minutes', '4', 'Intermediate', 'https://example.com/butter_chicken.jpg'),
    ('Paneer Tikka Masala', 'Indian vegetarian dish made with paneer marinated in spices and cooked in a rich tomato-based gravy', '15 minutes', '25 minutes', '4', 'Intermediate', 'https://example.com/paneer_tikka_masala.jpg'),
    ('Vegetable Biryani', 'Fragrant and flavorful rice dish cooked with mixed vegetables and aromatic spices', '20 minutes', '40 minutes', '6', 'Intermediate', 'https://example.com/vegetable_biryani.jpg');
    '''


    steps='''INSERT INTO steps (recipe_id, step_number, description) VALUES
    (1, 1, 'Cook the sushi rice according to the package instructions.'),
    (1, 2, 'Lay a sheet of nori on a bamboo sushi mat, shiny side down.'),
    (1, 3, 'Spread a thin layer of rice over the nori, leaving a 1-inch border at the top.'),
    (1, 4, 'Arrange the filling ingredients in a line across the center of the rice.'),
    (1, 5, 'Roll up the sushi using the bamboo mat, pressing gently to seal the edges.'),
    (2, 1, 'Preheat a grill or skillet over medium-high heat.'),
    (2, 2, 'Season the beef patties with salt and pepper.'),
    (2, 3, 'Cook the patties for 4-5 minutes on each side until cooked through.'),
    (2, 4, 'Toast the burger buns on the grill for 1-2 minutes until golden brown.'),
    (3, 1, 'Cook the macaroni according to the package instructions.'),
    (3, 2, 'In a saucepan, melt the butter over medium heat.'),
    (3, 3, 'Stir in the flour to make a roux, then gradually whisk in the milk.'),
    (3, 4, 'Cook the sauce, stirring constantly, until thickened and smooth.'),
    (3, 5, 'Stir in the cheese until melted and smooth, then add the cooked macaroni and mix well.'),
    (4, 1, 'Preheat the oven to 350°F (175°C).'),
    (4, 2, 'Grease and flour a baking pan.'),
    (4, 3, 'In a mixing bowl, combine the sugar, flour, cocoa powder, and salt.'),
    (4, 4, 'In a separate bowl, whisk together the eggs, oil, and vanilla extract.'),
    (4, 5, 'Gradually add the wet ingredients to the dry ingredients, mixing until well combined.'),
    (4, 6, 'Pour the batter into the prepared pan and smooth the top with a spatula.'),
    (4, 7, 'Bake for 25-30 minutes, or until a toothpick inserted into the center comes out clean.'),
    (4, 8, 'Allow the brownies to cool before cutting into squares.'),
    (5, 1, 'Preheat the oven to 350°F (175°C).'),
    (5, 2, 'Line a muffin tin with paper liners.'),
    (5, 3, 'In a mixing bowl, cream together the butter and sugar until light and fluffy.'),
    (5, 4, 'Beat in the eggs one at a time, then stir in the vanilla extract.'),
    (5, 5, 'Combine the flour, baking powder, and salt; stir into the batter alternately with the milk.'),
    (5, 6, 'Spoon the batter into the prepared muffin cups, filling them about 2/3 full.'),
    (5, 7, 'Bake for 20-25 minutes, or until a toothpick inserted into the center comes out clean.'),
    (5, 8, 'Allow the cupcakes to cool completely before frosting.'),
    (6, 1, 'Heat a skillet over medium heat and add a tortilla.'),
    (6, 2, 'Spread a layer of salsa over half of the tortilla.'),
    (6, 3, 'Top the salsa with shredded chicken and cheese.'),
    (6, 4, 'Fold the other half of the tortilla over the filling and cook until golden brown on both sides.'),
    (6, 5, 'Repeat with the remaining tortillas and filling ingredients.'),
    (7, 1, 'Heat oil in a large skillet over medium-high heat.'),
    (7, 2, 'Add the diced chicken and cook until browned on all sides.'),
    (7, 3, 'Add the onion, garlic, ginger, and spices and cook until fragrant.'),
    (7, 4, 'Stir in the tomato sauce and cream, then simmer until the chicken is cooked through and the sauce has thickened.'),
    (7, 5, 'Stir in the butter and garam masala, then garnish with cilantro before serving.'),
    (8, 1, 'Preheat the grill to medium-high heat.'),
    (8, 2, 'Cut the paneer into cubes and marinate in a mixture of yogurt, spices, and lemon juice.'),
    (8, 3, 'Thread the marinated paneer onto skewers, alternating with bell peppers, onions, and tomatoes.'),
    (8, 4, 'Grill the skewers for 10-12 minutes, turning occasionally, until the paneer is golden brown and the vegetables are tender.'),
    (8, 5, 'Serve the paneer tikka masala hot, garnished with fresh cilantro and lemon wedges.'),
    (9, 1, 'Rinse the basmati rice under cold water until the water runs clear, then soak for 30 minutes.'),
    (9, 2, 'In a large pot, heat ghee over medium heat and add the whole spices.'),
    (9, 3, 'Add the onions and sauté until golden brown, then add the ginger-garlic paste and cook until fragrant.'),
    (9, 4, 'Stir in the mixed vegetables and cook for a few minutes, then add the soaked rice and sauté for 2-3 minutes.'),
    (9, 5, 'Add the water and salt, then bring to a boil. Reduce the heat to low, cover, and simmer for 20-25 minutes, or until the rice is cooked through and the water is absorbed.'),
    (9, 6, 'Fluff the rice with a fork and garnish with chopped cilantro before serving.');
    '''

    ingredients='''INSERT IGNORE INTO ingredients (id, name) VALUES
    (1, 'Fresh fish'),
    (2, 'Vegetables'),
    (3, 'Rice'),
    (4, 'Beef patty'),
    (5, 'Cheese'),
    (6, 'Lettuce'),
    (7, 'Tomato'),
    (8, 'Macaroni'),
    (9, 'Chicken'),
    (10, 'Salsa'),
    (11, 'Chocolate'),
    (12, 'Flour'),
    (13, 'Sugar'),
    (14, 'Vanilla extract'),
    (15, 'Eggs'),
    (16, 'Baking powder'),
    (17, 'Butter'),
    (18, 'Tomatoes'),
    (19, 'Spices'),
    (20, 'Paneer'),
    (21, 'Mixed vegetables');
    '''

    recipe_ingredients='''INSERT IGNORE INTO recipe_ingredients (recipe_id, ingredient_id, quantity, measurement_unit) VALUES
    -- Japanese Dish: Sushi Rolls
    (1, 1, '200', 'grams'),   -- Fresh fish
    (1, 2, '1', ''),           -- Vegetables
    (1, 3, '2', 'cups'),       -- Rice
    -- American Dishes: Classic Cheeseburger
    (2, 4, '4', ''),           -- Beef patty
    (2, 5, '4', ''),           -- Cheese
    (2, 6, '4', 'leaves'),     -- Lettuce
    (2, 7, '4', ''),           -- Tomato
    -- Homemade Mac and Cheese
    (3, 8, '200', 'g'),        -- Macaroni
    (3, 5, '200', 'g'),        -- Cheese
    (3, 17, '2', 'tablespoons'),-- Butter
    -- Desert Dishes: Chocolate Brownies
    (4, 11, '200', 'g'),       -- Chocolate
    (4, 12, '1', 'cup'),       -- Flour
    (4, 13, '1', 'cup'),       -- Sugar
    -- Vanilla Cupcakes
    (5, 12, '1.5', 'cups'),    -- Flour
    (5, 14, '1', 'teaspoon'),  -- Vanilla extract
    (5, 15, '2', ''),          -- Eggs
    -- Mexican Dish: Chicken Quesadillas
    (6, 9, '300', 'g'),        -- Chicken
    (6, 5, '200', 'g'),        -- Cheese
    (6, 10, '1/2', 'cup'),     -- Salsa
    -- Indian Dishes: Butter Chicken
    (7, 9, '500', 'g'),        -- Chicken
    (7, 18, '4', ''),          -- Tomatoes
    (7, 19, '1', 'tablespoon'),-- Spices
    -- Paneer Tikka Masala
    (8, 20, '250', 'g'),       -- Paneer
    (8, 18, '2', ''),          -- Tomatoes
    (8, 19, '2', 'tablespoons'),-- Spices
    -- Vegetable Biryani
    (9, 3, '2', 'cups'),       -- Rice
    (9, 21, '2', 'cups'),      -- Mixed vegetables
    (9, 19, '1', 'tablespoon');-- Spices
    '''

    categories='''INSERT IGNORE INTO categories (name) VALUES
    ('Japanese'),
    ('American'),
    ('Dessert'),
    ('Mexican'),
    ('Indian');
    '''

    recipe_categories='''INSERT INTO recipe_categories (recipe_id, category_id) VALUES
    (1, 1),  -- Sushi Rolls is Japanese
    (2, 3),  -- Classic Cheeseburger is American
    (3, 3),  -- Homemade Mac and Cheese is American
    (4, 3),  -- Chocolate Brownies is Dessert
    (5, 3),  -- Vanilla Cupcakes is Dessert
    (6, 4),  -- Chicken Quesadillas is Mexican
    (7, 5),  -- Butter Chicken is Indian
    (8, 5),  -- Paneer Tikka Masala is Indian
    (9, 5);  -- Vegetable Biryani is Indian
'''


connection=mysql.connector.connect(host='localhost', user='root', password='', database='food_recipie')
cursor=connection.cursor()
cursor.execute("SELECT name,description,servings,difficulty_level,image_url FROM recipes")
    # print(cursor.fetchall())
dishes_list=cursor.fetchall()
dishes = [{'name': row[0], 'description': row[1], 'servings': row[2], 'difficulty_level': row[3], 'image_url': row[4]} for row in dishes_list]
print(len(dishes))
if len(dishes)>12:
    page.append({ "no": 3, "name": "third" })
    print(page)   
else:
    page=[
  { "no": 1, "name": "index" },
  { "no": 2, "name": "second" } 
]
    # dishes=json.dumps(dishes)
@app.route('/index')
def index():
    cursor.execute("SELECT name,description,servings,difficulty_level,image_url FROM recipes")
    # print(cursor.fetchall())
    dishes_list=cursor.fetchall()
    dishes = [{'name': row[0], 'description': row[1], 'servings': row[2], 'difficulty_level': row[3], 'image_url': row[4]} for row in dishes_list]
        # dishes=json.dumps(dishes)
    # cursor.execute("SELECT name,description,servings,difficulty_level,image_url FROM recipes")
    # # print(cursor.fetchall())
    # dishes_list=cursor.fetchall()
    # dishes = [{'name': row[0], 'description': row[1], 'servings': row[2], 'difficulty_level': row[3], 'image_url': row[4]} for row in dishes_list]
    # # dishes=json.dumps(dishes)
    # print(dishes, flush=True)
    return render_template('index.html',dishes=dishes,page=page)

@app.route('/second')
def second():
    cursor.execute("SELECT name,description,servings,difficulty_level,image_url FROM recipes")
    # print(cursor.fetchall())
    dishes_list=cursor.fetchall()
    dishes = [{'name': row[0], 'description': row[1], 'servings': row[2], 'difficulty_level': row[3], 'image_url': row[4]} for row in dishes_list]
    
    # cursor.execute("SELECT name,description,servings,difficulty_level,image_url FROM recipes")
    # # print(cursor.fetchall())
    # dishes_list=cursor.fetchall()
    # dishes = [{'name': row[0], 'description': row[1], 'servings': row[2], 'difficulty_level': row[3], 'image_url': row[4]} for row in dishes_list]
    # # dishes=json.dumps(dishes)
    # print(dishes, flush=True)
    return render_template('second.html',dishes=dishes,page=page)

@app.route('/third')
def third():
    cursor.execute("SELECT name,description,servings,difficulty_level,image_url FROM recipes")
    # print(cursor.fetchall())
    dishes_list=cursor.fetchall()
    dishes = [{'name': row[0], 'description': row[1], 'servings': row[2], 'difficulty_level': row[3], 'image_url': row[4]} for row in dishes_list]
    
    # cursor.execute("SELECT name,description,servings,difficulty_level,image_url FROM recipes")
    # # print(cursor.fetchall())
    # dishes_list=cursor.fetchall()
    # dishes = [{'name': row[0], 'description': row[1], 'servings': row[2], 'difficulty_level': row[3], 'image_url': row[4]} for row in dishes_list]
    # # dishes=json.dumps(dishes)
    # print(dishes, flush=True)
    return render_template('third.html',dishes=dishes,page=page)
@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/next-page')
def next_page():
    recipe_id = request.args.get('index')  # Get the index from the request query parameters
    print("index ",recipe_id)
    connection = mysql.connector.connect(host='localhost', user='root', password='', database='food_recipie')

    cursor = connection.cursor()

    # Retrieve category name
    cursor.execute("SELECT c.name FROM categories c INNER JOIN recipe_categories rc ON c.id = rc.category_id WHERE rc.recipe_id = %s", (recipe_id,))
    category = cursor.fetchone()  # Assuming each recipe belongs to only one category

    # Retrieve recipe ingredients with their names
    cursor.execute("SELECT i.name, ri.quantity, ri.measurement_unit FROM ingredients i INNER JOIN recipe_ingredients ri ON i.id = ri.ingredient_id WHERE ri.recipe_id = %s", (recipe_id,))
    ingredients_list = cursor.fetchall()
    ingredients = [{'name': row[0], 'quantity': row[1], 'measurement_unit': row[2]} for row in ingredients_list]

    # Retrieve recipe steps
    cursor.execute("SELECT step_number, description FROM steps WHERE recipe_id = %s", (recipe_id,))
    steps_list = cursor.fetchall()
    steps = [{'step_number': row[0], 'description': row[1]} for row in steps_list]
    cursor.execute("select prep_time,cook_time from recipes where id=%s",(recipe_id,))
    time=cursor.fetchall()
    time=[{'prep_time': row[0], 'cook_time': row[1]} for row in time]
    cursor.close()
    connection.close()

    return render_template('recipi.html',category=category,ingredients=ingredients,steps=steps,dish=dishes[int(recipe_id)-1],time=time[0])
    
    
def get_recipe_details(recipe_id):
    connection = mysql.connector.connect(host='localhost', user='root', password='', database='food_recipie')
    cursor = connection.cursor()

    # Retrieve category name
    cursor.execute("SELECT c.name FROM categories c INNER JOIN recipe_categories rc ON c.id = rc.category_id WHERE rc.recipe_id = %s", (recipe_id,))
    category = cursor.fetchone()[0]  # Assuming each recipe belongs to only one category

    # Retrieve recipe ingredients with their names
    cursor.execute("SELECT i.name, ri.quantity, ri.measurement_unit FROM ingredients i INNER JOIN recipe_ingredients ri ON i.id = ri.ingredient_id WHERE ri.recipe_id = %s", (recipe_id,))
    ingredients_list = cursor.fetchall()
    ingredients = [{'name': row[0], 'quantity': row[1], 'measurement_unit': row[2]} for row in ingredients_list]

    # Retrieve recipe steps
    cursor.execute("SELECT step_number, description FROM steps WHERE recipe_id = %s", (recipe_id,))
    steps_list = cursor.fetchall()
    steps = [{'step_number': row[0], 'description': row[1]} for row in steps_list]

    cursor.close()
    connection.close()

    return {'category': category, 'ingredients': ingredients, 'steps': steps}

# Example usage:
# recipe_id = 1  # Replace with the desired recipe ID
# recipe_details = get_recipe_details(recipe_id)
# print(recipe_details)
import mysql.connector

# def add_recipe(name, description, prep_time, cook_time, servings, difficulty_level):
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

# Example usage of the add_recipe function
# add_recipe("Spaghetti Carbonara", "Classic Italian pasta dish with eggs, cheese, and bacon.", "15 minutes", "20 minutes", "4", "Medium")




@app.route('/fooditem', methods=['GET','POST'])
def fooditem():
    return render_template('addfood.html')

@app.route('/categories', methods=['GET'])
def categories():
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    category_list = [{'id': row[0], 'name': row[1]} for row in categories]

    # Return the list of dictionaries as a JSON response
    return jsonify(category_list)


@app.route('/regfood', methods =  ['GET','POST'])
def regfood():
    #Data gathering
    name=request.args['name']
    description=request.args['desc']
    prep_time=request.args['prep']
    cook_time=request.args['cook']
    servings=request.args['servings']
    difficulty_level=request.args['difficulty_level']
    image_url=request.args['image_url']
    print(name,description,prep_time,cook_time,servings,difficulty_level,image_url)
    #Data transmission to db
    #  Connect to the MySQL database
    connection = mysql.connector.connect(host='localhost', user='root', password='', database='food_recipie')

        # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

        # Define the SQL query to insert a new recipe
    sql = "INSERT ignore INTO recipes (name, description, prep_time, cook_time, servings, difficulty_level,image_url) VALUES (%s, %s, %s, %s, %s, %s,%s)"

        # Execute the SQL query with the provided parameters
    cursor.execute(sql, (name, description, prep_time, cook_time, servings, difficulty_level,image_url))

        # Commit the transaction to save the changes
    connection.commit()

        # Close the cursor and database connection
    cursor.close()
    connection.close()

    print("Recipe added successfully!")

    msg="Data Saved Successfully"
    #return render_template('register.html')
    resp = make_response(json.dumps(msg))
    
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return resp

@app.route('/regdata', methods =  ['GET','POST'])
def regdata():
    #Data gathering
    nm=request.args['username']
    em=request.args['email']
    ph=request.args['phone']
    pswd=request.args['password']
    addr=request.args['address']
    
    #Data transmission to db
    connection = mysql.connector.connect(host='localhost',database='food_recipie',user='root',password='')
    sqlquery="insert ignore into user_data(name,email,phone_number,password,address) values('"+nm+"','"+em+"','"+ph+"','"+pswd+"','"+addr+"')"
    print(sqlquery)
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    connection.commit() 
    connection.close()
    cursor.close()
    msg="Data Saved Successfully"
    #return render_template('register.html')
    resp = make_response(json.dumps(msg))
    
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return resp



@app.route('/logdata', methods =  ['GET','POST'])
def logdata():
    #Data gathering
    em=request.args['email']
    pswd=request.args['password']

    
    #Data transmission to db
    connection = mysql.connector.connect(host='localhost',database='food_recipie',user='root',password='')
    sqlquery="select count(*) from  user_data where email='"+em+"' and password='"+pswd+"'"
    print(sqlquery)
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    data=cursor.fetchall()
    print(data) 
    connection.close()
    cursor.close()
    msg=""
    if data[0][0]==0:
        msg="Failure"
    else:
        msg="Success"
    
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return msg


if __name__ == '__main__':
    app.run()