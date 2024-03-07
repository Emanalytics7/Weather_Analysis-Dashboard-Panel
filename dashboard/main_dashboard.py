import panel as pn
from panel.template import FastListTemplate
from data_manager import DataManager
from visualizations import temp_chart, create_aqi_plot, condition_pie_chart, create_wind_speed_plot
from dashboard_components import create_location_selector, create_temp_unit_selector

data_manager = DataManager('cleaned_weather_data.csv', )
location_selector = create_location_selector(data_manager.weather['location_name'].unique().tolist())
temp_unit_selector = create_temp_unit_selector(options=['Celsius', 'Fahrenheit'])

@pn.depends(location_selector.param.value, temp_unit_selector.param.value)
def update_plots(country, temp_unit):
    # Generate plot figures
    temp_plot = temp_chart(country, temp_unit)
    aqi_plot = create_aqi_plot(country)
    condition_pie_plot = condition_pie_chart(country)
    wind_speed_plot = create_wind_speed_plot(country)

    # Create Panel objects for each plot directly here
    temp_plot_panel = pn.pane.Plotly(temp_plot)
    aqi_plot_panel = pn.pane.Plotly(aqi_plot)
    condition_pie_plot_panel = pn.pane.Plotly(condition_pie_plot)
    wind_speed_plot_panel = pn.pane.Plotly(wind_speed_plot)

    # Arrange the Panel objects in rows and columns
    row1 = pn.Row(pn.Column(temp_unit_selector, pn.Row(temp_plot_panel, aqi_plot_panel)))
    row2 = pn.Row(pn.Column(pn.Row(condition_pie_plot_panel, wind_speed_plot_panel)))

    main_column = pn.Column(row1, row2)

    return main_column

# Template for the dashboard
template = FastListTemplate(
    title='Global Weather Overview Dashboard', 
    sidebar=[
        pn.pane.Markdown("# WorldWide Weather Analytics"), 
        pn.pane.Markdown(" Global weather encompasses temperature changes, weather conditions, wind patterns,\
                          and air quality, each significantly impacting ecosystems, human health, and agriculture.\
                          Understanding these elements is crucial for managing environmental risks and enhancing \
                          resilience against climatic variations."), 

        pn.pane.PNG('clouds-sun.png', sizing_mode='scale_both'),
        pn.pane.Markdown("#### Settings"),   
        location_selector
    ],
    main=[
        # Dynamically update the plots based on user selections 
        update_plots]
    ,
    header_background="#9381ff",
    accent_base_color="#b8b8ff",
    # background_color='#bbd1ea', 
    main_layout='card')


pn.serve(template, port=5006, show=True, dev=True)