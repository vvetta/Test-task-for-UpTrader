from django import template 
from menu.models import MenuItem


register = template.Library()


@register.inclusion_tag('draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    print(current_url)

    menu_items = MenuItem.objects.filter(menu_name=menu_name) \
        .select_related('parent')
    
    active_item = None
    for item in menu_items:
        if item.get_url() == current_url:
            active_item = item
            break


    def build_menu_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_menu_tree(items, item)
                tree.append({
                    'item': item,
                    'children': children,
                    'is_active': item == active_item,
                    'is_expanded': item == active_item or (active_item 
                        and item == active_item.parent)
                })
        print(tree)
        return tree

    menu_tree = build_menu_tree(menu_items)

    return {'menu_tree': menu_tree, 'menu_name': menu_name}
