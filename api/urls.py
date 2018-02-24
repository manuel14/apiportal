from django.conf.urls import url, include
from django.conf import settings

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken import views as authView

from . import views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register(r'empleado', views.EmpleadoViewSet, base_name='empleado')
router.register(r'mensaje', views.EmpresaViewSet, base_name='empresa')
router.register(r'postulante', views.PostulanteViewSet, base_name='postulante')
router.register(r'oferta', views.OfertaViewSet,
                base_name='oferta')
router.register(r'adjunto', views.AdjuntoViewSet,
                base_name='adjunto')
router.register(r'recibo', views.ReciboViewSet,
                base_name='recibo')
urlpatterns = [
    url(r'^docs/', include_docs_urls(title='API docs')),
    url(r'^', include(router.urls)),
    url(r'^get-token/', authView.obtain_auth_token),
]
