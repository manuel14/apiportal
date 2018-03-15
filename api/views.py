from rest_framework import viewsets, mixins
from django.contrib.auth.models import Group, User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import detail_route, list_route
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser


class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()


class PostulanteViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = PostulanteSerializer
    queryset = Postulante.objects.all()

    @list_route(url_name='postulantes_for_oferta', url_path='postulantes_for_oferta/(?P<oferta>[0-9]+)')
    def postulantes_for_oferta(self, request, oferta=None):
        if oferta:
            data = Postulante.objects.filter(oferta=oferta)
            serializer = self.get_serializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response([])


class MensajeViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = MensajeSerializer
    queryset = Mensaje.objects.all()

    @list_route(url_name='mensajes_empleado', url_path='mensajes_empleado/(?P<empleado>[0-9]+)')
    def mensajes_empleado(self, request, empleado=None):
        if empleado:
            data = Mensaje.objects.filter(empleado=empleado)
            serializer = self.get_serializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response([])


@parser_classes((JSONParser, MultiPartParser))
class AdjuntoViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = AdjuntoSerializer

    def get_queryset(self):
        emp = Empleado.objects.get(user=self.request.user)
        try:
            return Adjunto.objects.filter(empleado=emp)
        except ObjectDoesNotExist:
            return []


class ReciboViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = ReciboSerializer

    def get_queryset(self):
        emp = Empleado.objects.get(user=self.request.user)
        try:
            return Recibo.objects.filter(empleado=emp)
        except ObjectDoesNotExist:
            return []


class OfertaViewSet(viewsets.ModelViewSet):
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

    @detail_route(url_name='user_group', url_path='user_group')
    def user_group(self, request, pk=None):
        try:
            group = User.objects.get(id=pk).groups.all()[0]
        except IndexError:
            return HttpResponseNotFound()
        serializer = self.get_serializer(group)
        return Response(serializer.data)


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
