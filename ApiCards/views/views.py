from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from ApiCards.middleware.set_token import set_token_middleware
from ..factories import UserFactory
from ..middleware.check_token import check_token
from ..models.user import user

# Create your views here.
class UserManagerView(APIView):
    @check_token
    def get(self, request):
        try:
            users = user.objects.all()
            serializer_class = UserFactory.get_serializer(2)

            serializer = serializer_class(users, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except serializer_class.DoesNotExist:
            raise Http404("User does not exist")
    @set_token_middleware
    def post(self, request):
        try:
            users = user.objects.all()
            users_data = [{'id': user.id, 'name': user.name} for user in users]  # Ejemplo de conversión a JSON
            return Response(users_data, status=status.HTTP_200_OK)
        except users.DoesNotExist:
            raise Http404("User does not exist")
