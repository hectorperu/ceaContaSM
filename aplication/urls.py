from django.urls import path, include
from .views.dbCreatetor.dbCreator import *
from .views.TblTipoEmpresa.TblTipoEmpresa import *
from .views.MovContablesDNoDomici.MovContablesDNoDomici import MovContablesDNoDomici
from .views.tbl_MovimientoCajaC.tbl_MovimientoCajaC import tbl_MovimientoCajaC
from .views.Tbl_AFBaja.Tbl_AFBaja import Tbl_AFBaja
from .views.Tbl_AFCargo.Tbl_AFCargo import Tbl_AFCargo

urlpatterns = [
    path('api/tenant/<str:nombre>', TenantCreator.as_view(), name='api_nombre'),
    path('api/tipoEmpresa/', TblTipoEmpresa.as_view(), name='api_nombre'),
    path('api/tipoEmpresa/<int:id>', TblTipoEmpresa.as_view(), name='api_nombre'),
    path('api/movcontablesdnodomici/',
         MovContablesDNoDomici.as_view(), name='api_nombre'),
    path('api/movcontablesdnodomici/<int:id>',
         MovContablesDNoDomici.as_view(), name='api_nombre'),
    path('api/tbl_MovimientoCajaC/', tbl_MovimientoCajaC.as_view(),
         name='api_tbl_MovimientoCajac'),
    path('api/tbl_MovimientoCajac/<int:id>', tbl_MovimientoCajaC.as_view(),
         name='api_tbl_MovimientoCajacyid'),
    path('api/Tbl_AFBaja/', Tbl_AFBaja.as_view(), name='api_Tbl_AfBaja'),
    path('api/Tbl_AFBaja/<int:id>', Tbl_AFBaja.as_view(), name='api_Tbl_Afbaja'),
    path('api/Tbl_AFCargo/', Tbl_AFCargo.as_view(), name='api_Tbl_AFCargo'),
    path('api/Tbl_AFCargo/<int:id>', Tbl_AFCargo.as_view(), name='api_Tbl_AFCargo'),
]
