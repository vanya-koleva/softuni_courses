from django import template


register = template.Library()

@register.inclusion_tag('common/user-info.html', takes_context=True)
def user_info(context, user):
    """
    There are better ways to do this than an inclusion tag.
    """
    if user.is_authenticated:
        return {
            'username': user.username,
        }

    return {
        'username': 'Anonymous',
    }