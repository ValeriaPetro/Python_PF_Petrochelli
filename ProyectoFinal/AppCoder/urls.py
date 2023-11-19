from django.urls import path
from django.http import HttpResponse

from AppCoder.views import * # Mejor hacerlo explicito con las views que se quieren importar, preferentemente ubicar 
                             # alfabeticamente. Para este ejercicio inicial puse * para que me traiga todo


urlpatterns = [
    path("inicio/", inicio_view),
    path("us/", us_view),
    path("business/", business_view),
    path("tool/", tool_view),
    
]
