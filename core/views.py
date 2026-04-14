from  rest_framework.generics import ListAPIView,CreateAPIView
from .models import Project,Contact
from .serializers import ProjectSerializer,ContactSerializer


class ProjectListAPIView(ListAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer


class ContactCreateAPIView(CreateAPIView):
	querset = Contact.objects.all()
	serializer_class = ContactSerializer
