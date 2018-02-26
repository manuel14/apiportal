from rest_framework import viewsets
from django.contrib.auth.models import Group

from .models import *
from .serializers import *


class EmpleadoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()


class EmpresaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()


class PostulanteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Postulante.objects.all()


class MensajeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Mensaje.objects.all()


class AdjuntoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Adjunto.objects.all()


class ReciboViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Recibo.objects.all()


class OfertaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OfertaSerializer
    queryset = Oferta.objects.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
