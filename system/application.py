# Application importation and usage loaders
import config
from ViewModel import *
from View import *
from Model import *

# Application importation and using emails behaviors
import sys
import tempfile
import mimetypes
import webbrowser

# Import the email modules we'll need
from email.parser import BytesParser, Parser
from email.policy import default

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Import the email modules we'll need
from email import policy
from email.parser import BytesParser

# An imaginary module that would make this work and be safe.
from imaginary import magic_html_parser


# Application most assemblying engine file
application = new Dispatcher()
