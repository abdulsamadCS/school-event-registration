# School Events Registration Web Application

This is a Django web application for managing and registering school extracurricular activities.

## Prerequisites

- Python
- pip

## Quick Start

1. Clone the repository:

    ```bash
    git clone https://github.com/abdulsamadCS/school-event-registration.git
    ```

2. Navigate to the project directory:

    ```bash
    cd school-event-registration
    cd event_registration
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

2. Create a demo superuser account:

    ```bash
    python manage.py create_demo_superuser
    ```

    The demo superuser credentials are as follows:
   - Username: `demo_user`
   - Password: `demo_password`

3. Run the development server:

    ```bash
    python manage.py runserver
    ```

The application will be accessible at [http://localhost:8000/](http://localhost:8000/).

## Accessing the Application

1. Navigate to [http://localhost:8000/](http://localhost:8000/).
2. Log in using the demo superuser credentials provided earlier.

## Custom Admin Interface

The application uses a custom admin interface to display only the "Event" and "Participant" models. The default Django admin interface includes "Users" and "Groups" which are not relevant to this application.

## Importing Additional Data

1. In the admin interface, you'll find "Events" and "Participants" sections.
2. Use the "Import" button to bulk import events and participants from CSV files.
