import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go


#Define Global df for 'On_Click' event in 'PairedBar_withValues_withOnClick_df()':
global global_CurrDf

# Add_values to each bar:
def autolabel(ax, rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center',
                    va='bottom'
                    )

def PairedBar_withValues_withOnClick_df(df,labels, col_bar1, col_bar2, label_bar1, label_bar2, y_title, graph_title, color1, color2):
    global global_CurrDf
    global_CurrDf = df

    x_coord = np.arange(len(df))  # the label locations
    width_bar = 0.4  # the width of the bars
    x_labels_list = df[labels]

    #Create different labels for 'on_click' event:
    x_labels_list_for_wedge1 = []
    x_labels_list_for_wedge2 = []
    for l in x_labels_list:
        x_labels_list_for_wedge1.append(l+"_1")
        x_labels_list_for_wedge2.append(l+"_2")
    #print(f"labels_list_for_wedge1: {x_labels_list_for_wedge1}")
    #print (f"labels_list_for_wedge2: {x_labels_list_for_wedge2}")

    # plt.subplots() returns:
    #   fig=Figure;
    #   ax=axes.Axes object or array of Axes objects( if more than one subplot was created).
    #  figsize : (width, height)
    #  facecolor : the background color
    fig, ax = plt.subplots(figsize=(17, 8))    #size of Graph's window

    # Get HEXA code of Color => https://www.color-hex.com/color/006d2c
    rects1 = ax.bar( x=(x_coord-width_bar/2), height=df[col_bar1], width=width_bar, label=label_bar1, color=color1)
    rects2 = ax.bar( x=(x_coord+width_bar/2), height=df[col_bar2], width=width_bar, label=label_bar2, color=color2)

    #Create invisable Bar for 'on_click' event => to return Label ---------------------
    wedges1 = ax.bar(x=(x_coord-width_bar/2), height=df[col_bar1], width=width_bar, label=x_labels_list_for_wedge1, fill=False, linewidth=0)
    wedges2 = ax.bar(x=(x_coord+width_bar/2), height=df[col_bar2], width=width_bar, label=x_labels_list_for_wedge2, fill=False, linewidth=0)

    # Assign a label to each of the artist to be retrieved later:
    for w1, w2, l1, l2 in zip(wedges1, wedges2, x_labels_list_for_wedge1, x_labels_list_for_wedge2):
        w1.set_label(l1)
        w2.set_label(l2)

    make_picker(fig, wedges1)
    make_picker(fig, wedges2)
    # -------------------------------------------------------------------------------

    # Add some text for labels, title and custom x-axis tick labels, etc:
    ax.set_ylabel(y_title)
    ax.set_title(graph_title)

    ax.set_xticks(x_coord)
    ax.set_xticklabels(x_labels_list)                       #Show Label's name and not just their index on X-axes
    ax.legend((rects1, rects2), (label_bar1, label_bar2))   #Show specified labels in the labelBar

    autolabel(ax, rects1)
    autolabel(ax, rects2)

    fig.tight_layout()
    plt.show()

# What to do on_click!!!
def action_onClick(label):
    global global_CurrDf

    state_abbr = label[:-2]
    # print(label)
    #print(state_abbr )
    #print( global_CurrDf[ global_CurrDf["State_abbr"] == state_abbr])    #get row with wanted value (=state)

    curr_state_df = global_CurrDf[global_CurrDf["State_abbr"] == state_abbr]
    print(curr_state_df)

    t_NO = curr_state_df.T[1:5]
    t_NO['State'] = state_abbr
    t_NO.reset_index(inplace=True)
    t_NO.columns=['Income', 'Value', 'State']

    t_FB = curr_state_df.T[5:9]
    t_FB['State'] = state_abbr
    t_FB.reset_index(inplace=True)
    t_FB.columns = ['Income', 'Value', 'State']

    print("NEW:\n")
    print(t_NO)
    print(t_FB)

    #Graph =>  #Important! Number of colors MUST be as a number of 'values_for_pivot' => len(t_FB) = len(t_NO)
    # Get HEXA code of Color =>  https://www.color-hex.com/color/006d2c
    colors_greens  = ["#006D2C", "#31A354", "#74C476", "#99c4aa"]
    colors_violets = ["#1F006D", "#624c98", "#8f7fb6","#bbb2d3"]
    if (label[-2:] == "_1"):     #For 'NO'
        bars_with_layers_for_each_category_graph_using_Pivot(df=t_NO,
                                                             index_for_pivot= 'State',
                                                             columns_for_pivot='Income',
                                                             values_for_pivot='Value',
                                                             layers_list= t_NO['Income'],
                                                             colors=colors_violets)
    else:   # => (label[-2:] == "_2") => For 'FB'
        bars_with_layers_for_each_category_graph_using_Pivot(df=t_FB,
                                                             index_for_pivot='State',
                                                             columns_for_pivot='Income',
                                                             values_for_pivot='Value',
                                                             layers_list=t_FB['Income'],
                                                             colors=colors_greens )

