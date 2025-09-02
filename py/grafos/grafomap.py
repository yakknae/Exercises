import networkx as nx
import matplotlib.pyplot as plt

# -- Crear el grafo
G = nx.Graph()

# -- Informacion sobre las provincias
nodos = {
    'Buenos Aires': {
        'capital': 'La Plata',
        'poblacion': 17541141,
        'superficie': 305907.4,
        'lat': -34.9210,  
        'lon': -57.9545    
    },
    'Córdoba': {
        'capital': 'Córdoba',
        'poblacion': 3760450,
        'superficie': 164707.8,
        'lat': -31.4201,
        'lon': -64.1888
    },
    'Santa Fe': {
        'capital': 'Santa Fe',
        'poblacion': 3536418,
        'superficie': 133249.1,
        'lat': -31.6333,
        'lon': -60.7000
    },
    'Mendoza': {
        'capital': 'Mendoza',
        'poblacion': 1990338,
        'superficie': 149069.2,
        'lat': -32.8895,
        'lon': -68.8458
    },
    'Tucumán': {
        'capital': 'San Miguel de Tucumán',
        'poblacion': 1694656,
        'superficie': 22592.1,
        'lat': -26.8083,
        'lon': -65.2167
    },
    'Salta': {
        'capital': 'Salta',
        'poblacion': 1424397,
        'superficie': 155340.5,
        'lat': -24.7833,
        'lon': -65.4167
    },
    'Entre Ríos': {
        'capital': 'Paraná',
        'poblacion': 1385961,
        'superficie': 78383.7,
        'lat': -31.7333,
        'lon': -60.5167
    },
    'San Juan': {
        'capital': 'San Juan',
        'poblacion': 781217,
        'superficie': 88296.2,
        'lat': -31.5375,
        'lon': -68.5364
    },
    'Chaco': {
        'capital': 'Resistencia',
        'poblacion': 1204541,
        'superficie': 99763.3,
        'lat': -27.4516,
        'lon': -58.9862
    },
    'Corrientes': {
        'capital': 'Corrientes',
        'poblacion': 1120801,
        'superficie': 89123.3,
        'lat': -27.4667,
        'lon': -58.8333
    },
    'San Luis': {
        'capital': 'San Luis',
        'poblacion': 508328,
        'superficie': 75347.1,
        'lat': -33.2833,
        'lon': -66.3333
    },
    'Catamarca': {
        'capital': 'San Fernando del Valle de Catamarca',
        'poblacion': 415438,
        'superficie': 101486.1,
        'lat': -28.4667,
        'lon': -65.7833
    },
    'La Pampa': {
        'capital': 'Santa Rosa',
        'poblacion': 358428,
        'superficie': 143492.5,
        'lat': -36.6203,
        'lon': -64.2900
    },
    'Formosa': {
        'capital': 'Formosa',
        'poblacion': 605193,
        'superficie': 75488.3,
        'lat': -26.1847,
        'lon': -58.1750
    },
    'Neuquén': {
        'capital': 'Neuquén',
        'poblacion': 664057,
        'superficie': 94422.0,
        'lat': -38.9513,
        'lon': -68.0975
    },
    'Misiones': {
        'capital': 'Posadas',
        'poblacion': 1261294,
        'superficie': 29911.4,
        'lat': -27.3667,
        'lon': -55.8967
    },
    'La Rioja': {
        'capital': 'La Rioja',
        'poblacion': 393531,
        'superficie': 91493.7,
        'lat': -29.4167,
        'lon': -66.8500
    },
    'Jujuy': {
        'capital': 'San Salvador de Jujuy',
        'poblacion': 770881,
        'superficie': 53244.2,
        'lat': -24.1850,
        'lon': -65.2994
    },
    'Río Negro': {
        'capital': 'Viedma',
        'poblacion': 747610,
        'superficie': 202168.6,
        'lat': -40.8000,
        'lon': -62.9667
    },
    'Chubut': {
        'capital': 'Rawson',
        'poblacion': 618994,
        'superficie': 224302.3,
        'lat': -43.3000,
        'lon': -65.1000
    },
    'Santa Cruz': {
        'capital': 'Río Gallegos',
        'poblacion': 365698,
        'superficie': 244457.5,
        'lat': -51.6200,
        'lon': -69.2167
    },
    'Tierra del Fuego, Antártida e Islas del Atlántico Sur': {
        'capital': 'Ushuaia',
        'poblacion': 173715,
        'superficie': 910324.4,
        'lat': -54.8072,
        'lon': -68.3072
    },
    'Ciudad Autónoma de Buenos Aires': {
        'capital': 'Ciudad Autónoma de Buenos Aires',
        'poblacion': 3075646,
        'superficie': 205.9,
        'lat': -34.6037,
        'lon': -58.3816
    },
    'Santiago del Estero': {
        'capital': 'Santiago del Estero',
        'poblacion': 978313,
        'superficie': 136934.3,
        'lat': -27.7833,
        'lon': -64.2667
    }
}
# -- Agregar todos los nodos
for provincia, info in nodos.items():
    G.add_node(info['capital'],provincia=provincia,poblacion=info['poblacion'],superficie=info['superficie'],lat=info['lat'],lon=info['lon'])

