## Setup

- Create a `.env` file in the root of your project directory and add the following lines, replacing the placeholder values with your actual configuration details:

```bash
SECRET_KEY=your-256-bit-secret
DB_NAME=cpt
DB_USER=<database_username>
DB_PASSWORD=<database_password>
DB_HOST=<database_host>
DB_PORT=3306 || <database_port>
```

```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
