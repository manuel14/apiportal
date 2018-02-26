from rest_framework import serializers
from .models import *


class EmpleadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleado
        fields = ('__all__')


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = ('__all__')


class OfertaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Oferta
        fields = ('__all__')


class AdjuntoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adjunto
        fields = ('__all__')


class PostulanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Postulante
        fields = ('__all__')


class ReciboSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recibo
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')
