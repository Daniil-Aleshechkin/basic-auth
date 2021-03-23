from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from ..models import Page
from .serializers import PageSerializer


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def api_detailall_page_view(request):
    try:
        pages = Page.objects.all()
    except Page.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)
