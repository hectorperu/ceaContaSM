from django.db import connections
from django.db.utils import OperationalError


def post_TBL_AFCargo(descripcion, idempresa):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(
                "exec spp_Mantenimiento_Tbl_AFCargo @IdCargo=1,@Descripcion=%s,@IdEmpresa=%s,@Estado=1,@modo=1", [descripcion, idempresa])
            return True
    except OperationalError as e:
        return str(e)
