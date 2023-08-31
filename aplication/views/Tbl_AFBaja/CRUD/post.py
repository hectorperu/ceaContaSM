from django.db import connections
from django.db.utils import OperationalError


def post_TblAFBaja(descripcion):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("exec spp_Mantenimiento_Tbl_AFBaja @IdBaja=1,@Descripcion=%s,@Estado=1,@modo=1", [
                descripcion,
            ])
        return True
    except OperationalError as e:
        return str(e)
