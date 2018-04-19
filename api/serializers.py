from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
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
        fields = ('empleado', 'tipo', 'archivo')


class PostulanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Postulante
        fields = ('__all__')


class ReciboSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recibo
        fields = ('periodo', 'empleado', 'abierto',
                  'firmado', 'archivo', 'tipo')


class MensajeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mensaje
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    empleado_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email', 'empleado_id', 'is_staff', 'is_active')

    def get_empleado_id(self, obj):
        try:
            return Empleado.objects.get(user=obj).pk
        except ObjectDoesNotExist:
            return None


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')


class FormularioAdelantoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormularioAdelanto
        fields = ('__all__')
        read_only_fields = ('estado',)


class FormularioVacacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormularioVacaciones
        fields = ('__all__')


class FichadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fichada
        fields = ('periodo', 'empleado', 'abierto',
                  'firmado', 'archivo')
