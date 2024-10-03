
import dash
#import webbrowser
#import threading


#dcc.Loading


from bibli_funciones import  ejecucion_demanda_parte_2, dem_total, Aplicativo

#global 
#option_usuario_3_a, usuario_atipico

#tabla_datos_totales_final_dem_a, datos_frecuencia_desviaciones_dem_a, tabla_datos_desviaciones_final_dem_a, tabla_dem_total_a = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

url = 'http://127.0.0.1:8050'

#def open_browser():
#    webbrowser.open(url)
    
app = dash.Dash(  __name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}], prevent_initial_callbacks='initial_duplicate',  suppress_callback_exceptions=True)
server = app.server

Aplicativo(app, url, ejecucion_demanda_parte_2, dem_total)

if __name__ == "__main__":
    #threading.Timer(1, open_browser).start()
    app.run_server(debug=True)
