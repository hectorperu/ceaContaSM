from django.db import connections
from django.db.utils import OperationalError


def get_tbl_MovimientoCajaC():
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("select *from tbl_MovimientoCajaC")
            rows = cursor.fetchall()
            data = []
            for row in rows:
                data.append({
                    'idmovimientocajac': row[0],
                    'anio': row[1],
                    'mes': row[2],
                    'zona': row[3],
                    'codunidadeconomica': row[4],
                    'nrodoc': row[5],
                    'fechacontable': row[6],
                    'codmgc': row[7],
                    'glosa': row[8],
                    'rucemitido': row[9],
                    'codigoctabancaria': row[10],
                    'codigotipodocpago': row[11],
                    'nrodocpago': row[12],
                    'monto': row[13],
                    'transferido': row[14],
                    'correlativo': row[15],
                    'estado': row[16],
                    'transferidoant': row[17],
                })
    except OperationalError as e:
        return str(e)


def get_byid_MovimientoCajaC(id):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(
                "select *from tbl_MovimientoCajaC WHERE idMovimientoCajaC=%s", [id])
            rows = cursor.fetchall()
            data = []
            for row in rows:
                data.append({
                    'idmovimientocajac': row[0],
                    'anio': row[1],
                    'mes': row[2],
                    'zona': row[3],
                    'codunidadeconomica': row[4],
                    'nrodoc': row[5],
                    'fechacontable': row[6],
                    'codmgc': row[7],
                    'glosa': row[8],
                    'rucemitido': row[9],
                    'codigoctabancaria': row[10],
                    'codigotipodocpago': row[11],
                    'nrodocpago': row[12],
                    'monto': row[13],
                    'transferido': row[14],
                    'correlativo': row[15],
                    'estado': row[16],
                    'transferidoant': row[17],

                })
            return data
    except OperationalError as e:
        return str(e)
