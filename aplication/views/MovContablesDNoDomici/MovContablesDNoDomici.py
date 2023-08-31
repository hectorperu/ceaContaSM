from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import OperationalError
from aplication.serializers import MovcontablesdnodomiciSerializer
from ..MovContablesDNoDomici.CRUD.get import get_MovContablesDNoDomici, get_byid_MovContablesDNoDomici
from ..MovContablesDNoDomici.CRUD.post import post_MovContablesDNoDomici
from ..MovContablesDNoDomici.CRUD.put import put_MovContablesDNoDomici
from ..MovContablesDNoDomici.CRUD.delete import delete_MovContablesDNoDomici


class MovContablesDNoDomici (APIView):
    def get(self, request, id=None):
        if id is None:
            try:
                data = get_MovContablesDNoDomici()
                serializer = MovcontablesdnodomiciSerializer(data, many=True)
                return Response(serializer.data, status=200)
            except OperationalError as e:
                return Response(f"Error al conectar a la nueva base de datos: {str(e)}", status=500)
        else:
            try:
                data = get_byid_MovContablesDNoDomici(id)
                serializer = MovcontablesdnodomiciSerializer(data, many=True)
                return Response(serializer.data, status=200)
            except OperationalError as e:
                return Response(f"Error al conectar a la nueva base de datos: {str(e)}", status=500)

    def post(self, request):
        serializer = MovcontablesdnodomiciSerializer(data=request.data)
        if serializer.is_valid():
            movcontable_d = request.data.get('movcontable_d')
            codunidadeconomica = request.data.get('codunidadeconomica')
            tipodoccredfiscal = request.data.get('tipodoccredfiscal')
            nrodocdua = request.data.get('nrodocdua')
            anioduacredfiscal = request.data.get('anioduacredfiscal')
            montoretigv = request.data.get('montoretigv')
            pais = request.data.get('pais')
            nombrenodomiciliado = request.data.get('nombrenodomiciliado')
            rentabruta = request.data.get('rentabruta')
            deduccioncosto = request.data.get('deduccioncosto')
            rentaneta = request.data.get('rentaneta')
            tasaretencion = request.data.get('tasaretencion')
            impuestoretenido = request.data.get('impuestoretenido')
            convenio2imposicion = request.data.get('convenio2imposicion')
            tiporenta = request.data.get('tiporenta')
            aplicaart76 = request.data.get('aplicaart76')
            result = post_MovContablesDNoDomici(movcontable_d, codunidadeconomica, tipodoccredfiscal,
                                                nrodocdua, anioduacredfiscal, montoretigv, pais, nombrenodomiciliado, rentabruta, deduccioncosto,
                                                rentaneta, tasaretencion, impuestoretenido, convenio2imposicion, tiporenta, aplicaart76)
            if result == True:
                return Response({"message": "data created successful"}, status=200)
            else:
                return Response(f"Error al conectar a la nueva base de datos: {result}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, id=None):
        if id is None:
            return Response({"message": "Debe especificar un id"}, status=400)
        else:
            serializer = MovcontablesdnodomiciSerializer(data=request.data)
            if serializer.is_valid():
                Movcontable_d = request.data.get('Movcontable_d')
                CodUnidadEconomica = request.data.get('CodUnidadEconomica')
                TipoDocCredFiscal = request.data.get('TipoDocCredFiscal')
                NroDocDUA = request.data.get('NroDocDUA')
                AnioDuaCredFiscal = request.data.get('AnioDuaCredFiscal')
                MontoRetIGV = request.data.get('MontoRetIGV')
                Pais = request.data.get('Pais')
                NombreNoDomiciliado = request.data.get('NombreNoDomiciliado')
                RentaBruta = request.data.get('RentaBruta')
                DeduccionCosto = request.data.get('DeduccionCosto')
                RentaNeta = request.data.get('RentaNeta')
                TasaRetencion = request.data.get('TasaRetencion')
                ImpuestoRetenido = request.data.get('ImpuestoRetenido')
                Convenio2Imposicion = request.data.get('Convenio2Imposicion')
                TipoRenta = request.data.get('TipoRenta')
                AplicaArt76 = request.data.get('AplicaArt76')
                result = put_MovContablesDNoDomici(
                    id, Movcontable_d, CodUnidadEconomica, TipoDocCredFiscal,
                    NroDocDUA, AnioDuaCredFiscal, MontoRetIGV, Pais, NombreNoDomiciliado, RentaBruta, DeduccionCosto,
                    RentaNeta, TasaRetencion, ImpuestoRetenido, Convenio2Imposicion, TipoRenta, AplicaArt76)
                if result == True:
                    return Response({"message": "data updated successful"}, status=200)
                else:
                    return Response(f"Error al conectar a la nueva base de datos: {result}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        if id is None:
            return Response({"message": "Debe especificar un id"}, status=400)
        else:
            if delete_MovContablesDNoDomici(id) == True:
                return Response({"message": "data deleted successful"}, status=200)
            else:
                return Response(f"Error al conectar a la nueva base de datos: {delete_MovContablesDNoDomici(id)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
