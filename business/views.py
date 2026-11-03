from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from business.models import Lead
from business.serializers import LeadSerializer
from business.permissions import IsOwner

# Create your views here.
class LeadCreateView(CreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

    serializer_class = LeadSerializer

    def perform_create(self, serializer):

        serializer.save(created_by=self.request.user)

class LeadListView(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

class LeadRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    
    