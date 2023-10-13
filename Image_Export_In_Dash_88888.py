import pandas as pd
import dash
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import os


# 01: Create a Dash web application
app = dash.Dash(__name__)
server = app.server

# 02: Define Download Path 
from pathlib import Path
download_path = str(Path.home() / "Downloads")
download_path.replace("\\", "/")

# 03: Speciry Columns to include
#columns_to_include = ['Date','WA_B1','ESB_B1','WA_S1','ESB_S1','WA_B2','ESB_B2','WA_S2','ESB_S2','WA_B3','ESB_B3','WA_S3','ESB_S3','WA_B4','ESB_B4','WA_S4','ESB_S4']

# 04A: Read .csv file
data = pd.read_csv(download_path+'\Test_Origina_Data_ORIGINAL.csv',parse_dates=['Date'])
#data = pd.read_csv(download_path+'\Test_Origina_Data_ORIGINAL.csv',usecols=columns_to_include,parse_dates=['Date'])
# Create a Pandas DataFrame
#data = pd.DataFrame(data0)

# 04B: Crate Pandas DataFrame and Include only those columns required as Output file as per click button
data1 = (data[['Date','ESB_S1', 'ESB_B1', 'WA_S1', 'WA_B1']])       # 'Extract Average Price Porker 45-60 Kg'
data2 = (data[['Date','ESB_S2', 'ESB_B2', 'WA_S2', 'WA_B2']])       # 'Extract Prime Price Porker 45-60 Kg'
data3 = (data[['Date','ESB_S3', 'ESB_B3', 'WA_S3', 'WA_B3']])       # 'Extract Average Price Baconer 60.1 - 75 Kg'
data4 = (data[['Date','ESB_S4', 'ESB_B4', 'WA_S4', 'WA_B4']])       # 'Extract Prime Price Baconer 60.1 - 75 Kg'

# 04C:
y1 = ['ESB_S1', 'ESB_B1', 'WA_S1', 'WA_B1']
y2 = ['ESB_S2', 'ESB_B2', 'WA_S2', 'WA_B2'] 
y3 = ['ESB_S3', 'ESB_B3', 'WA_S3', 'WA_B3']
y4 = ['ESB_S4', 'ESB_B4', 'WA_S4', 'WA_B4']

# 04D: store min/max value for y-axis --> y1,y2,y3,y4
d1_min = int((data1[y1].min()).min())
d1_max = int((data1[y1].max()).max())
##
d2_min = int((data2[y2].min()).min())
d2_max = int((data2[y2].max()).max())
##
d3_min = int((data3[y3].min()).min())
d3_max = int((data3[y3].max()).max())
##
d4_min = int((data4[y4].min()).min())
d4_max = int((data4[y4].max()).max())

# 04D: call function to Downgrade for min and Upgrade for Max to accomodate y axis tick
def round_down_to_nearest_100_for_min_or_max(number,min_max):
    remainder = number % 100
    if remainder == 50 or remainder == 0 :      #regardless of min or max
                return number
    elif min_max == 'min':                      #get lowest value
        if remainder < 50:
            return number - remainder
        else:
            return number - remainder+50
    elif min_max == 'max':                      #get highest value
        if remainder < 50:
            return number - remainder +50
        else: 
            return number - remainder + 100   
  
# 04E: store min/max tick point for y-axis for corresponding data sets such as data1,data2,data3 and data4
y1_min_for_data1 = round_down_to_nearest_100_for_min_or_max(d1_min,'min')
y1_max_for_data1 = round_down_to_nearest_100_for_min_or_max(d1_max,'max')
y2_min_for_data2 = round_down_to_nearest_100_for_min_or_max(d2_min,'min')
y2_max_for_data2 = round_down_to_nearest_100_for_min_or_max(d2_max,'max')
y3_min_for_data3 = round_down_to_nearest_100_for_min_or_max(d3_min,'min')
y3_max_for_data3 = round_down_to_nearest_100_for_min_or_max(d3_max,'max')
y4_min_for_data4 = round_down_to_nearest_100_for_min_or_max(d4_min,'min')
y4_max_for_data5 = round_down_to_nearest_100_for_min_or_max(d4_max,'max')

