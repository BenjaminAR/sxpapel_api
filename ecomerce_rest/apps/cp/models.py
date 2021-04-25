from django.db import models
import uuid

class cp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    codigo = models.CharField(max_length=6)
    colonia = models.CharField(max_length=120)
    d_tipo_asenta = models.CharField(max_length=120)
    municipio = models.CharField(max_length=120)
    estado = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=120)
    d_CP = models.CharField(max_length=120, null= True)
    c_estado = models.CharField(max_length=120, null= True)
    c_oficina = models.CharField(max_length=120, null= True)
    c_CP = models.CharField(max_length=120, null= True)
    c_tipo_asenta = models.CharField(max_length=120, null= True)
    c_mnpio = models.CharField(max_length=120, null= True)
    id_asenta_cpcons = models.CharField(max_length=120, null= True)
    d_zona = models.CharField(max_length=120, null= True)
    c_cve_ciudad = models.CharField(max_length=120, null= True)
    
    class Meta:
        verbose_name = 'Codigo postal'
        verbose_name_plural = 'Codigos postales'
    
    def __str__(self):
        return self.codigo


312509