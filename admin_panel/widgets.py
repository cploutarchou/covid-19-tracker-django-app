from django import forms
from django.forms.widgets import Select, SelectMultiple


class AdminPanelSelect(Select):
    template_name = "admin_panel/widgets/select.html"

    def _get_media(self):
        return forms.Media(
            css={
                "all": ("admin/plugins/select2/select2.min.css",)
            },
            js=(
                "admin/plugins/select2/select2.min.js",
            ))

    media = property(_get_media)


class AdminPanelSelectMultiple(SelectMultiple):
    template_name = "admin_panel/widgets/select.html"

    def build_attrs(self, base_attrs, extra_attrs=None):
        extra_attrs['multiple'] = 'multiple'
        return {**base_attrs, **(extra_attrs or {})}

    def _get_media(self):
        return forms.Media(
            css={
                "all": ("admin/plugins/select2/select2.min.css",)
            },
            js=(
                "admin/plugins/select2/select2.min.js",
            ))

    media = property(_get_media)
