from rest_framework import serializers
from snippets.models import Snippet, Info,LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.CharField(read_only=True, source='owner.username')
#
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
#
#
# class UserSerializer(serializers.ModelSerializer):
     # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())  # 'snippets' is a reverse
     # relationship on the User model,
     # it will not be included by default when using the ModelSerializer class,
     # so we needed to add an explicit field for it.
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')


    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class InfoObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = (
            'name',
            'date_of_b',
            'year_i_school',
            'avatar'
        )


class SnippetObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'id',
            'highlighted',
            'title',
            'code',
            'linenos',
            'language',
            'style'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    snippets = SnippetObjectSerializer(many=True, read_only=True)
    info = InfoObjectSerializer(many=True, read_only=True)
    # def to_representation(self, instance):
    #     return self.info

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets', 'info']


class InfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Info
        fields = ['name', 'date_of_b', 'year_i_school', 'avatar', 'owner']
