from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
import products.models as products_app_models
import products.serializers as products_app_seralizers


@api_view(['GET'])
def api_home(request,*args, **kwargs):
    
    instance = products_app_models.Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data = model_to_dict(instance , fields=['id','title' , 'price' , 'sale_price'])
        data = products_app_seralizers.ProductSerializer(instance).data
    return Response(data)