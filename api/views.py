from rest_framework import viewsets
from django.contrib.auth.models import Group, User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.response import Response
from django.core.serializers import serialize
from .models import *
from .serializers import *
from rest_framework.decorators import detail_route, list_route


class EmpleadoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()


class EmpresaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()


class PostulanteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostulanteSerializer
    queryset = Postulante.objects.all()


class MensajeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MensajeSerializer
    queryset = Mensaje.objects.all()


class AdjuntoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AdjuntoSerializer
    def get_queryset(self): 
        emp = Empleado.objects.get(user=self.request.user)
        try:
            return Adjunto.objects.filter(empleado=emp)
        except ObjectDoesNotExist:
            return []


class ReciboViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReciboSerializer
    def get_queryset(self): 
        emp = Empleado.objects.get(user=self.request.user)
        try:
            return Recibo.objects.filter(empleado=emp)
        except ObjectDoesNotExist:
            return []


class OfertaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OfertaSerializer
    queryset = Oferta.objects.all()

    @list_route(url_name='ofertas_by_empresa', url_path='ofertas_by_empresa/(?P<empresa>[0-9]+)')
    def ofertas_by_empresa(self, request, empresa=None):
        if empresa:
            data = Oferta.objects.filter(empresa=empresa)
            serializer = self.get_serializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response([])



class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class FormularioAdelantoViewSet(viewsets.ModelViewSet):
    serializer_class = FormularioAdelantoSerializer 
    def get_queryset(self): 
        emp = Empleado.objects.get(user=self.request.user)
        try:
            return FormularioAdelanto.objects.filter(empleado=emp)
        except ObjectDoesNotExist:
            return []

class FormularioVacacionesViewSet(viewsets.ModelViewSet):
    serializer_class = FormularioVacacionesSerializer
    def get_queryset(self): 
        emp = Empleado.objects.get(user=self.request.user)
        try:
            return FormularioVacaciones.objects.filter(empleado=emp)
        except ObjectDoesNotExist:
            return []