import panel as pn

def create_location_selector(options):
    return pn.widgets.Select(name='Select Location', options=options)

def create_temp_unit_selector(options):
    return pn.widgets.RadioButtonGroup(name='Temperature Unit', options=options, button_type='primary')