from django.db import models
from django.contrib.auth.models import User, Group


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
        'foto_perfil', upload_to='images/', null=True, blank=True)
    firma = models.ImageField(
        'firma', upload_to='images/', null=True, blank=True)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.SET_NULL, related_name='empleados', null=True, blank=True)
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
        Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)


class Recibo(models.Model):
    periodo = models.DateField(auto_now=False, auto_now_add=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    abierto = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    firmado = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    archivo = models.FileField(
        'recibo', upload_to='recibos/', null=True, blank=True)


class Oferta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.SET_NULL, null=True, blank=True, related_name="empresas")
    sector = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.BooleanField(default=True)
    limite = models.DateField(auto_now_add=False, auto_now=False)


class Adjunto(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, null=True, blank=True)
    archivo = models.FileField(
        'adjunto', upload_to='adjuntos/', null=True, blank=True)


class Postulante(models.Model):
    nombre = models.CharField(max_length=200)
    cv = models.ImageField('cv', upload_to='images/', null=True, blank=True)
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
    motivo = models.CharField(max_length=400)
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




