# Food Recipe Website

This project is a web application for sharing and discovering food recipes. It is built using Flask and XAMPP.

## Features

- User authentication and authorization
- Recipe creation, editing, and deletion
- Search functionality for recipes
- User profile management

## Technologies Used

- Flask
- XAMPP
- HTML/CSS
- JavaScript
- SQLite (or any other database supported by XAMPP)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/foodrecipe.git
    ```
2. Navigate to the project directory:
    ```bash
    cd foodrecipe
    ```
3. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Configure XAMPP and start Apache and MySQL services.

6. Set up the database:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

7. Run the application:
    ```bash
    flask run
    ```

## Usage

- Open your web browser and go to `http://localhost:5000`.
- Register for a new account or log in with an existing account.
- Start adding and exploring recipes!

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

