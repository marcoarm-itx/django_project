from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.

layout = """
<h1>Sitio web de Marco hecho con Django</h1>
<hr>
<ul>
 <li>
    <a href="/inicio">Inicio</a>
 </li>
 <li>
    <a href="/hola-mundo">Hola mundo</a>
 </li>
 <li>
    <a href="/pagina-pruebas">Página de pruebas</a>
 </li>
 <li>
    <a href="/contacto">Contacto</a>
 </li>
</ul>
<hr>
"""


def index(request):
    """ html = ""
         <h1> Inicio </h1>
         <p>Años hasta el 2050:</p>
         <ul>
     ""
     year = 2021
     while year <= 2050:
         if year % 2 == 0:
             html += f"<li>{str(year)}</li>"
         year += 1
     html += "</ul>"

     return HttpResponse(layout+html)"""
    year = 2021
    hasta = range(year, 2051)

    nombre = "Marco Rodriguez"
    lenguajes = ['Javascript', 'Python', 'PHP', 'C']

    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta a la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })


def hola_mundo(request):
    return render(request, 'hola_mundo.html', {
        'title': 'Hola Mundo'
    })


def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio/')

    return render(request, 'pagina.html', {
        'title': 'Pagina de pruebas'
    })


def contacto(request):
    return render(request, 'contacto.html', {
        'title': 'Contacto'
    })


def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public
    )
    articulo.save()
    return HttpResponse(f"Articulo creado con ID {articulo.id}")


def save_article(request):
    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title=title,
            content=content,
            public=public
        )

        articulo.save()
        return HttpResponse(f"Articulo creado con ID {articulo.id}")
        return redirect('articulos')
    else:
        return HttpResponse(f"Articulo NO creado")


def create_article(request):
    return render(request, 'create_article.html', {
        'title': 'Crear Articulo'
    })


def create_full_article(request):
    if request.method == 'POST':
        formulario = FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title=title,
                content=content,
                public=public
            )
            articulo.save()

            # crear mensaje flash (solo dura una visualizacion)
            messages.success(request, f'Articulo guardado correctamente con id:{articulo.id}')

            return redirect('articulos')
            # return HttpResponse(articulo.title + ' - ' + articulo.content + ' - ' + str(articulo.public))

    else:
        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario,
        'title': 'Crear Articulo Full'
    })


def articulo(request):
    try:
        articulo = Article.objects.get(pk=4)
        response = f"Articulo: {articulo.title}"
    except:
        response = "Articulo no encontrado"

    return HttpResponse(response)


def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()
    return HttpResponse(f"Articulo editado con ID {articulo.id}")


def articulos(request):
    # Usando estos metodos da igual la BBDD que usemos por detras
    articulos = Article.objects.filter(public=True).order_by('-id')

    """articulos = Article.objects.filter(
        Q(title__contains="Batman") | Q(title__contains="Cuarto")
    )"""

    # articulos = Article.objects.filter(title__contains='articulo')

    # Tambien podemos usar consultas SQL
    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE  title='Batman'")

    return render(request, 'articulos.html', {
        'articulos': articulos,
        'title': 'Listado de Articulos'
    })


def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')
