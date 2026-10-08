import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'buffalo-mbogo-clan-secret-2024'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///buffaloOS.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOTEL_NAME = "Hoima Buffalo Hotel & Business Hub"
    HOTEL_TAGLINE = "From Buffalo Country to Five-Star Comfort"
