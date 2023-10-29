from rest_framework import status
from rest_framework.views import APIView,Response
from .models import Item
from .serializers import ItemSerializer

class MyRestAPI(APIView):

    from rest_framework import status
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response

class MyRestAPI(APIView):

    def get(self, request, id=None):
        if id is not None:
            try:
                item = Item.objects.get(id=id)
                item_data = ItemSerializer(item).data
                response_data = {"data": item_data}
                return Response(response_data, status=status.HTTP_200_OK)
            except Item.DoesNotExist:
                response_data = {"response": "No information found"}
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        else:
            items = Item.objects.all()
            items_data = ItemSerializer(items, many=True).data
            response_data = {"data": items_data}
            return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        item = Item.objects.create(name=name)
        item_data = ItemSerializer(item).data
        response_data = {"response": "Created Successfully!!", "data": item_data}
        return Response(response_data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        name = request.data.get('name')
        try:
            item = Item.objects.get(id=id)
            item.name = name
            item.save()
            item_data = ItemSerializer(item).data
            response_data = {"response": "Updated Successfully!!", "data": item_data}
            return Response(response_data, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            response_data = {"response": "No information found"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            item = Item.objects.get(id=id)
            item.delete()
            response_data = {"response": "Deleted Successfully!!"}
            return Response(response_data, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            response_data = {"response": "No information found"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
