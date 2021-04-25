import re
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.cp.models import cp
from apps.cp.api.serializers import cpSerializer

# Vista usando decorador con función.

@api_view(['GET', 'POST'])
def cp_api_view(request):

    if request.method == 'GET':
        Cp = cp.objects.all()
        cp_serializer = cpSerializer(Cp, many=True)
        return Response(cp_serializer.data)
    elif request.method == 'POST':
        print(request.data)


# vista basada em clase


'''
class cpApiView(APIView):
    
    def get(self,request):
        Cp = cp.objects.all()
        cp_serializer = cpSerializer(Cp, many = True)
        return Response(cp_serializer.data)
'''
