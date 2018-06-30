from django.db import models

active="Ativada"
inactive="Inativa"
cancelado="Cancelada"
expired="Expirada"
CHOICES=[
(active, "Ativo"),
 (inactive, "Inativo"), 
 (cancelado, "Cancelado"),
 (expired,"Expirado"),
 ]

class Promotion(models.Model):
	#categoria=models.CharField(max_length=500, default="")
	título=models.CharField(max_length=500, default="")
	#thumbnail=models.ImageField(upload_to = '../media/cupom_system/media' ,blank=True)
	#imagem_de_capa=models.ImageField(upload_to ='../media/cupom_system/media',blank=True)
	#recorrência_semanal=models.ForeignKey("Semanal", on_delete=models.CASCADE, null=True)
	#recorrência_período_único=models.ForeignKey("Unique", on_delete=models.CASCADE, null=True)
	quantidade=models.IntegerField(null=True, default=0)
	preço_normal=models.DecimalField(max_digits=5, decimal_places=2)
	preço_promocional=models.DecimalField(max_digits=5, decimal_places=2)
	horário_de_consumo=models.CharField(max_length=500, default="")
	status=models.CharField(max_length=500, choices=CHOICES)
	regras_gerais=models.TextField(max_length=3000, default="")
	descrição=models.TextField(max_length=3000, default="")

	def __str__(self):
		return self.título

	def get_absolute_url(self):
		slugid=self.id
		return "{}".format(slugid)
