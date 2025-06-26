"""
Widgest that are not specific to the module 

"""
from wtforms import (
    SelectMultipleField,
    widgets,
)


class MultiCheckboxField(SelectMultipleField):
    """
    Use to create checkbox

    Args:
        SelectMultipleField
    """

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

