from django.db import connections
from django.db.utils import OperationalError


def get_Tbl_AFCargo():
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("select *from Tbl_AFCargo")
            rows = cursor.fetchall()
            data = []
            for row in rows:
                data.append({
                    'idcargo': row[0],
                    'descripcion': row[1],
                    'idempresa': row[2],
                    'estado': row[3]
                })
            return data
    except OperationalError as e:
        return str(e)


def getbyid_Tbl_AFCargo(id):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("select *from Tbl_AFCargo where idcargo=%s", [id])
            rows = cursor.fetchall()
            data = []
            for row in rows:
                data.append({
                    'idcargo': row[0],
                    'descripcion': row[1],
                    'idempresa': row[2],
                    'estado': row[3]
                })
                return data
    except OperationalError as e:
        return str(e)
