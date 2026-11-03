
from rest_framework import serializers

from business.models import Lead

class LeadSerializer(serializers.ModelSerializer):

    created_by = serializers.StringRelatedField()

    class Meta:

        model = Lead

        fields = "__all__"

        read_only_fields = ["id","created_at","created_by","updated_at"]
