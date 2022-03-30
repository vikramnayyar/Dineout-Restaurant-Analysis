# deployment: https://dataviz.shef.ac.uk/blog/03/07/2020/Deploy-Your-Dash-App
#

#%% Importing libraries
# from tkinter import OFF
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input

# from matplotlib.pyplot import figure
import plotly.express as px
import plotly.graph_objects as go

import dash_bootstrap_components as dbc
import pandas as pd
# import pandas_datareader.data as web


#%% 
df = pd.read_csv('data/dash_data.csv')

df_state = df.groupby('State').mean()
df_state.reset_index(level=0, inplace=True)
df_state = df_state.sort_values("Votes", ascending=False)
df_state = df_state.round(2)


# %% App Layout & Bootstrap
# ref: https://hackerthemes.com/bootstrap-cheatsheet/

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server   # added as deployment was not working

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}



sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Number of students per education level", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


# App Layout
app.layout = dbc.Container([
    dbc.Row([   
        dbc.Col(html.H1("Dineout Restaurants in India", 
        className='text-center text-secondary, mb-4'), 
        width = 12)
    ]),

    
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id='selected_feature', multi=False, value='Bengal',
                        options=[{'label':x, 'value':x}
                                for x in sorted(df_state['State'].unique())],
                        ),            
            
            dcc.Graph(id='intro-table', figure={})
        ], # width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=5, xl=5        
    ),

        dbc.Col([
            dcc.Graph(id='fig_3', figure={})
        ], # width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=5, xl=5        
    ),

    ]),

    dbc.Row([
            dbc.Col([
                dcc.Graph(id='viz-plot', figure={})
            ], # width={'size':5, 'offset':1, 'order':1},
                xs=12, sm=12, md=12, lg=5, xl=5        
            ),
        dbc.Col([
            dcc.Graph(id='fig_4', figure={})
        ], # width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=5, xl=5        
    ),

    ])




])

# %%  Running Plots

# %%--------- Figure 1
@app.callback(
    Output('intro-table', 'figure'),
    Input('selected_feature', 'value')
)
def update_graph(selected_feature):

    df_state = df[df["State"] == selected_feature]
    state_localities = df_state["Locality"].value_counts()
    state_localities = state_localities.sort_values(ascending= True)

    fig = px.bar(y = state_localities.index, x=state_localities, color=state_localities, orientation = 'h',
                labels = {
                    'color': 'Total' +'<br>'+ 'Restaurants'
                }) # color continuous scale
    fig.update_layout(yaxis_title = 'Localities', xaxis_title = 'Total Restaurants', 
                    title_text='Restaraunt Distribution Across State', 
                    title_x=0.5,
                    paper_bgcolor='rgba(0,0,0,0)', 
                    title_font_color = '#4B0082'
                    # plot_bgcolor='rgba(0,0,0,0)',                    
                    # font=dict(
                    #     family="Courier New, monospace",
                    #     size=12,
                    #     color='rgb(12, 128, 128)'
                    # )
                    )
    
    
    return fig




# %%--------- Figure 2
@app.callback(
    Output('viz-plot', 'figure'),
    Input('selected_feature', 'value')
)
def update_graph(selected_feature):

    def cuisine_info(state):
        state_cuisines_clean =[]
        
    #     Forming state dataframe
        filter = (df['State'] == state)
        df_state = df[filter].copy() 
        
    #     Filtering cuisines
        state_cuisines = df_state['Cuisine'].str.split(',').explode().unique().tolist()
        
    #     Removing 'Multi-Cuisine' category from cuisines    
        a = 'Multi-Cuisine'
        b = '  Multi-Cuisine'
        if a in state_cuisines:
            state_cuisines.remove('Multi-Cuisine')
        if b in state_cuisines:
            state_cuisines.remove('  Multi-Cuisine')

        
        for word in state_cuisines:
            word = word.replace('  ', '')
            state_cuisines_clean.append(word)
        
    #     Removing duplicates from cuisines list
        state_cuisines_clean = np.unique(state_cuisines_clean)
        state_cuisines_clean
        
    #     Forming state cuisine dataframe    
        df_filtered = pd.DataFrame()
        df_cuisine_state = pd.DataFrame()

        # Forming cuisine df for state
        for cuisine in state_cuisines_clean:
            df_state['Cuisine Verification'] = df_state['Cuisine'].str.contains(cuisine, case=False, na=False).astype(int)
            df_filtered = df_state[df_state['Cuisine Verification'] == 1]

            total_restnt = len(df_filtered.index)
            total_votes = len(df_filtered.index)
            df_state = df_state.drop(['Cuisine Verification'], axis=1)

            avg_rating = df_filtered['Rating'].sum()/total_restnt

            df_cuisine_state = df_cuisine_state.append({'Cuisine': cuisine, 'Total Restaurants': total_restnt, 'Total Votes': total_votes, 'Rating':avg_rating}, ignore_index=True)
    
        return df_cuisine_state
    
    import numpy as np
    cuisine = cuisine_info(selected_feature)
    # Filtering top cusines 
    top_cuisine = cuisine[cuisine['Total Votes']>50].reset_index(drop = True)
    top_cuisine.sort_values(by='Rating', ascending=False, inplace=True)
    top_cuisine.reset_index(inplace = True, drop=True)
    top_cuisine['Total Votes'] = top_cuisine['Total Votes'].astype('str') + ' votes'    

    # Plotting Maharashtra cuisines
    top_cuisine['State'] = selected_feature
    fig = px.treemap(top_cuisine, 
                    path=['State', 'Cuisine', 'Total Votes'], 
                    values='Rating',
                    color='Rating',
                    labels = {'Votes'}
                    )
    fig.update_layout( title_text = 'Favourite Cuisines',
                    title_font_color = '#4B0082',
                    title_x = 0.5,
                    paper_bgcolor='rgba(0,0,0,0)', 
                    plot_bgcolor='rgba(0,0,0,0)'
                    )
    return fig



