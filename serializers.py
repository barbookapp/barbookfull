from rest_framework import serializers
from .models import Bottle

class BottleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bottle
		fields = ('name', 'abv', 'country', 'category', 'primary', 'secondary', 'subcat')