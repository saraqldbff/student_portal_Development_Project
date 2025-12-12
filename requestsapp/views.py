from rest_framework import generics, permissions
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

# API view that allows a student to:
# 1) GET → view all their service requests
# 2) POST → create a new service request
class StudentRequestsView(generics.ListCreateAPIView):

    # Use the serializer for converting model <-> JSON
    serializer_class = ServiceRequestSerializer

    # Only authenticated users can access this view
    permission_classes = [permissions.IsAuthenticated]

    # Return only the requests that belong to the logged-in student
    def get_queryset(self):
        return ServiceRequest.objects.filter(
            student=self.request.user
        ).order_by('-created_at')

    # Automatically assign 'student' field when creating a new request
    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


# API view to:
# 1) GET → retrieve a single request by ID
# 2) PUT/PATCH → update the request (if allowed)
class RequestDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Determine which requests the user is allowed to access
    def get_queryset(self):
        user = self.request.user

        # Students can only access their own requests
        if not user.is_staff:
            return ServiceRequest.objects.filter(student=user)

        # Admin can access all requests
        return ServiceRequest.objects.all()