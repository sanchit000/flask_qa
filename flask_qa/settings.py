

import os
"""
Setup the DB variable from env file
"""
SQLALCHEMY_DATABASE_URI = 'postgres://rwcfgoyqzjbckz:c65fba435b820fc5037fd3af33ce76cb5ac53a7aa1e8075ed1f3a8567875f8ee@ec2-18-215-41-121.compute-1.amazonaws.com:5432/d9717nnm2u0c14'
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False