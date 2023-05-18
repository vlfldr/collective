# backupDay values:
#   daily: back up once per day
#   Monday/Tuesday/etc: back up once per week
#   1-31: back up once monthly on day of the month (or last day)

clients = {
    "laptop": {
      "backupDay": "daily",     
      "backupTime": "5:00AM",
      "lastBackup": "",
      "backupDirs": ["/home/user/photos", "/home/user/notes"],
      "excludeDirs": ["/home/*/Cache", "/home/user/notes/secrets"]
    },
    "desktop": {
      "backupDay": "Sunday",
      "backupTime": "11:00PM",
      "lastBackup": "",
      "backupDirs": ["/home/server/docker-data", "/home/server/.mozilla"],
      "excludeDirs": ["/home/*/Cache", "/home/user/.mozilla/cache"]
    }
}

def shouldBackup(client):
    if client.get('lastBackup', '') == '':
        return True
    
    schedule = client.get('backupDay')

    #if schedule == 'daily' and (it's 24h or longer since lastBackup)

    #elif schedule is int AND
    #   (it's that day of the month OR the last day of the month) AND
    #   (it's backupTime OR past backupTime) THEN backup

    # else [weekly]

    return False