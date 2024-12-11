from django.shortcuts import render

# Create your views here.
def homepage(request):
            
    context = {"empresa": "JPR-Soluções em Produção - VPS - alterado!!!!!!!!"}
    return render(request, 'homepage.html', context)
