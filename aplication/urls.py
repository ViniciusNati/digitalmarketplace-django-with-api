from django.urls import path
from .views import *
from . import views

from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('cat', CatViewSet) 
router.register('post', PostViewSet)
router.register('comment', CommentViewSet)


urlpatterns = [
    path('', index.as_view(), name='index'),
    path('anunciar', AnunciarView),
    path('verified', VerifiedView),
    path('account', AccountView),
    path('profile/<str:username>/<int:id>', ProfileSlug, name='profile'),
    path('post/<slug:slug>/', PostView), #um path pra duas views, post e commentview
    #path('comments', CommentView),


]
