from django.db import models
from django.contrib.auth.models import User

# Model representing a student's service request
class ServiceRequest(models.Model):

    # Available request types the student can choose from
    REQUEST_TYPES = [
        ('transcript', 'Transcript'),
        ('letter', 'Letter'),
        ('clearance', 'Clearance'),
    ]

    # Possible status values for each request
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    # The student who submitted the request (linked to Django's User model)
    student = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='requests'
    )

    # Type of request (transcript, letter, etc.)
    request_type = models.CharField(
        max_length=20, 
        choices=REQUEST_TYPES
    )

    # Optional description explaining details of the request
    description = models.TextField(blank=True)

    # Current status of the request (default is pending)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending'
    )

    # When the request was first created
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically updated timestamp whenever the request is modified
    updated_at = models.DateTimeField(auto_now=True)

    # Display a clean readable name for each object in the admin panel
    def __str__(self):
        return f"{self.student.username} - {self.request_type}"