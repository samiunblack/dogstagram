from django import template

register = template.Library()

@register.inclusion_tag('snippets/form_snippets.html')
def render_styled_form(form):
    return {'form': form}


@register.filter(name='field_type')
def field_type(field):
    return field.field.widget.__class__.__name__