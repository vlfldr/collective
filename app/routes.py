from flask import request, render_template
from app import app, sqlDB
from app.models import Client
from app.tempModel import clients, shouldBackup  # temporary data models

@app.get("/status")
def getStatus():
    req = request.get_json()
    cName = req['clientName']

    flagBackup, registered = False, False

    if cName in clients:
        registered = True
        flagBackup = shouldBackup(clients[cName])

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

    if cName in clients:
        return {"msg": "ERROR_NAME_NOT_UNIQUE"}, 400    # 400 = bad request
        
    try:
        clients[cName] = req
        sqlDB.session.add(Client(clientName=cName))
        sqlDB.session.commit()
    except:
        return {"msg": "ERROR_CLIENT_DATA_MALFORMED"}, 400

    return {"msg": "SUCCESS"}, 201  # 201 = success/created

@app.get("/getconfig")
def getConfig():
    req = request.get_json()
    cName = req['clientName']

    if cName not in clients:
        return {"msg": "ERROR_CLIENT_NOT_REGISTERED"}, 400
    
    clnt = clients[cName]

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

    if cName not in clients:
        return {"msg": "ERROR_CLIENT_NOT_REGISTERED"}, 400    # 400 = bad request

    clients.pop(cName) 

    return {"msg": "SUCCESS"}

@app.get('/')
def home():
    return render_template('home.html', clients=clients)

