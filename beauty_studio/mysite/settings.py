import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-...')

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
