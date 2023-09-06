from django.db.models import Q
from rest_framework import generics

from universities.models import OTM
from .serializers import OTMSerializer


#
class OTMListAPIView(generics.ListAPIView):
    queryset = OTM.objects.filter(is_active=True, parent_category__isnull=True).order_by('-id')
    serializer_class = OTMSerializer

    def get_queryset(self):
        querysets = self.queryset.all()
        param = self.request.GET.get('search')

        param_condition = Q()
        if param:
            param_condition = Q(title__icontains=param)

        qs = querysets.filter(param_condition)
        return qs
