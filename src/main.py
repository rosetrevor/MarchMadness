import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

def main():
    app = dash.Dash()
    app.title = "March Madness"
    server = app.server

    app.layout = dbc.Container(
        [
            dbc.Row(html.H1("March Madness with Dash")),
            dbc.Row(html.H5("Trevor Rose"))
        ]
    )
    app.run_server(debug=False)

if __name__ == "__main__":
    main()