# -- Informacion sobre las aristas
aristas = [
    ('La Plata', 'Córdoba', 780),
    ('La Plata', 'Santa Fe', 520),
    ('La Plata', 'Paraná', 480),
    ('La Plata', 'Santa Rosa', 650),
    ('La Plata', 'Viedma', 900),
    ('La Plata', 'Ciudad Autónoma de Buenos Aires', 50),

    ('Córdoba', 'Santa Fe', 440),
    ('Córdoba', 'San Luis', 280),
    ('Córdoba', 'La Rioja', 550),
    ('Córdoba', 'San Fernando del Valle de Catamarca', 600),
    ('Córdoba', 'Santa Rosa', 500),

    ('Santa Fe', 'Paraná', 180),
    ('Santa Fe', 'Resistencia', 520),
    ('Santa Fe', 'Santiago del Estero', 460),
    ('Paraná', 'Corrientes', 300),

    ('Resistencia', 'Corrientes', 350),
    ('Resistencia', 'Formosa', 250),
    ('Resistencia', 'Salta', 850),

    ('Corrientes', 'Posadas', 300),

    ('Salta', 'San Salvador de Jujuy', 240),
    ('Salta', 'San Miguel de Tucumán', 240),
    ('Salta', 'Formosa', 900),

    ('San Miguel de Tucumán', 'Santiago del Estero', 400),

    ('San Juan', 'San Luis', 250),
    ('San Juan', 'Mendoza', 220),
    ('San Juan', 'La Rioja', 300),

    ('San Luis', 'Mendoza', 300),
    ('San Luis', 'Santa Rosa', 400),

    ('Mendoza', 'Neuquén', 400),

    ('Neuquén', 'Viedma', 200),
    ('Viedma', 'Rawson', 600),
    ('Rawson', 'Río Gallegos', 800),
    ('Río Gallegos', 'Ushuaia', 500),

    ('Santa Rosa', 'La Plata', 650),
    ('Santa Rosa', 'Córdoba', 500),
    ('Santa Rosa', 'San Luis', 400),
    ('Santa Rosa', 'Viedma', 550),

    ('Ciudad Autónoma de Buenos Aires', 'La Plata', 50),
]

# -- Agregar aristas al grafo
for ciudad1, ciudad2, distancia in aristas:
    G.add_edge(ciudad1,ciudad2,costo=distancia)

# -- Visualizar los nodos y aristas
plt.figure(figsize=(16,12))
# -- Distancias entre nodos y aristas
#pos = nx.kamada_kawai_layout(G)

# Posición real: longitud (x), latitud (y)
pos = {info['capital']: (info['lon'], info['lat']) for info in nodos.values()}

# -- Dibujar grafo
nx.draw(G, pos,
        with_labels=True,
        node_color='lightblue',
        node_size=600,
        font_size=8,
        font_weight='bold',
        edge_color='gray',
        alpha=0.9)

# Etiquetas de distancias
edge_labels= nx.get_edge_attributes(G,'costo')
nx.draw_networkx_edge_labels(G,pos,edge_labels,font_size=6,font_color='red')

plt.title("grafo: ciudades Argentinas y distancias")
plt.axis('equal')
plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.tight_layout()
plt.show()