# %% Figure 3

@app.callback(
    Output('fig_3', 'figure'),
    Input('selected_feature', 'value')
)
def update_graph(selected_feature):

    # Extracting localities
    df_state = df[df["State"] == selected_feature]

    locality_list = df_state.Locality.value_counts().index.tolist()
    
    # Obtaining total votes
    def total_votes(locality):
        df_x = df_state[df_state['Locality'] == locality]
        total_votes = df_x['Votes'].sum()
        return total_votes

    total_votes_value = []
    total_votes_list = []
    for index, locality in enumerate(locality_list):
        total_votes_value = total_votes(locality) 
        total_votes_list.append(total_votes_value)
    
    # Locality-wise total restuarants in Maharashtra 
    # location_counts = df_state['Locality'].value_counts()

    # Zipping required lists and forming dataframe
    list_of_tuples = list(zip(locality_list, total_votes_list))
    locations_df = pd.DataFrame(list_of_tuples, columns = ['Location', 'Total Votes'])
    

    #     Adding attributes to the localities dataframe
    df_location = pd.DataFrame()
    rating_list = []
    cost_list = []
    location_rating_list = []
    location_cost_list = []

    for index, location in enumerate(locations_df['Location']):
        df_location = df[df['Locality'] == location]

    #     Calculating average rating

        for rating in df_location["Rating"]:
            rating_list.append(rating)
        avg_rating = sum(rating_list)/len(rating_list)
        location_rating_list.append(avg_rating)
        
    #     Calculating average cost

        for cost in df_location["Cost"]:
            cost_list.append(cost)
        avg_cost = sum(cost_list)/len(cost_list)
        location_cost_list.append(avg_cost)

#     Adding attributes to the dataframe
    locations_df['Rating'] = location_rating_list
    locations_df['Cost'] = location_cost_list
    # karnataka_locations_df.head(20)

    top_locations = locations_df[locations_df['Total Votes']>100]
    top_locations["State"] = selected_feature

    fig = px.treemap(top_locations, 
                 path=['State', 'Location', 'Total Votes'], 
                 values='Rating',
                 color='Rating',
                 labels = {'Votes'}
                )
    fig.update_layout( title_text = 'Top Localities',
                    title_font_color = '#4B0082',
                    title_x = 0.5,
                    paper_bgcolor='rgba(0,0,0,0)', 
                    plot_bgcolor='rgba(0,0,0,0)',
                    )
# fig.show()


    return fig







# %%--------- Figure 4
@app.callback(
    Output('fig_4', 'figure'),
    Input('selected_feature', 'value')
)
def update_graph(selected_feature):

    restnt_state = df['State'].value_counts()
    a = restnt_state.index
    b = restnt_state
    df_state_restnts = pd.DataFrame(list(zip(a,b)))
    df_state_restnts.columns = ['State', 'Total Restaurants']
    df_state_restnts = df_state_restnts.set_index('State')

    # grouping df state-wise
    df_state = df.groupby('State').mean()
    df_state.reset_index(level=0, inplace=True)
    df_state = df_state.set_index('State')

    # Matching indices of df_state_restnts with df_state 
    df_state_restnts.reindex(df_state.index)

    # Adding total restaurants column to state dataframe  
    df_state['Total Restaurants'] = df_state_restnts['Total Restaurants']


    # Normalizing columns with integer values
    df_state_normalized = df_state.copy()
    columns = ['Rating', 'Votes', 'Cost', 'Total Restaurants']

    # apply normalization techniques
    for column in columns:
        df_state_normalized[column] = (df_state_normalized[column] / df_state_normalized[column].abs().max())

    # view normalized data
    df_state_normalized.reset_index(level=0, inplace=True)


    df_state_normalized = df_state_normalized[df_state_normalized["State"] == selected_feature]
    df_state_normalized.reset_index(inplace = True)

    r = [df_state_normalized['Rating'][0], df_state_normalized['Votes'][0], df_state_normalized['Cost'][0], df_state_normalized['Total Restaurants'][0]]
    theta=['Rating', 'Votes', 'Cost', 'Total Restaurants']


    fig = go.Figure(
        data=[
            go.Scatterpolar(r=r, theta=theta, fill='toself', name= selected_feature)
        ],
        layout=go.Layout(
            title=go.layout.Title(text='Overall Performance'),
            title_x = 0.5,
            polar={'radialaxis': {'visible': False}},
            showlegend=True,
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
        )
    )
    fig.update_layout(
        title_font_color = '#4B0082',
    )
    
    
    
    return fig





# %%
if __name__=='__main__':
    # app.run_server(debug=True, port=8000)   # use this for local deployment
    app.run_server(debug=True)    # port should not be alloted to heroku 