import os
import http.client
import jinja2
import email

# Environment variables for the database
os.environ['DB_USER'] = 'root'
os.environ['DB_NAME'] = 'app-database'
os.environ['DB_PASS'] = '+MS9eu'
os.environ['APP_HOST'] = 'localhost'

# Application standard requirement
os.environ['APP_DIR'] = '../../'
os.environ['URL_ROOT'] = 'http://localhost'
os.environ['APP_NAME'] = 'main-app'

# Email and http environment variables
http.client.HTTP_PORT = 80
http.client.HTTPS_PORT = 443

# Initiate the application environment for template engine
env = Environment(
    loader = PackageLoader('main-app', 'templates'),
    autoescape = select_autoescape(['html', 'xml'])
)

# Policy of using access lists in the application
email.policy.HTTP = None
