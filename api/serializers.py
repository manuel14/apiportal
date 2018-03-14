from rest_framework import serializers
from .models import *
from django.conf import settings
import os


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
    path = serializers.SerializerMethodField('get_path_adjuntos')

    class Meta:
        model = Adjunto
        fields = ('empleado', 'tipo', 'path')

    def get_path_adjuntos(self, obj):
        filepath = settings.URL_SERVER
        filepath += os.path.join(filepath, settings.MEDIA_URL, "ushuaiavision", "{0}", "{1}").format(obj.empleado.legajo, obj.archivo.name)
        return filepath


class PostulanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Postulante
        fields = ('__all__')


class ReciboSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField('get_path_recibos')

    class Meta:
        model = Recibo
        fields = ('periodo', 'empleado', 'abierto', 'firmado', 'path')

    def get_path_recibos(self, obj):
        filepath = settings.URL_SERVER
        filepath += os.path.join(filepath, settings.MEDIA_URL, "ushuaiavision", "{0}", "{1}").format(obj.empleado.legajo, obj.archivo.name)
        return filepath


class MensajeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mensaje
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')


class FormularioAdelantoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormularioAdelanto
        fields = ('__all__')


class FormularioVacacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormularioVacaciones
        fields = ('__all__')
