#I below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://timleo:sucksomeDicks0-@timtime.ccqv3rhgwzsj.us-east-2.rds.amazonaws.com/timleo'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://timleo:sucksomeDicks0-@aa1fvq8qseo7j9m.ccqv3rhgwzsj.us-east-2.rds.amazonaws.com:3306/aa1fvq8qseo7j9m'


# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
