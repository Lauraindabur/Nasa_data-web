
"""
EL VENV ES UN ENTORNO VIRTUAL DONDE TENGO DESCARGADO EL PAQUETE REQUESTS 
PARA USARLO EN EL PROTECTO CON APIS 
"""""

import requests  #Me ayuda a llamar las apis 
print(requests.__version__) # Para PROBAR que si unciona pues es una libreria

   
#daay =  input("Escribe el dia en  formato  AAAA-MM-DD: ")
daay = "2015-11-23"
api_key = "gTsNYxtZddgLPxLBzamQoKV5e9yYqgSGxDP39Wd4"   # API KEY DE LA PAGINA DE LA NASA (COOREO ISNT)

URL_EPIC =  f"https://api.nasa.gov/EPIC/api/natural/date/{daay}?api_key={api_key}" 
print(URL_EPIC) # URL DE LA API QUE ME DA LAS IMAGENES DE LA NASA

respuesta= requests.get(URL_EPIC) # HAGO LA PETICION A LA API Y ME DEVUELVE UN JSON CON LOS DATOS DE ESA FECHA
# print(respuesta) ME DEBE SALIR 200 PQ TODO SALIO BIEN  

datos = respuesta.json() # CONVIERTO EL JSON EN UN DICCIONARIO DE PYTHON    

datos_lim=datos[:5]   #Soloq iero hacer get de las primeras 5 iamgenes de la lsita de datos (api)

""""
for dato in datos_lim:
    coords = dato["centroid_coordinates"]
    print("Latitud:", coords["lat"], "| Longitud:", coords["lon"])
"""

for dato in datos_lim:
    imagen = dato["image"]
    print("Imagen:", imagen)
    fecha = daay.split("-")  #dividir la echa en partes para obtener dia mes año  AAAA-MM-DD
    año = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    url_imagen = f"https://epic.gsfc.nasa.gov/archive/natural/{año}/{mes}/{dia}/png/{imagen}.png" # URL DE LA IMAGEN QUE QUIERO DESCARGAR

    #TRY CATCH POR SI NO ENCUENTRA LA IMAGEN EN PNG
    response= requests.get(url_imagen) # HAGO LA PETICION A LA API Y ME DEVUELVE UN JSON CON LOS DATOS DE ESA FECHA

    if response.status_code != 200:
        url_imagen2 = f"https://epic.gsfc.nasa.gov/archive/natural/{año}/{mes}/{dia}/jpg/{imagen}.jpg"
        print(url_imagen2)
    else:
        url_imagen2 = f"https://epic.gsfc.nasa.gov/archive/natural/{año}/{mes}/{dia}/png/{imagen}.png"
        print(url_imagen2)

