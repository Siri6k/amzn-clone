from EcommerceInventory.Helpers import renderResponse
from rest_framework import generics
from UserServices.models import Modules
import json
from django.core.serializers import serialize as serializer


class ModuleView(generics.CreateAPIView):
    def get(self, request):
        menus = Modules.objects.filter(
            is_menu=True, parent_id=None
        ).order_by('display_order')

        serialized_menus = serializer('json', menus)

        serialized_menus = json.loads(serialized_menus)

        cleaned_menus= []
        for menu in serialized_menus:
            menu["fields"]["id"] = menu["pk"]
            menu["fields"] ["submenus"]= Modules.objects.filter(
                parent_id=menu["pk"], is_menu=True, is_active=True
            ).order_by('display_order').values(
                'id', "module_name", "module_url", 
                "module_icon", 
                "module_description",
                "display_order", "is_menu", 
                "is_active", "parent_id"
            )
            cleaned_menus.append(menu["fields"])

        return renderResponse(
            data=cleaned_menus, 
            message='All Modules', 
            status=200
        )