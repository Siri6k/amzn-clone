from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from EcommerceInventory import settings


from UserServices.Controller.SidebarController import (
    ModuleView,
)
from UserServices.Controller.ModuleController import (
    SuperAdminDynamicFormController,
)
from UserServices.Controller.DynamicFormController import DynamicFormController

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("UserServices.urls")),
    path(
        "api/getForm/<str:modelName>/",
        DynamicFormController.as_view(),
        name="dynamicForm",
    ),
    path(
        "api/superAdminForm/<str:modelName>/",
        SuperAdminDynamicFormController.as_view(),
        name="SuperAdmindynamicForm",
    ),
    path(
        "api/getMenus/",
        ModuleView.as_view(),
        name="sidebarmenu",
    ),
    path("api/products/", include("ProductServices.urls")),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
