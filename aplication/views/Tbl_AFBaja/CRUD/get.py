from django.db import connections
from django.db.utils import OperationalError


def get_TblAFBaja():
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM Tbl_AFBaja")
            rows = cursor.fetchall()
            data = []
            for row in rows:
                data.append(
                    {'idbaja': row[0], 'descripcion': row[1], 'estado': row[2]})
            return data
    except OperationalError as e:
        return str(e)


def get_byidTblAFBaja(id):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(
                "SELECT * FROM Tbl_AFBaja WHERE IdBaja=%s", [id]
            )
            rows = cursor.fetchall()
            data = []
            for row in rows:
                data.append(
                    {'idbaja': row[0], 'descripcion': row[1], 'estado': row[2]})
            return data
    except OperationalError as e:
        return str(e)
