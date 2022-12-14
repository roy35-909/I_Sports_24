from .models import Content
from .serializers import ContentSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
class ContentModelViewSet(ReadOnlyModelViewSet):
    queryset = Content.objects.all().order_by('-id')
    serializer_class = ContentSerializer
    lookup_field = 'id'
    authentication_classes= [TokenAuthentication]
    permission_classes =[IsAuthenticated]
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view+=1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
class Top10ContentModelViewSet(ReadOnlyModelViewSet):
    queryset = Content.objects.all().order_by('-id')[:10]
    serializer_class = ContentSerializer
    lookup_field = 'id'
    authentication_classes= [TokenAuthentication]
    permission_classes =[IsAuthenticated]
    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        instance = Content.objects.get(id=id)
        instance.view+=1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
class Top5ContentModelViewSet(ReadOnlyModelViewSet):
    queryset = Content.objects.all().order_by('-id')[:5]
    serializer_class = ContentSerializer
    lookup_field = 'id'
    authentication_classes= [TokenAuthentication]
    permission_classes =[IsAuthenticated]
    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        instance = Content.objects.get(id=id)
        instance.view+=1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
class Top3ContentModelViewSet(ReadOnlyModelViewSet):
    queryset = Content.objects.order_by('-id')[:3]
    serializer_class = ContentSerializer
    lookup_field = 'id'
    authentication_classes= [TokenAuthentication]
    permission_classes =[IsAuthenticated]
    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        instance = Content.objects.get(id=id)
        instance.view+=1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
