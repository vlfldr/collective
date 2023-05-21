from app import db
from datetime import datetime   # all dates in UTC. converted in client to user tz

class Client(db.Model):
    clientID = db.Column(db.Integer, primary_key=True)

    clientName  = db.Column(db.String(128), index=True, unique=True)
    backupDay   = db.Column(db.String(10))
    backupTime  = db.Column(db.DateTime)
    lastBackup  = db.Column(db.DateTime)

class Directory(db.Model):
    directoryID = db.Column(db.Integer, primary_key=True)
    clientID = db.Column(db.Integer, db.ForeignKey('client.clientID'))

    path = db.Column(db.String(1024))
    action = db.Column(db.String(1))    # B for backup, E for exclude



# def shouldBackup(client):
#     if client.get('lastBackup', '') == '':
#         return True
    
#     schedule = client.get('backupDay')

#     #if schedule == 'daily' and (it's 24h or longer since lastBackup)

#     #elif schedule is int AND
#     #   (it's that day of the month OR the last day of the month) AND
#     #   (it's backupTime OR past backupTime) THEN backup

#     # else [weekly]

#     return False