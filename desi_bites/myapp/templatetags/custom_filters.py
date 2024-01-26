from django import template

register = template.Library()

@register.filter(name='filter_category')
def filter_category(items, category):
    return items.filter(category=category)