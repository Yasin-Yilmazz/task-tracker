from rest_framework.viewsetts import ModelViewSet
from .serializers import(
    User, UserSerializer
)

class UserView(ModelViewSet):
    queryset = User.object.all()
    serializer_class = UserSerializer