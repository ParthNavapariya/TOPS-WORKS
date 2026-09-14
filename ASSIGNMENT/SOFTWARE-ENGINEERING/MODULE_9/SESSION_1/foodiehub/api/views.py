from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def hello_spotify(request):
    return Response({
        "message":"hello , spotify Fans!"
    })




# 4. Difference between JSON and XML

# JSON Format:
# {
#     "product_name": "Flipkart Mobile",
#     "price": 15000
# }


# XML Format:
# <product>
#     <product_name>Flipkart Mobile</product_name>
#     <price>15000</price>
# </product>