# Imports:
# Import the Flet library and alias it as 'ft'
import flet as ft

# Import the SQLite module for database operations
import sqlite3

# Import the random module for generating random values
import random


# Main Function:

# The main function is the entry point of the application
# It sets up the user interface using Flet elements and defines window properties
def main(page: ft.Page):
    # Set the title, theme, alignment, width, height, and other properties of the application window
    page.title = "Users CRM"
    page.theme_mode = "light"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False

    # Database Initialization:
    # The register function handles user registration and database interaction
    def register(e):
        # Connect to the SQLite database (or create it if not exists)
        db = sqlite3.connect("users.db")
        cursor = db.cursor()

        # Create the 'users' table if it doesn't exist
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER NOT NULL,
                    username TEXT,
                    password TEXT,
                    isAdmin BOOLEAN,
                    age INT
                )''')

        # Insert a new user into the 'users' table with random values
        cursor.execute(
            f"INSERT INTO users VALUES({random.randint(1, 999999)}, "
            f"'{user_login_text_field.value}', '{password_text_field.value}', "
            f"{is_admin_checkbox.value}, {int(age_text_field.value)})")

        # Commit changes and close the database connection
        db.commit()
        db.close()

        # Reset input fields and update the page
        user_login_text_field.value = ''
        password_text_field.value = ''
        is_admin_checkbox.value = False
        age_text_field.value = ''
        registration_btn.disabled = True
        page.update()

    # Validation Function:
    # The validate function is called when input fields change to enable/disable the registration button
    def validate(e):
        pass
        # Enable the registration button if both username and password fields have values
        if all([user_login_text_field.value, password_text_field.value, age_text_field.value]):
            registration_btn.disabled = False
        # Disable the registration button if any field is empty
        else:
            registration_btn.disabled = True
        # Update the page to reflect changes
        page.update()

    # UI Elements:
    # Create various UI elements using Flet library
    user_login_text_field = ft.TextField(label="Username", width=200, on_change=validate)
    password_text_field = ft.TextField(label="Password", width=200, on_change=validate, password=True)
    is_admin_checkbox = ft.Checkbox(label="Admin User?", value=False)
    age_text_field = ft.TextField(label="Age", text_align=ft.TextAlign.CENTER, width=100, on_change=validate)
    registration_btn = ft.OutlinedButton(text="Add User", width=200, on_click=register, disabled=True)

    # Organize UI elements in rows and columns
    page.add((
        ft.Row([
            ft.Column([
                ft.Text("User Registration"),
                user_login_text_field,
                password_text_field,
                age_text_field,
                is_admin_checkbox,
                registration_btn
            ])
        ], alignment=ft.MainAxisAlignment.CENTER)
    ))


# Running the Application:
# Launch the Flet application with the main function as the target
ft.app(target=main)
