from django.contrib import admin
from django.urls import path, include

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
]
