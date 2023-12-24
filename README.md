# itudb2311
Repository for the term project of the course BLG-317E (Database Systems).

## Getting Started with the itudb2311 Project

This section provides a step-by-step guide to get the itudb2311 project up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:
- MySQL
- Python 3
- Flask

```bash
pip install requirements.txt
```


### Setup Instructions

1. **Initialize the MySQL Database:**
   
   - Start your MySQL server.

2. **Configure Application Settings:**

   In the `settings.py` file, update the database connection settings to match your MySQL setup:

   ```python
   # settings.py
   db_user = 'FILL!__your_username__'
   db_password = 'FILL!__your_password__'
   db_host = 'localhost'  # or your database host
   db_name = 'thelook_ecommerce'

3. **Create the Database Tables:**

   In the project directory, run the `create_db.py` script to create the database with the required tables:

   ```bash
   cd path/to/itudb2311
   python create_db.py
   ```

4. **Run The Application:**
    Navigate to the project directory and run the Flask application:
    ```bash
    cd path/to/itudb2311
    python app.py
    ```

    This will start the Flask server. By default, it runs on http://127.0.0.1:5000
    Open your web browser and go to http://127.0.0.1:5000 to view the application.


