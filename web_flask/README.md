# 0x04. AirBnB clone - Web framework

## Overview
Briefly describe the purpose and functionality of the web application.

## Project Structure
1. **app.py**: Main application file where Flask app is created and routes are defined.
2. **templates/**: Folder containing HTML templates for rendering pages.
3. **static/**: Folder for static files like CSS, JavaScript, and images.
4. **forms.py**: File for defining Flask forms using WTForms library.
5. **utils.py**: Utility functions or helper functions.
6. **requirements.txt**: File listing all Python dependencies for the project.

## Installation
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv_name`.
3. Activate the virtual environment: `source venv_name/bin/activate` (Unix) or `venv_name\Scripts\activate` (Windows).
4. Install dependencies: `pip install -r requirements.txt`.

## Usage
1. Run the Flask application: `python app.py`.
2. Access the application in your browser at `http://localhost:5000`.

## Routing
- **URL Creation**: Define routes in `app.py` using decorators like `@app.route('/route_name')`.
- **HTTP Methods**: Use different HTTP methods like `GET`, `POST`, `PUT`, `DELETE` for handling requests.
- **Route Parameters**: Capture dynamic parts of the URL using `<variable_name>` in routes, accessed via `request.args` or `request.form`.

## Templates
- **Jinja2 Templating**: Use templates in `templates/` folder for rendering dynamic HTML pages.
- **Template Inheritance**: Create base templates (`base.html`) and extend them in child templates for DRY code.

## Forms
- **WTForms Integration**: Define forms in `forms.py` using WTForms library for form validation and data handling.
- **Form Rendering**: Render forms in templates using Jinja2 to create input fields, buttons, etc.

## Sessions and Cookies
- **Session Management**: Use Flask `session` object to store user-specific data across requests.
- **Cookie Handling**: Set and get cookies using `response.set_cookie()` and `request.cookies`.

## Variable Rules
- **Dynamic Routes**: Use variable rules in routes (`<variable_name>`) to create dynamic URLs.
- **URL Building**: Generate URLs dynamically in templates using `url_for()` function.

## Context Variables
- **Global Context**: Use `context processors` to inject variables into templates globally, available in all templates.
- **Request Context**: Access request-specific data like cookies, form data, etc., using `request` object.


