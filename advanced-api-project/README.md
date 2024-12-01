# Advanced API Project

This project demonstrates the use of Django REST Framework to build advanced APIs with features like filtering, searching, and ordering, as well as comprehensive unit tests for CRUD operations and API functionalities.

## Features

- CRUD operations for the `Book` model
- Filtering, searching, and ordering capabilities
- Permissions and authentication to secure API endpoints
- Comprehensive unit tests to ensure API reliability

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourGitHubUsername/Alx_DjangoLearnLab.git
   cd advanced-api-project

2. Install dependencies:
   pip install -r requirements.txt

3. Apply migrations:
   python manage.py migrate

4. Run the development server:
   python manage.py runserver



Running Unit Tests
To run the unit tests for the Book API, use the following command:
   python manage.py test api00


What the Tests Cover

Create: Ensure books can be created successfully via the API.
Retrieve: Test listing and retrieving book details.
Update: Validate updates to book records.
Delete: Check that books are deleted correctly.
Filtering, Searching, and Ordering: Confirm these features work as intended.
Permissions: Verify that unauthenticated users cannot perform restricted actions.
Usage
Use tools like Postman or curl to interact with the API endpoints.
Example endpoints:
GET /api/books/ - List all books
POST /api/books/ - Create a new book
GET /api/books/<id>/ - Retrieve a single book
PUT /api/books/<id>/ - Update a book
DELETE /api/books/<id>/ - Delete a book
