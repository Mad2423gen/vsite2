from django import template
from blogs.models import Category

register = template.Library()


@register.inclusion_tag('blogs/includes/category_links.html')
def render_category_links():
    return {
        'category_list': Category.objects.all(),
    }
