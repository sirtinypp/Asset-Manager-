from django import template
from ..masking import mask_name as _mask_name, mask_department as _mask_dept, mask_username as _mask_user

register = template.Library()

@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    request = context.get('request')
    if not request:
        return ''
    updated = request.GET.copy()
    for k, v in kwargs.items():
        if v is not None:
            updated[k] = v
        else:
            updated.pop(k, None)
    return updated.urlencode()

@register.simple_tag(takes_context=True)
def mask_name(context, first, last, obj_id=None):
    request = context.get('request')
    is_demo = request.session.get('demo_mode', False) if request else False
    return _mask_name(first, last, obj_id, is_demo)

@register.simple_tag(takes_context=True)
def mask_dept(context, name, obj_id=None):
    request = context.get('request')
    is_demo = request.session.get('demo_mode', False) if request else False
    return _mask_dept(name, obj_id, is_demo)

@register.simple_tag(takes_context=True)
def mask_user(context, username):
    request = context.get('request')
    is_demo = request.session.get('demo_mode', False) if request else False
    return _mask_user(username, is_demo)