# 04F: Rename data frame columns for display purpose
data1 = data1.rename(columns={'ESB_S1': 'ESB Seller', 'ESB_B1': 'ESB Buyer', 'WA_S1': 'WA Seller', 'WA_B1': 'WA Buyer'})
data2 = data2.rename(columns={'ESB_S2': 'ESB Seller', 'ESB_B2': 'ESB Buyer', 'WA_S2': 'WA Seller', 'WA_B2': 'WA Buyer'})
data3 = data3.rename(columns={'ESB_S3': 'ESB Seller', 'ESB_B3': 'ESB Buyer', 'WA_S3': 'WA Seller', 'WA_B3': 'WA Buyer'})
data4 = data4.rename(columns={'ESB_S4': 'ESB Seller', 'ESB_B4': 'ESB Buyer', 'WA_S4': 'WA Seller', 'WA_B4': 'WA Buyer'})

# 04G: Downloaded File to --> C:\Users\xyz_Name\Downloads folde
#data1.to_csv(download_path.replace("\\", "/")+"/ESB and WA Average Price Porker (45kg - 60Kg).csv",index=False,encoding='utf-8')
data1.to_csv(download_path.replace("\\", "/")+"/ESB and WA Average Price Porker (45kg - 60Kg).csv",index=False)
data2.to_csv(download_path.replace("\\", "/")+"/ESB and WA Prime Price Porker (45kg - 60Kg).csv",index=False)
data3.to_csv(download_path.replace("\\", "/")+"/ESB and WA Average Price Baconer (60.1kg - 75Kg).csv",index=False)
data4.to_csv(download_path.replace("\\", "/")+"/ESB and WA Prime Price Baconer (60.1kg - 75Kg).csv",index=False)  

# 04H: Define the titles and coordinates for each graph
graph_titles = [
    ('ESB and WA Average Price Porker (45kg - 60Kg)', 'top left', '100px', '100px'),
    ('ESB and WA Prime Price Porker (45kg - 60Kg)', 'top left', '100px', '100px'),
    ('ESB and WA Average Price Baconer (60.1kg - 75Kg)', 'top left', '100px', '100px'),
    ('ESB and WA Prime Price Baconer (60.1kg - 75Kg)', 'top left', '100px', '100px'),
]

# 04I: Create a function to add annotations to a figure
# Create a function to add annotations to a figure with a centered title
#  If you want to position the title at the top center of the figure and make only the title text bold, you can modify the add_annotations function as follows:
def add_annotations(fig, title, x_center, y_top):
    fig.add_annotation(
        text=title,  # Set the title text
        xref="paper", yref="paper",
        x=x_center, y=y_top,
        xanchor="center", yanchor="top",  # Position at the top center
        showarrow=False,
        font=dict(size=14, family="Arial, sans-serif", color="black"), # plotly does not support weight="bold"),  # Set font properties
    )

# 05: Create the layout of the web application
app.layout = html.Div([
    html.Div([
        #html.Label('Select Date Range:',style={'position': 'absolute', 'top': '0px', 'left': '1000px', 'font-size': '12px'}),
        html.Label('.'),
        dcc.RangeSlider(
            id='date-slider',
            min=pd.to_datetime(data['Date'].min()).timestamp(),
            max=pd.to_datetime(data['Date'].max()).timestamp(),
            step=7 * 24 * 3600,  # 1 week
            marks=None,
            ##marks={date.timestamp(): date.strftime('%Y-%m-%d') for date in data['Date']},
            value=[
                pd.to_datetime(data['Date'].min()).timestamp(),
                pd.to_datetime(data['Date'].max()).timestamp()
            ]
        ),
        ]),
    html.Div([
        #html.Label('Your Dashboard Title', style={'position': 'absolute', 'left': '100px', 'top': '100px', 'font-size': '24px'}),
        dcc.Graph(id='graph-01'),
        html.Button('View/Extract Data', id='extract-button-01',
                    style={'position': 'absolute', 'top': '90px', 'right': '168px'}),
        ]),
    html.Div([
        dcc.Graph(id='graph-02'),
        html.Button('View/Extract Data', id='extract-button-02',
        ##html.Button('View/Extract ESB and WA Prime Price Porker (45-60 Kg) Data', id='extract-button-02',
                    style={'position': 'absolute', 'top': '320px', 'right': '168px'}),
        ]),
    html.Div([
        dcc.Graph(id='graph-03'),
        html.Button('View/Extract Data', id='extract-button-03',
                    style={'position': 'absolute', 'top': '550px', 'right': '168px'}),
        ]),
   html.Div([
        dcc.Graph(id='graph-04'),
        html.Button('View/Extract Data', id='extract-button-04',
                    style={'position': 'absolute', 'top': '780px', 'right': '168px'}),
        ]),
    dcc.Store(id='data-store')  # Store component to hold the data for download
])

