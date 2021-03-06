from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime


def upload_path_recibo(instance, filename):
    if instance.tipo == "R":
        tipo = "recibos"
    else:
        tipo = "aguinaldos"
    return '{0}/{1}/{2}/{3}/{4}'.format(instance.empleado.empresa.nombre, instance.empleado.legajo, tipo, instance.periodo, filename)


def upload_path_adjunto(instance, filename):
    return '{0}/{1}/{2}/{3}'.format(instance.empleado.empresa.nombre, instance.empleado.legajo, "adjuntos", filename)


def upload_path_cv(instance, filename):
    return '{0}/{1}/{2}/{3}'.format(instance.oferta.empresa, "cvs", instance.dni, filename)


def upload_path_fichada(instance, filename):
    return '{0}/{1}/{2}/{3}/{4}'.format(instance.empleado.empresa.nombre, instance.empleado.legajo, "fichadas", instance.periodo, filename)


def upload_path_empleado(instance, filename):
    return '{0}/{1}/{2}'.format(instance.empresa, instance.legajo, filename)


class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    legajo = models.IntegerField(null=True, blank=True)
    cuil = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(
        'foto_perfil', upload_to=upload_path_empleado, null=True, blank=True)
    firma = models.ImageField(
        'firma', upload_to=upload_path_empleado, null=True, blank=True)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, related_name='empleados', default=2)
    domicilio = models.CharField(max_length=200, null=True, blank=True)
    fecha_ingreso = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    puesto = models.CharField(max_length=200, null=True, blank=True)
    fecha_nacimiento = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    dni = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre + str(self.legajo)

    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'


class Mensaje(models.Model):
    asunto = models.CharField(max_length=200)
    contenido = models.CharField(max_length=500)
    empleado = models.ForeignKey(
        Empleado, related_name='mensajes', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)
    leido = models.BooleanField(default=False)


class Recibo(models.Model):
    periodo = models.DateField(auto_now=False, auto_now_add=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    abierto = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    firmado = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    archivo = models.FileField(
        'recibo', upload_to=upload_path_recibo, null=True, blank=True)
    A = "A"
    R = "R"
    tipo_choices = (
        (A, 'Aguinaldo'),
        (R, 'Recibo')
    )
    tipo = models.CharField(
        max_length=20, choices=tipo_choices, default=R)

    def __str__(self):
        return self.empleado.nombre+ " " + datetime.strftime(self.periodo ,"%d-%m-%Y")


class Oferta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.SET_NULL, null=True, blank=True, related_name="empresas")
    sector = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.BooleanField(default=True)
    limite = models.DateField(auto_now_add=False, auto_now=False)

    def __str__(self):
        return self.titulo


class Adjunto(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, null=True, blank=True)
    archivo = models.FileField(
        'adjunto', upload_to=upload_path_adjunto, null=True, blank=True)


class Postulante(models.Model):
    nombre = models.CharField(max_length=200)
    cv = models.FileField('cv', upload_to=upload_path_cv,
                          null=True, blank=True)
    dni = models.IntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    oferta = models.ForeignKey(
        Oferta, on_delete=models.SET_NULL, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    ciudad = models.CharField(max_length=200, null=True, blank=True)
    provincia = models.CharField(max_length=200, null=True, blank=True)


class Formulario(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, auto_now=False)
    P = "P"
    A = "A"
    R = "R"
    estado_choices = (
        (P, 'Pendiente'),
        (A, 'Aprobado'),
        (R, 'Rechazado')
    )
    estado = models.CharField(
        max_length=20, choices=estado_choices, default=P)


class FormularioAdelanto(Formulario):
    importe = models.IntegerField()
    motivo = models.CharField(max_length=400, blank=True, null=True)
    empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, related_name='adelantos', null=True, blank=True)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.SET_NULL, blank=True, null=True, related_name="adelantos")


class FormularioVacaciones(Formulario):
    responsable = models.CharField(max_length=100)
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
    observaciones = models.CharField(max_length=400, null=True, blank=True)
    periodo = models.DateField(auto_now_add=False, auto_now=False)
    empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, related_name='vacaciones', null=True, blank=True)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.SET_NULL, blank=True, null=True, related_name="vacaciones")


class FormularioLicencia(Formulario):
    responsable = models.CharField(max_length=100)
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
    observaciones = models.CharField(max_length=400, null=True, blank=True)
    periodo = models.DateField(auto_now_add=False, auto_now=False)
    empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, related_name='licencias', null=True, blank=True)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.SET_NULL, blank=True, null=True, related_name="licencias")


class Fichada(models.Model):
    periodo = models.DateField(auto_now=False, auto_now_add=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    abierto = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    firmado = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    archivo = models.FileField(
        'fichada', upload_to=upload_path_fichada, null=True, blank=True)
