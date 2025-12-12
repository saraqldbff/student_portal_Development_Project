from django.contrib import admin
from .models import ServiceRequest

# Register ServiceRequest model and customize how it appears in the admin panel
@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):

    # Columns to display in the admin list view
    list_display = ('id', 'student', 'request_type', 'status', 'created_at')

    # Filters on the right side for easier navigation
    list_filter = ('status', 'request_type')

    # Enable searching by student username, email, and request description
    search_fields = ('student__username', 'student__email', 'description')

    # Sort requests by newest first
    ordering = ('-created_at',)

    # Custom admin actions (approve or reject multiple requests)
    actions = ['approve_requests', 'reject_requests']

    # Action → Mark selected requests as "approved"
    def approve_requests(self, request, queryset):
        queryset.update(status='approved')
    approve_requests.short_description = "Mark selected requests as APPROVED"

    # Action → Mark selected requests as "rejected"
    def reject_requests(self, request, queryset):
        queryset.update(status='rejected')
    reject_requests.short_description = "Mark selected requests as REJECTED"