# 06: Define callback functions
@app.callback(
    [Output('graph-01', 'figure'),
     Output('graph-02', 'figure'),
     Output('graph-03', 'figure'),
     Output('graph-04', 'figure')],
    [Input('date-slider', 'value')]
)

# 07: Define update_graph
def update_graph(selected_date_range):
    filtered_data1 = data1[(data1['Date'] >= pd.to_datetime(selected_date_range[0], unit='s')) &
                         (data1['Date'] <= pd.to_datetime(selected_date_range[1], unit='s'))]
    filtered_data2 = data2[(data['Date'] >= pd.to_datetime(selected_date_range[0], unit='s')) &
                         (data['Date'] <= pd.to_datetime(selected_date_range[1], unit='s'))]
    filtered_data3 = data3[(data['Date'] >= pd.to_datetime(selected_date_range[0], unit='s')) &
                         (data['Date'] <= pd.to_datetime(selected_date_range[1], unit='s'))]
    filtered_data4 = data4[(data['Date'] >= pd.to_datetime(selected_date_range[0], unit='s')) &
                         (data['Date'] <= pd.to_datetime(selected_date_range[1], unit='s'))]

    fig1 = px.line(filtered_data1, x='Date', y=['ESB Seller', 'ESB Buyer', 'WA Seller', 'WA Buyer'])
  
    fig1.update_layout(
        title_text='<b>ESB and WA Average Price Porker (45kg - 60Kg)</b>',  # Title with <b> tags for bold
        title_x=0.5,            # Set the x-position to center
        title_y=.9, #1.2,       # Set the y-position to place it above the graph  value should be between int/float 0 and 1
        title_xanchor='center', # Center the x position
        title_font=dict(size=20, family="Arial, sans-serif", color="#808080") #, weight="bold")  # Set font properties
    )
    fig1.update_layout(xaxis_title='', yaxis_title='',legend_title_text='')
    fig1.update_yaxes(range=[y1_min_for_data1, y1_max_for_data1], dtick=100)
    fig1.update_layout(height=230)#, width=400)
    fig1.update_layout(margin=dict(l=0, r=0, t=50, b=0))        #left/right/top/bottom margin
    #fig1.update_layout(padding=dict(l=10, r=10, t=10, b=10))   #left/right/top/bottom margin
  
    fig2 = px.line(filtered_data2, x='Date', y=['ESB Seller', 'ESB Buyer', 'WA Seller', 'WA Buyer'])
    fig2.update_layout(
        title_text='<b>ESB and WA Prime Price Porker (45kg - 60Kg)</b>',  # Title with <b> tags for bold
        title_x=0.5,            # Set the x-position to center
        title_y=.9, #1.2,       # Set the y-position to place it above the graph  value should be between int/float 0 and 1
        title_xanchor='center', # Center the x position
        title_font=dict(size=20, family="Arial, sans-serif", color="#808080") #, weight="bold")  # Set font properties
    )
    fig2.update_layout(xaxis_title='', yaxis_title='',legend_title_text='')
    fig2.update_yaxes(range=[y2_min_for_data2, y2_max_for_data2], dtick=100)
    fig2.update_layout(height=230)#, width=400)
    fig2.update_layout(margin=dict(l=0, r=0, t=50, b=0))   #left/right/top/bottom margin

    fig3 = px.line(filtered_data3, x='Date', y=['ESB Seller', 'ESB Buyer', 'WA Seller', 'WA Buyer']) #, title='ESB and WA Average Price Baconer (60.1kg - 75Kg)')
    fig3.update_layout(
        title_text='<b>ESB and WA Average Price Baconer (60.1kg - 75Kg)</b>',  # Title with <b> tags for bold
        title_x=0.5,            # Set the x-position to center
        title_y=.9, #1.2,       # Set the y-position to place it above the graph  value should be between int/float 0 and 1
        title_xanchor='center', # Center the x position
        title_font=dict(size=20, family="Arial, sans-serif", color="#808080") #, weight="bold")  # Set font properties
    )
    fig3.update_layout(xaxis_title='', yaxis_title='',legend_title_text='')
    fig3.update_yaxes(range=[y3_min_for_data3, y3_max_for_data3], dtick=100)
    fig3.update_layout(height=230)#, width=400)
    fig3.update_layout(margin=dict(l=0, r=0, t=50, b=0))   #left/right/top/bottom margin

    fig4 = px.line(filtered_data4, x='Date', y=['ESB Seller', 'ESB Buyer', 'WA Seller', 'WA Buyer'], title='ESB and WA Prime Price Baconer (60.1kg - 75Kg)')
    fig4.update_layout(
        title_text='<b>ESB and WA Prime Price Baconer (60.1kg - 75Kg)</b>',  # Title with <b> tags for bold
        title_x=0.5,            # Set the x-position to center
        title_y=.9, #1.2,       # Set the y-position to place it above the graph  value should be between int/float 0 and 1
        title_xanchor='center', # Center the x position
        title_font=dict(size=20, family="Arial, sans-serif", color="#808080") #, weight="bold")  # Set font properties
    )
    fig4.update_layout(xaxis_title='', yaxis_title='',legend_title_text='')
    fig4.update_yaxes(range=[y4_min_for_data4, y4_max_for_data5], dtick=100)
    fig4.update_layout(height=230)#, width=400)
    fig4.update_layout(margin=dict(l=0, r=0, t=50, b=0))   #left/right/top/bottom margin

    return fig1, fig2, fig3, fig4


