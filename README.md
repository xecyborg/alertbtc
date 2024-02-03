# Crypto Price Alert App

## Overview

This Django application allows users to set cryptocurrency Bitcoin price alerts. When the specified cryptocurrency price reaches the user-defined target, the application sends an email alert to the user.

## Setup

### Requirements

- Docker
- Docker Compose

### Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/xecyborg/alertbtc.git
   
2. Navigate to the project directory:
   ```bash
   cd your-crypto-price-alert-app

3. Create a .env file in the project root with the following content:
   ```bash
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password

4. Build and run the Docker containers:
   ```bash
   docker-compose up --build
This command will build the images and start the containers. The application will be accessible at http://localhost:8000/.

# AlertBTC App API Documentation

## Authentication

This application uses Djoser for authentication. You can use the Djoser authentication endpoints to register, log in, and obtain authentication tokens.

- **Register User:**
  - **Endpoint:** `/auth/register/`
  - **Method:** POST
  - **Description:** Register a new user account.
  - **Request Body:**
    ```json
    {
      "username": "your_username",
      "email": "your_email@example.com",
      "password": "your_password"
    }
    ```
    Replace `your_username`, `your_email@example.com`, and `your_password` with your desired values.

- **Log In:**
  - **Endpoint:** `/auth/login/`
  - **Method:** POST
  - **Description:** Log in with your credentials and obtain an authentication token.
  - **Request Body:**
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
    Replace `your_username` and `your_password` with your registered credentials.

- **Obtain Token:**
  - **Endpoint:** `/auth/token/login/`
  - **Method:** POST
  - **Description:** Obtain an authentication token using your credentials.
  - **Request Body:**
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
    Replace `your_username` and `your_password` with your registered credentials.

## Alerts API

### Create Alert

- **Endpoint:** `/alerts/create/`
- **Method:** POST
- **Description:** Create a new price alert.
- **Authentication:** Bearer Token (Include the obtained authentication token in the request header)
- **Request Body:**
  ```json
  {
    "target_price": 50000.00
  }

### Delete Alert

- **Endpoint:** `/alerts/delete/<int:pk>/`
- **Method:** DELETE
- **Description:** Delete an existing price alert by ID.
- **Authentication:** Bearer Token (Include the obtained authentication token in the request header)

# Contributer
Ravi Raj Singh

### List Alerts

- **Endpoint:** `/alerts/list/`
- **Method:** GET
- **Description:** Retrieve a list of all price alerts for the authenticated user.
- **Authentication:** Bearer Token (Include the obtained authentication token in the request header)
   
