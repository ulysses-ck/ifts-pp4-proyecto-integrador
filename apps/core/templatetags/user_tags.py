from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def is_logged_in(context):
    user = context['request'].user
    return user.is_authenticated
