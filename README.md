# CRUD Mastery CRM Application

This project is a CRUD (Create, Read, Update, Delete) Mastery application built with Django. It serves as a CRM (Customer Relationship Management) system to help manage customer information efficiently. This project was undertaken to practice and master CRUD operations in Django.

## Features

- Create, Read, Update, Delete (CRUD) operations for managing customers
- User authentication (Sign up, Log in)
- Responsive design with Bootstrap and Bootswatch
- Enhanced forms with Django Crispy Forms
- Font Awesome icons integration
- Emoji support for better user interaction

## Technologies Used

- **Django**: Backend framework for building the application
- **Bootstrap**: Frontend framework for responsive design
- **Bootswatch**: Themes for Bootstrap
- **Django Crispy Forms**: Enhanced form rendering
- **Font Awesome**: Icons for better UI
- **Get Emoji**: Emojis for interactive UI

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or higher

### Installation

1. **Clone the repository:**
   

2. **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the development server:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

5. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **User Authentication:**
    - Sign up for a new account
    - Log in with existing credentials
- **Customer Management:**
    - Create a new customer
    - View a list of customers
    - Update customer information
    - Delete a customer

## Customization

This project can be customized further by adding more features or enhancing existing ones. Feel free to fork the repository and make your changes.

## Resources

- [Bootswatch](https://bootswatch.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/)
- [Font Awesome](https://fontawesome.com/v4/icons/)
- [Get Emoji](https://getemoji.com/)

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
