from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar

import blog.views
import blango_auth.views
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm


urlpatterns = [
    path('admin/', admin.site.urls),

    path("", blog.views.index, name="home"),

    # MUST BE FIRST – override the default register URL
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
    ),

    # Django built-in auth URLs
    path("accounts/", include("django.contrib.auth.urls")),

    # django-registration URLs (activation workflow)
    path("accounts/", include("django_registration.backends.activation.urls")),

    # profile
    path("accounts/profile/", blango_auth.views.profile, name="profile"),

    # blog
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),

    path("ip/", blog.views.get_ip),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
