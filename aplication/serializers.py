from rest_framework import serializers
from .models import *


class TblTipoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblTipoEmpresa
        fields = '__all__'


class MovcontablesdnodomiciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movcontablesdnodomici
        fields = '__all__'


class TblMovimientocajacSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblMovimientocajac
        fields = '__all__'


class Tbl_AFBajaSerializar(serializers.ModelSerializer):
    class Meta:
        model = TblAfbaja
        fields = '__all__'
        extra_kwargs = {
            'estado': {'required': False}
        }


class Tbl_AFCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblAfcargo
        fields = '__all__'
        extra_kwargs = {
            'estado': {'required': False}
        }
