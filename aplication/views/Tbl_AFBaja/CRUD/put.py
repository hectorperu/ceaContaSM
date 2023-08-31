from django.db import connections
from django.db.utils import OperationalError


def put_TblAFBaja(id, descripcion):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("exec spp_Mantenimiento_Tbl_AFBaja @IdBaja=%s,@Descripcion=%s,@Estado=1,@modo=2", [
                id,
                descripcion,
            ])
        return True
    except OperationalError as e:
        return str(e)
