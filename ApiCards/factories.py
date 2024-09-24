from ApiCards.serializer.users import AdminUserSerializer, UserSerializer


class UserFactory:
    @staticmethod
    def get_serializer(user_types):
        return {
            1:lambda :AdminUserSerializer,
            2:lambda :UserSerializer,
        }.get(user_types,lambda:None)