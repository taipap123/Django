import json
from ..Database import DBconnect

cnn = DBconnect.MyConnect()

def getListItem():
    try:
        sql = "SELECT * FROM myapp_sanpham WHERE idLoaiSP = 28"
        data = cnn.executeQuery(sql)
        response = json.dumps(data)
    except:
        response = json.dumps([{}])
    return response