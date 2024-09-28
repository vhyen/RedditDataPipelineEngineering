import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

# Reddit API Configs
SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

# Database Configs
DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USER = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')

# Airflow Configs
INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')

# Reddit processed fields of post
POST_FIELDS = (
    'id', 
    'title',
    'selftext',
    'score',
    'num_comments',
    'author', 
    'created_utc',
    'url',
    'upvote_ratio',
    'over_i8',
    'edited',
    'spoiler',
    'stickied'
)
