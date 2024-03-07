import plotly.express as px
import pandas as pd
from data_manager import DataManager

data_manager = DataManager('cleaned_weather_data.csv')


def temp_chart(location, temp_unit):
    df = data_manager.get_location_data(location)
    y_axis = 'Temperature (°C)' if temp_unit == 'Celsius' else 'Temperature (°F)'
    fig = px.line(df, x='last_updated', y=y_axis, color_discrete_sequence=['#7158e2'])
    fig.update_layout(
        title={
            'text': f'Temperature Trends over Time',
            'y': 0.96,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'color': 'RebeccaPurple', 'size': 20}  
        },
        xaxis=dict(
            title='Date',
            titlefont=dict(
                family="Arial, sans-serif",  
                size=15,                      
                color="RebeccaPurple"       
            )
        ),
        yaxis=dict(
            title=y_axis,
            titlefont=dict(
                family="Arial, sans-serif", 
                size=15,                     
                color="RebeccaPurple"        
            )
        )
    )


    return fig


# Aqi and Pollutants Concentration

def create_aqi_plot(location):
    data = data_manager.get_location_data(location)
    air_quality_columns = [
        'air_quality_Carbon_Monoxide', 'air_quality_Ozone', 'air_quality_Nitrogen_dioxide', 
        'air_quality_Sulphur_dioxide', 'air_quality_PM2.5', 'air_quality_PM10'
    ]
    avg_concentration = data[air_quality_columns].mean()
    readable_labels = {
        'air_quality_Carbon_Monoxide': 'CO',
        'air_quality_Ozone': 'O3',
        'air_quality_Nitrogen_dioxide': 'NO2',
        'air_quality_Sulphur_dioxide': 'SO2',
        'air_quality_PM2.5': 'PM2.5',
        'air_quality_PM10': 'PM10'
    }
    avg_concentration.index = [readable_labels[col] for col in avg_concentration.index]
    avg_concentration = avg_concentration.sort_values(ascending=False).reset_index()
    avg_concentration.columns = ['Pollutants', 'Average Concentration']
    
    fig = px.bar(avg_concentration, x='Pollutants', y='Average Concentration',
                 title=f'Average Air Quality Indexes for {location}',color='Pollutants', 
                 color_discrete_sequence=px.colors.qualitative.Set3,
                 template='plotly_white'
                )
    fig.update_layout(showlegend=False)
    fig.update_layout(
        title={
            'text': f'Average Air Quality ({location})',
            'y': 0.96,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'color': 'RebeccaPurple', 'size': 20}  
        },
        xaxis=dict(
            title='Pollutants',
            titlefont=dict(
                family="Arial, sans-serif",  
                size=15,                     
                color="RebeccaPurple"        
            )
        ),
        yaxis=dict(
            title='Average Concentration',
            titlefont=dict(
                family="Arial, sans-serif",  
                size=15,                      
                color="RebeccaPurple"    
            )
        )
    )
    return fig

# Weather Conditions
def condition_pie_chart(location):
    data = data_manager.get_location_data(location)
    weather_counts = data['condition_text'].value_counts().head(4)
    fig = px.pie(weather_counts, values=weather_counts.values, names=weather_counts.index,
                 title='Weather Condition Distribution', hole=0.6, 
                 color_discrete_sequence=px.colors.qualitative.Set3
                )
    fig.update_traces(textinfo='percent')
    fig.update_layout(showlegend=True)
    fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
    fig.update_layout(
        title={
            'text': f'Weather Condition Distribution ',
            'y':0.96,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top', 
            'font': {'color': 'RebeccaPurple', 'size': 20}})
    fig.update_layout(
        font=dict(
            family="Arial, sans-serif",
            size=12,
            color="RebeccaPurple"
        )
    )
    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.01,
            xanchor="auto",
            x=0.9
        )
    )
    return fig


# Wind speed
def create_wind_speed_plot(location):
    data = data_manager.get_location_data(location)
    fig = px.line(data, x='last_updated', y='Wind Speed (kph)', color_discrete_sequence=['#7158e2'])
    fig.update_layout(
            title={
                'text': f'Wind Speed Trends',
                'y': 0.96,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': {'color': 'RebeccaPurple', 'size': 20}  
            },
            xaxis=dict(
                title='Date',
                titlefont=dict(
                    family="Arial, sans-serif",  
                    size=15,                      
                    color="RebeccaPurple"         
                )
            ),
            yaxis=dict(
                title=f'Wind Speed (kph)',
                titlefont=dict(
                    family="Arial, sans-serif",  
                    size=15,                      
                    color="RebeccaPurple"    
                )
            )
        )
    return fig

