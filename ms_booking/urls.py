"""
URL configuration for ms_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ms_dashboard.urls")),
    path('property/', include("ms_property.urls")),
    path('destination/', include("ms_destination.urls")),
    path('booking/', include("ms_booking_booking.urls")),
    path('booking-step/', include("ms_booking_step.urls")),
    path('login/', include("ms_login.urls")),
    path('logout/', include("ms_logout.urls")),
    path('signup/', include("ms_signup.urls")),
    path('identify/', include("ms_identify_account.urls")),
    path("mapstar-recruitments/", include("ms_recruitment.urls")),
    path("applicants/", include("ms_applicant.urls")),
    path("common-question/", include("ms_common_question.urls")),
    path("partners/", include("ms_partner.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
