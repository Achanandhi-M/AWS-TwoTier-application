
## This project is based on Flask. The flask server is deployed in the (Amazon EC2) the flask serves the HTML form, and when the user enters the data in the form the data will be stored inside Amazon RDS(Database)
![Screenshot from 2024-02-29 16-24-48](https://github.com/Achanandhi-M/AWS-TwoTier-application/assets/110651321/bb7f0d57-1fa2-46bb-b3e8-79bd75df3501)


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Features

- **User Input Form**: Users can submit their name, favorite quote, and advice through a form.
- **Database Integration**: Data submitted by users is stored in a PostgreSQL database hosted on Amazon RDS.
- **Dynamic Responses**: After submitting the form, users are redirected to a response page where they can see a confirmation message.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Achanandhi-M/AWS-TwoTier-application.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AWS-TwoTier-application
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```bash
   python3 app.py
   ```

5. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/) to access the application.

## Usage

1. Fill out the form with your name, favorite quote, and advice.
2. Click the "Submit" button to submit the form.
3. You will be redirected to a response page where you can see a confirmation message.

## Dependencies

- Flask: [Flask](https://pypi.org/project/Flask/) is a lightweight WSGI web application framework in Python.
- psycopg2: [psycopg2](https://pypi.org/project/psycopg2/) is a PostgreSQL adapter for the Python programming language.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.
