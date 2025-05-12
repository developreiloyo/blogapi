from .models import Post, Categoria, RedesSociales

def consulta(id):
	try:
		return Post.objects.get(id=id)
	except:
		return None
def general():
	return Post.objects.all()
	
def categoria(unique):	
	return Post.objects.all().prefetch_related("categoria").filter(categoria=unique, publicado=True).order_by('-fecha_publicacion')
	
def categorias(unique,cantidad):	
	return Post.objects.all().prefetch_related("categoria").filter(categoria=unique, publicado=True).order_by('-fecha_publicacion')[:cantidad]
def obtenerRedes():
	return RedesSociales.objects.filter(estado =True).latest('fecha_creacion')