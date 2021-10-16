"""
to render html web pages
"""
from django.http import HttpResponse
from django.template.loader import render_to_string # can also use get_template for when there are multiple contexts 
from articles.models import Article

def home_view(request):
    """
    take in a request (django sends rqeuest)
    return HTML as a response (we pick the reponse)
    """
    
    article_obj = Article.objects.get(id=2)
    article_queryset = Article.objects.all() #QuerySet
    
    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id
    }

    HTML_String = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_String)