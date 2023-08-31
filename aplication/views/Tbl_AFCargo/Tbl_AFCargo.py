from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import OperationalError
from aplication.serializers import Tbl_AFCargoSerializer
from ..Tbl_AFCargo.CRUD.get import get_Tbl_AFCargo, getbyid_Tbl_AFCargo
from ..Tbl_AFCargo.CRUD.post import post_TBL_AFCargo
from ..Tbl_AFCargo.CRUD.put import put_Tbl_AFCargo
from ..Tbl_AFCargo.CRUD.delete import delete_TblAFCargo


class Tbl_AFCargo (APIView):
    def get(self, request, id=None):
        if id is None:
            try:
                data = get_Tbl_AFCargo()
                serializer = Tbl_AFCargoSerializer(data, many=True)
                return Response(serializer.data, status=200)
            except OperationalError as e:
                return Response(f"Error al conectar a la nueva base de datos: {str(e)}", status=500)
        else:
            try:
                data = getbyid_Tbl_AFCargo(id)
                serializer = Tbl_AFCargoSerializer(data, many=True)
                return Response(serializer.data, status=200)
            except OperationalError as e:
                return Response(f"Error al conectar a la nueva base de datos: {str(e)}", status=500)

    def post(self, request):
        serializer = Tbl_AFCargoSerializer(data=request.data)
        if serializer.is_valid():
            descripcion = request.data.get('descripcion')
            idempresa = request.data.get('idempresa')
            if post_TBL_AFCargo(descripcion, idempresa) == True:
                return Response({"message": "data saved successful"}, status=200)
            else:
                return Response(f"Error al conectar a la nueva base de datos: {post_TBL_AFCargo(descripcion)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, id=None):
        if id is None:
            return Response({"message": "Debe especificar un id"}, status=400)
        else:
            serializer = Tbl_AFCargoSerializer(data=request.data)
            if serializer.is_valid():
                descripcion = request.data.get('descripcion')
                idempresa = request.data.get('idempresa')
                if put_Tbl_AFCargo(id, descripcion, idempresa) == True:
                    return Response({"message": "data updated successful"}, status=200)
                else:
                    return Response(f"Error al conectar a la nueva base de datos: {put_Tbl_AFCargo(id, descripcion,idempresa)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        if id is None:
            return Response({"message": "Debe especificar un id"}, status=400)
        else:
            if delete_TblAFCargo(id) == True:
                return Response({"message": "data deleted successful"}, status=200)
            else:
                return Response(f"Error al conectar a la nueva base de datos: {delete_TblAFCargo(id)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
