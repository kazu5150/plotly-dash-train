import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px


app =  dash.Dash(__name__)

month = ["1月","2月","3月","4月","5月","6月","7月",
         "8月","9月","10月","11月","12月"]
devident = [3500,500,200,0,100,40,20,10,0,560,2340,1230,]

month_name =  "配当受取月"
devidend_name = "配当金"

df =  pd.DataFrame({
    month_name : month,
    devidend_name : devident
})

fig = px.line(df, x=month_name, y=devidend_name)



app.layout = html.Div(children=[
    html.H1(children="資産管理"),
    html.Div(children="配当金グラフ"),
    dcc.Graph(
        id = "devidend_graph",
        figure = fig
    )
                      ])

if __name__ == '__main__':
    app.run_server(debug=False, host= '127.0.0.1', port=8000)
