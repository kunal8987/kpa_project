# KPA API Development

Below is a detailed guide on how to implement the two selected APIs using Django REST Framework (DRF).

Backend Assignment: API Development Task with Django REST Framework
Overview
This assignment involves implementing two APIs from a provided Postman collection using Django REST Framework. The APIs will interact with a PostgreSQL database and integrate with a given frontend codebase.

Selected APIs
Create User API (POST)

Endpoint: /api/users/
Functionality: Create a new user in the database.
Request Body: JSON containing user details.
Response: Confirmation of user creation with user ID.
Get User Details API (GET)

Endpoint: /api/users/{id}/
Functionality: Retrieve user details based on the user ID.
Response: JSON containing user details.

## Setup Instructions
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up PostgreSQL and update the database settings in `settings.py`.
4. Run migrations using `python manage.py migrate`.
5. Run the application using `python manage.py runserver`.

## Technologies Used
- Django
- Django REST Framework
- PostgreSQL

## Implemented APIs
1. **Create User API**
   - Method: POST
   - Endpoint: `/api/users/`
   - Description: Creates a new user.

2. **Get User Details API**
   - Method: GET
   - Endpoint: `/api/users/{id}/`
   - Description: Retrieves user details by ID.

## Limitations
- The application does not include authentication.
- Error handling is basic and can be improved.