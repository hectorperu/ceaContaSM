from django.db import connections
from django.db.utils import OperationalError


def delete_TblAFCargo(codigo):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("exec spp_Mantenimiento_Tbl_AFCargo @IdCargo=%s,@Descripcion='',@IdEmpresa=0,@Estado=0,@modo=3", [
                codigo
            ])
        return True
    except OperationalError as e:
        return str(e)
