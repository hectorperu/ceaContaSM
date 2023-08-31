from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import OperationalError
from aplication.serializers import Tbl_AFBajaSerializar
from ..Tbl_AFBaja.CRUD.get import get_TblAFBaja, get_byidTblAFBaja
from ..Tbl_AFBaja.CRUD.post import post_TblAFBaja
from ..Tbl_AFBaja.CRUD.put import put_TblAFBaja
from ..Tbl_AFBaja.CRUD.delete import delete_TblAFBaja


class Tbl_AFBaja (APIView):
    def get(self, request, id=None):
        if id is None:
            try:
                data = get_TblAFBaja()
                serializer = Tbl_AFBajaSerializar(data, many=True)
                return Response(serializer.data, status=200)
            except OperationalError as e:
                return Response(f"Error al conectar a la nueva base de datos: {str(e)}", status=500)
        else:
            try:
                data = get_byidTblAFBaja(id)
                serializer = Tbl_AFBajaSerializar(data, many=True)
                return Response(serializer.data, status=200)
            except OperationalError as e:
                return Response(f"Error al conectar a la nueva base de datos: {str(e)}", status=500)

    def post(self, request):
        serializer = Tbl_AFBajaSerializar(data=request.data)
        if serializer.is_valid():
            descripcion = request.data.get('descripcion')
            if post_TblAFBaja(descripcion) == True:
                return Response({"message": "data saved successful"}, status=200)
            else:
                return Response(f"Error al conectar a la nueva base de datos: {post_TblAFBaja(descripcion)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, id=None):
        if id is None:
            return Response({"message": "Debe especificar un id"}, status=400)
        else:
            serializer = Tbl_AFBajaSerializar(data=request.data)
            if serializer.is_valid():
                descripcion = request.data.get('descripcion')
                if put_TblAFBaja(id, descripcion) == True:
                    return Response({"message": "data updated successful"}, status=200)
                else:
                    return Response(f"Error al conectar a la nueva base de datos: {put_TblAFBaja(id, descripcion)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        if id is None:
            return Response({"message": "Debe especificar un id"}, status=400)
        else:
            if delete_TblAFBaja(id) == True:
                return Response({"message": "data deleted successful"}, status=200)
            else:
                return Response(f"Error al conectar a la nueva base de datos: {delete_TblAFBaja(id)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
