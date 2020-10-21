<capital>Description of the project launch</capital>
1. Clone project from this repository and install required tools
2. In the 'main' folder create local_settings.py and add: 
    1. SECRET_KEY
    2. Information about your Postgresql database:
        1. DATABASE_NAME
        2. DATABASE_USER
        3. DATABASE_PASSWORD
        4. HOST
        5. PORT
3.  Install migrations via 'python manage.py migrate'
