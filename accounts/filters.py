import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_created']


class ObjectFilter(django_filters.FilterSet):
	class Meta:
		model = Object
		fields = '__all__'
		exclude = ['contributor', 'date_created', 'description', 'name']

class WarningFilter(django_filters.FilterSet):
	class Meta:
		model = Warning
		fields = '__all__'

class ArticleFilter(django_filters.FilterSet):
	class Meta:
		model = Article
		fields = '__all__'
		exclude = ['name']



class OtherFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	description = CharFilter(field_name='description', lookup_expr='icontains')
	#if Object.objects.filter(start_date, end_date).order_by('-diameter'):
	#	diameter = Object.objects.filter(date_created__gte=start_date, date_created__lte=end_date).order_by('-diameter')[0]

class WarningFilter(django_filters.FilterSet):
	class Meta:
		model = Warning
		fields = '__all__'