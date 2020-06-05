from rest_framework import serializers

from appsite.models import Users, Consultants, Category,Field

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'city', 'last_login_date' )

class ConsultantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Consultants
        fields = ('username', 'city', 'last_login_date' )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')

class FieldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Field
        fields = ('name', 'description')