def onclick(event):
    wedge= event.artist
    label = wedge.get_label()
    #print(label)
    action_onClick (label)

def make_picker(fig, wedges):
    for wedge in wedges:
        wedge.set_picker(True)
    fig.canvas.mpl_connect('pick_event', onclick)

#------------------------------------------------------
def PairedBar_withValues_df(df,labels, col_bar1, col_bar2, label_bar1, label_bar2, y_title, graph_title, color1, color2):
    x = np.arange(len(df))  # the label locations
    width = 0.4  # the width of the bars

    fig, ax = plt.subplots(figsize=(17, 8))

    # Get HEXA code of Color => https://www.color-hex.com/color/006d2c
    rects1 = ax.bar(x - width/2, df[col_bar1], width, label=label_bar1, color =color1)
    rects2 = ax.bar(x + width/2, df[col_bar2], width, label=label_bar2, color =color2)

    # Add some text for labels, title and custom x-axis tick labels, etc:
    ax.set_ylabel(y_title)
    ax.set_title(graph_title)

    ax.set_xticks(x)
    ax.set_xticklabels(df[labels])
    ax.legend()

    autolabel(ax, rects1)
    autolabel(ax, rects2)

    fig.tight_layout()
    plt.show()

#-----------------------------------------------------------------------------------------------------------------
"""
The PIVOT function takes the follow arguments:
    INDEX (= what you want on the X-axis), 
    COLUMNS (=what you want as the LAYERS in the stack), 
    VALUES (=the value to use as the HEIGHT of each layer). 
Note that there needs to be a UNIQUE COMBINATION of (index , column values) for each number in the values column in order for this to work.

The end result is a new dataframe with the data oriented (reshaped DataFrame organized by given index/column values),
 so the default Pandas stacked plot works perfectly.
"""
def bars_with_layers_for_each_category_graph_using_Pivot(df, index_for_pivot, columns_for_pivot, values_for_pivot, layers_list,colors):
    pivot_df = df.pivot(index=index_for_pivot, columns=columns_for_pivot, values=values_for_pivot)
    print(f"pivot_df\n {pivot_df}")

    # Note: .loc[:,['Jan','Feb', 'Mar']] is used here to rearrange the layer ordering
    pivot_df.loc[:, layers_list].plot.bar(stacked=True, color=colors, figsize=(7, 5))
    plt.show()

#--------------------------------------------------------------------------------------------------------------

def US_Map_with_Text(df, Zval_to_present_on_graph,locations_val, color_base, text_on_select, cbar_title):
    fig = go.Figure ( data=go.Choropleth (
        locations=df[locations_val],
        z=df[Zval_to_present_on_graph].astype(float),   # th
        locationmode='USA-states',      # Change for other Countries!
        colorscale= color_base,
        autocolorscale=False,
        text = text_on_select,          # This is the categorical value for each element
        marker_line_color ='black',     # line markers between states
        colorbar_title = cbar_title
    ))

    fig.update_layout(
        title_text='2017 US Naturalization (US-citizenship which is granted to foreign citizens) by States <br>',
        geo=dict(
            scope='usa',
            projection=go.layout.geo.Projection(type='albers usa'),
            showlakes=False,  # lakes
            lakecolor='rgb(255, 255, 255)'),
    )
    fig.show()

#-----------------------------------------------------------------------------------------------------------------------



