from rest_framework import serializers
from .models import ServiceRequest

# Serializer used to convert the ServiceRequest model to JSON
# and handle validation for API requests
class ServiceRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceRequest

        # Include all fields from the model
        fields = '__all__'

        # These fields cannot be modified by the user through the API
        read_only_fields = [
            'student',      # assigned from request.user
            'status',       # default = pending, updated by admin only
            'created_at',   # automatically generated when created
            'updated_at'    # automatically updated on every save
        ]