# 08: Define callback functions for output
@app.callback(
    Output('data-store', 'data'),
    [Input('extract-button-01', 'n_clicks'),
     Input('extract-button-02', 'n_clicks'),
     Input('extract-button-03', 'n_clicks'),
     Input('extract-button-04', 'n_clicks')],
    [State('date-slider', 'value')]
)

# 09: Define extract data function with click extract button
def extract_data(n_clicks_01, n_clicks_02, n_clicks_03, n_clicks_04, selected_date_range):
    ctx = dash.callback_context
    if not ctx.triggered:
        return None

    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if triggered_id == 'extract-button-01':
##        csv_string = data1.to_csv(index=False,encoding='utf-8')
##        return {
##            'content': csv_string,
##            'filename': 'ESB and WA Average Price Porker (45kg - 60Kg).csv'  # Specify the desired filename
##        }
        filtered_data1 = os.startfile(download_path +'\ESB and WA Average Price Porker (45kg - 60Kg).csv')
        return filtered_data1
    elif triggered_id == 'extract-button-02':
        filtered_data2 = os.startfile(download_path +'\ESB and WA Prime Price Porker (45kg - 60Kg).csv')
        return filtered_data2
    elif triggered_id == 'extract-button-03':
        filtered_data3 = os.startfile(download_path +'\ESB and WA Average Price Baconer (60.1kg - 75Kg).csv')
        return filtered_data3
    elif triggered_id == 'extract-button-04':
        filtered_data4 = os.startfile(download_path +'\ESB and WA Prime Price Baconer (60.1kg - 75Kg).csv')
        return filtered_data4
    
# 00: main calling program     
if __name__ == '__main__':
    app.run_server(host="0.0.0.0",debug=True)
    #app.run_server(host="127.0.0.1",debug=True)


