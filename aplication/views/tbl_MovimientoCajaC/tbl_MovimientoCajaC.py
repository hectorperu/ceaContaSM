from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import OperationalError
from aplication.serializers import TblMovimientocajacSerializer
from ..tbl_MovimientoCajaC.CRUD.get import get_tbl_MovimientoCajaC, get_byid_MovimientoCajaC


class tbl_MovimientoCajaC (APIView):
    def get(self, request, id=None):
        if id is None:
            try:
                data = get_tbl_MovimientoCajaC()
                serializer = TblMovimientocajacSerializer(data, many=True)
                return Response(serializer.data, status=200)
            except OperationalError as e:
                return Response(f"Error al conectar a la nueva base de datos: {str(e)}", status=500)
        else:
            try:
                data = get_byid_MovimientoCajaC(id)
                serializer = TblMovimientocajacSerializer(data, many=True)
                return Response(serializer.data, status=200)
            except OperationalError as e:
                return Response(f"Error al conectar a la nueva base de datos: {str(e)}", status=500)

    def post(self, request):
        serializer = TblMovimientocajacSerializer(data=request.data)
        if serializer.is_valid():
            anio = request.data.get('anio')
            mes = request.data.get('mes')
            zona = request.data.get('zona')
            codunidadeconomica = request.data.get('codunidadeconomica')
            nrodoc = request.data.get('nrodoc')
            fechacontable = request.data.get('fechacontable')
            codmgc = request.data.get('codmgc')
            glosa = request.data.get('glosa')
            rucemitido = request.data.get('rucemitido')
            codigoctabancaria = request.data.get('codigoctabancaria')
            codigotipodocpago = request.data.get('codigotipodocpago')
            nrodocpago = request.data.get('nrodocpago')
            monto = request.data.get('monto')
            transferido = request.data.get('transferido')
            correlativo = request.data.get('correlativo')
            estado = request.data.get('estado')
            transferidoant = request.data.get('transferidoant')

            # result =
            # if result == True:
            #     return Response({"message": "data created successful"}, status=200)
            # else:
            #     return Response(f"Error al conectar a la nueva base de datos: {result}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=400)

    # def put(self,request,id=None):
    #     if id is None:
    #           return Response({"message":"Debe especificar un id"},status=400)
    #     else:
    #         serializer=  MovcontablesdnodomiciSerializer(data=request.data)
    #         if serializer.is_valid():
    #             Movcontable_d = request.data.get('Movcontable_d')
    #             CodUnidadEconomica = request.data.get('CodUnidadEconomica')
    #             TipoDocCredFiscal = request.data.get('TipoDocCredFiscal')
    #             NroDocDUA = request.data.get('NroDocDUA')
    #             AnioDuaCredFiscal = request.data.get('AnioDuaCredFiscal')
    #             MontoRetIGV = request.data.get('MontoRetIGV')
    #             Pais = request.data.get('Pais')
    #             NombreNoDomiciliado = request.data.get('NombreNoDomiciliado')
    #             RentaBruta = request.data.get('RentaBruta')
    #             DeduccionCosto = request.data.get('DeduccionCosto')
    #             RentaNeta = request.data.get('RentaNeta')
    #             TasaRetencion = request.data.get('TasaRetencion')
    #             ImpuestoRetenido = request.data.get('ImpuestoRetenido')
    #             Convenio2Imposicion = request.data.get('Convenio2Imposicion')
    #             TipoRenta = request.data.get('TipoRenta')
    #             AplicaArt76 = request.data.get('AplicaArt76')
    #             result =  put_MovContablesDNoDomici(
    #                 id,Movcontable_d, CodUnidadEconomica, TipoDocCredFiscal,
    #                 NroDocDUA, AnioDuaCredFiscal, MontoRetIGV, Pais, NombreNoDomiciliado, RentaBruta, DeduccionCosto,
    #                 RentaNeta, TasaRetencion, ImpuestoRetenido, Convenio2Imposicion, TipoRenta, AplicaArt76)
    #             if result==True:
    #                 return Response({"message":"data updated successful"}, status=200)
    #             else :
    #                 return Response(f"Error al conectar a la nueva base de datos: {result}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #         else:
    #             return Response(serializer.errors, status=400)
    # def delete(self,request,id=None):
    #     if id is None:
    #         return Response({"message":"Debe especificar un id"},status=400)
    #     else:
    #         if delete_MovContablesDNoDomici(id)==True:
    #             return Response({"message":"data deleted successful"}, status=200)
    #         else:
    #             return Response(f"Error al conectar a la nueva base de datos: {delete_MovContablesDNoDomici(id)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
