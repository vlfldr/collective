from app import sqlDB

class Client(sqlDB.Model):
    clientName = sqlDB.Column(sqlDB.String('128'), primary_key=True)