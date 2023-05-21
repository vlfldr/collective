from flask import request, render_template
from app import app, db
from app.models import Client
from datetime import datetime

@app.get("/status")
def getStatus():
    req = request.get_json()
    cName = req['clientName']

    flagBackup, registered = False, False

    if db.session.execute(db.select(Client).filter_by(clientName=cName)).scalar():
        registered = True
        #flagBackup = shouldBackup(clients[cName])

    statusData = {
        "clientName": cName,
        "registered": registered,
        "shouldBackup": flagBackup
    }
    return statusData

@app.post("/register")
def register():
    req = request.get_json()
    cName = req['clientName']

    # throw 400 bad request if client name not unique
    if db.session.execute(db.select(Client).filter_by(clientName=cName)).scalar():
        return {"msg": "ERROR_NAME_NOT_UNIQUE"}, 400
    
    # TODO: convert req['backupTime'] to datetime obj
    
    try:
        db.session.add(Client(
                clientName=cName, backupDay=req['backupDay']))
        db.session.commit()
    except:
        return {"msg": "ERROR_CLIENT_DATA_MALFORMED"}, 400
        
    return {"msg": "SUCCESS"}, 201  # 201 = success/created

@app.get("/getconfig")
def getConfig():
    req = request.get_json()
    cName = req['clientName']

    clnt = db.one_or_404(db.select(Client).filter_by(clientName=cName))

    if not clnt:
        return {"msg": "ERROR_CLIENT_NOT_REGISTERED"}, 400
    
    return {
        "clientName": cName, 
        "backupScript": render_template('backup.sh', clientName=cName, clientData=clnt)
    }

@app.put("/updateconfig")
def updateConfig():
    return "Success"

@app.delete("/unregister")
def unregister():
    req = request.get_json()
    cName = req['clientName']

    # abort and return 404 if user not registered
    clnt = db.one_or_404(db.select(Client).filter_by(clientName=cName))

    try:
        db.session.delete(clnt)
        db.session.commit()
    except:
        return {"msg": "DATABASE_ERROR"}, 500

    return {"msg": "SUCCESS"}

@app.get('/')
def home():
    return render_template('home.html', 
            clients=db.session.execute(db.select(Client)).scalars())

