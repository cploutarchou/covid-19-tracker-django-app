from django import template

register = template.Library()

green = "text-success"
red = "text-danger"

arrow_up = "fa fa-angle-up"
arrow_down = "fa fa-angle-down"

conditions = {
    'death_rate': {
        "BC_0": (red, arrow_up),
        "GC_0": (green, arrow_down)
    },
    'recovered': {
        "BC_0": (green, arrow_up),
        "GC_0": (red, arrow_down)
    },
    'confirmed': {
        "BC_0": (red, arrow_up),
        "GC_0": (green, arrow_down)
    },
    'deaths': {
        "BC_0": (red, arrow_up),
        "GC_0": (green, arrow_down)
    },
}


@register.simple_tag
def arrow(name, value):
    if value > 0:
        return conditions[name]["BC_0"][1]
    else:
        return conditions[name]["GC_0"][1]


@register.simple_tag
def color(name, value):
    if value > 0:
        return conditions[name]["BC_0"][0]
    else:
        return conditions[name]["GC_0"][0]
