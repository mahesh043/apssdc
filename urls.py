from django.urls import path
from DjProject import views
from django.contrib.auth import views as g

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('rg/',views.register,name="reg"),
	path('ds/',views.dashboard,name="dsh"),
	path('pf/',views.prfle,name="pfe"),
	path('upf/',views.updf,name="upfe"),
	path('mb/',views.redmi,name="mbe"),
	path('mb1/',views.redmi1,name="mbe1"),
	path('mb2/',views.redmi2,name="mbe2"),
	path('mb3/',views.vivo,name="mbe3"),
	path('mb4/',views.vivo1,name="mbe4"),
	path('mb5/',views.vivo2,name="mbe5"),
	path('mb6/',views.one1,name="mbe6"),
	path('mb7/',views.one2,name="mbe7"),
	path('mb8/',views.one3,name="mbe8"),
	path('mbb/',views.books,name="boo1"),
	path('mba/',views.card,name="car"),
	path('lg/',g.LoginView.as_view(template_name="html/login.html"),name="lgn"),
	path('lgg/',g.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]
