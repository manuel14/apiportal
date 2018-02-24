from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from django.contrib.auth.models import User, Group

from .models import *
from .serializers import *


class EmpleadoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()


class EmpresaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Empresa.objects.all()


class PostulanteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Postulante.objects.all()


class MensajeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Mensaje.objects.all()


class AdjuntoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Adjunto.objects.all()


class ReciboViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Recibo.objects.all()


class OfertaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OfertaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Oferta.objects.all()