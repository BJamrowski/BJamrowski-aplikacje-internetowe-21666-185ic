# BJamrowski-projektowanie-aplikacji-21666-185ic
## Repozytorium przedmiotu Aplikacje internetowe

Projekt ten jest rozwinieciem projekty z laboratorium nr 4.

Zdarzaja sie sytuacje gdy tworzymy kilka podobnych w dzialaniu widokow.
Django REST pozwala nam na pogrupowanie ich dzieki ViewSet. Wykorzystujac je
mozemy rowniez zastosowac Routery do obslugi URL. Routery dostarczaja
szybkiego dopasowywania ViewSet-ow do odpowiednich adresow URL.
Przykladowe ViewSet
```
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
```

Zastosowane routers
```
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls
```

Django pozwala na wykorzystanie 3 sposobow uwierzytelniania: basic, session oraz token.
Basic jest prostym trybem ale niestety niezbyt bezpiecznym, dodatkowo kazdy zapytanie musi
byc weryfikowany.
W przypadku session klient po uwierzytelnieniu otrzymuje ID zapisany w formie pliku cookie.
Jest ono przekaazywane w kazdym naglowku  zapytania HTTP.
Uwierzytelnianie przy pomocy tokenu jest najbardziej popularna opcja. Po wyslaniu danych
do serwera generwowany jest ciag znakow, ktory przechowywany jest przez klienta. Klient
przekazuje go w naglowku kazdego zapytania HTTP aby serwer mogl stwierdzic czy uzytkownik
jest uwierzytelniony.
