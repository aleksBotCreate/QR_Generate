import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('TOKEN')
