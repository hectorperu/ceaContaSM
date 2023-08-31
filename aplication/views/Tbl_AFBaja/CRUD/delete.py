from django.db import connections
from django.db.utils import OperationalError


def delete_TblAFBaja(codigo):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("exec spp_mantenimiento_tbl_AFBaja @IdBaja=%s, @Descripcion='' ,@Estado=0, @Modo=3", [
                codigo
            ])
        return True
    except OperationalError as e:
        return str(e)
