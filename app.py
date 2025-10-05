from flask import Flask, render_template

app = Flask(__name__)

# Datos completos, ahora con RUTAS LOCALES (.mp4)
db = {
  "portada": {
    "titulo": "Five Nights at Freddy's: Expediente Confidencial",
    "subtitulo": "Tu acceso a los archivos de Freddy Fazbear's Pizza.",
    "imagen_portada": "/static/images/portada.jpg"
  },
  "personajes": [
    {
      "id": 1,
      "nombre": "Freddy Fazbear",
      "descripcion": "El oso líder de la banda y el personaje principal del primer juego. Es el más inteligente de los animatrónicos originales y su comportamiento se activa cuando la energía de la pizzería es baja. Su jumpscare es el más aterrador.",
      "imagen": "/static/images/fnaf1/freddy.png",
      "video": "/static/videos/freddy_fazbear.mp4", # RUTA MP4
      "juego": "FNAF 1"
    },
    {
      "id": 2,
      "nombre": "Bonnie the Bunny",
      "descripcion": "El conejo guitarrista de la banda. Es conocido por ser el animatrónico más activo de todos, moviéndose muy rápido y atacando por la puerta izquierda de la oficina. Sus ojos rojos brillan en la oscuridad.",
      "imagen": "/static/images/fnaf1/bonnie.png",
      "video": "/static/videos/bonnie_the_bunny.mp4", # RUTA MP4
      "juego": "FNAF 1"
    },
    {
      "id": 3,
      "nombre": "Chica the Chicken",
      "descripcion": "La gallina con un cupcake. Chica deambula por la cocina, lo que hace que sea imposible verla en las cámaras. Es la única animatrónica con una cara destrozada. Su jumpscare es sorpresivo.",
      "imagen": "/static/images/fnaf1/chica.png",
      "video": "/static/videos/chica_the_chicken.mp4", # RUTA MP4
      "juego": "FNAF 1"
    },
    {
      "id": 4,
      "nombre": "Foxy the Pirate Fox",
      "descripcion": "El zorro pirata que se esconde en Pirate Cove. Foxy es el más rápido de todos los animatrónicos y te atacará si no lo vigilas. Es conocido por su rapidez y sus ojos blancos brillantes.",
      "imagen": "/static/images/fnaf1/foxy.png",
      "video": "/static/videos/foxy_the_pirate_fox.mp4", # RUTA MP4
      "juego": "FNAF 1"
    },
    {
      "id": 5,
      "nombre": "Golden Freddy",
      "descripcion": "Una versión fantasmal y dorada de Freddy. Golden Freddy aparece aleatoriamente en la oficina y si lo miras, tu juego colapsará. Es un personaje clave en la historia de la saga.",
      "imagen": "/static/images/fnaf1/golden_freddy.png",
      "video": "/static/videos/golden_freddy.mp4", # RUTA MP4
      "juego": "FNAF 1"
    },
    {
      "id": 6,
      "nombre": "Toy Freddy",
      "descripcion": "Una versión más brillante de Freddy. A diferencia del Freddy original, Toy Freddy es más pequeño y amigable, aunque su jumpscare es igualmente aterrador. Sus ojos son azules y su traje es más brillante.",
      "imagen": "/static/images/fnaf2/toy_freddy.png",
      "video": "/static/videos/toy_freddy.mp4", # RUTA MP4
      "juego": "FNAF 2"
    },
    {
      "id": 7,
      "nombre": "Toy Bonnie",
      "descripcion": "Una versión más moderna de Bonnie. Toy Bonnie es mucho más rápido y activo, y ataca por el conducto de ventilación derecho de la oficina. Sus ojos son grandes y expresivos.",
      "imagen": "/static/images/fnaf2/toy_bonnie.png",
      "video": "/static/videos/toy_bonnie.mp4", # RUTA MP4
      "juego": "FNAF 2"
    },
    {
      "id": 8,
      "nombre": "Toy Chica",
      "descripcion": "Una versión más pequeña de Chica. Toy Chica se mueve por la ventilación y es conocida por quitarse el pico y los ojos. Su jumpscare es inesperado y aterrador. Su cupcake es pequeño y con forma de vela.",
      "imagen": "/static/images/fnaf2/toy_chica.png",
      "video": "/static/videos/toy_chica.mp4", # RUTA MP4
      "juego": "FNAF 2"
    },
    {
      "id": 9,
      "nombre": "Mangle",
      "descripcion": "Un animatrónico de zorro destrozado que se mueve por el conducto de ventilación. Mangle es uno de los personajes más icónicos de la saga, y su jumpscare es uno de los más aterradores.",
      "imagen": "/static/images/fnaf2/mangle.png",
      "video": "/static/videos/mangle.mp4", # RUTA MP4
      "juego": "FNAF 2"
    },
    {
      "id": 10,
      "nombre": "The Puppet (Marionette)",
      "descripcion": "Un animatrónico muy delgado y alto. The Puppet es uno de los personajes más importantes en la historia de la saga, y su jumpscare es uno de los más aterradores. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf2/puppet.png",
      "video": "/static/videos/the_puppet.mp4", # RUTA MP4
      "juego": "FNAF 2"
    },
    {
      "id": 11,
      "nombre": "Balloon Boy",
      "descripcion": "Un animatrónico de niño que se mueve por la ventilación. Balloon Boy no te ataca, pero te hace ruido para que otros animatrónicos te ataquen. Su jumpscare es muy molesto.",
      "imagen": "/static/images/fnaf2/balloon_boy.png",
      "video": "/static/videos/balloon_boy.mp4", # RUTA MP4
      "juego": "FNAF 2"
    },
    {
      "id": 12,
      "nombre": "Withered Freddy",
      "descripcion": "Una versión destrozada de Freddy. Withered Freddy es mucho más agresivo y te atacará si no lo vigilas. Es uno de los animatrónicos más viejos de la saga. Su jumpscare es uno de los más aterradores.",
      "imagen": "/static/images/fnaf2/withered_freddy.png",
      "video": "/static/videos/withered_freddy.mp4", # RUTA MP4
      "juego": "FNAF 2"
    },
    {
      "id": 13,
      "nombre": "Withered Bonnie",
      "descripcion": "Una versión destrozada de Bonnie. Withered Bonnie es uno de los animatrónicos más aterradores de la saga, y su jumpscare es uno de los más violentos. Su jumpscare es muy rápido y agresivo.",
      "imagen": "/static/images/fnaf2/withered_bonnie.png",
      "video": "/static/videos/withered_bonnie.mp4", # RUTA MP4
      "juego": "FNAF 2"
    },
    {
      "id": 14,
      "nombre": "Withered Chica",
      "descripcion": "Una versión destrozada de Chica. Withered Chica es mucho más agresiva y te atacará si no la vigilas. Es una de las animatrónicas más aterradoras de la saga. Su jumpscare es muy rápido y aterrador.",
      "imagen": "/static/images/fnaf2/withered_chica.png",
      "video": "/static/videos/withered_chica.mp4", # RUTA MP4
      "juego": "FNAF 2"
    },
    {
      "id": 15,
      "nombre": "Withered Foxy",
      "descripcion": "Una versión destrozada de Foxy. Withered Foxy es mucho más rápido y agresivo que Foxy. Es uno de los animatrónicos más aterradores de la saga. Su jumpscare es muy rápido y aterrador.",
      "imagen": "/static/images/fnaf2/withered_foxy.png",
      "video": "/static/videos/withered_foxy.mp4", # RUTA MP4
      "juego": "FNAF 2"
    },
    {
      "id": 16,
      "nombre": "Springtrap",
      "descripcion": "El animatrónico principal del tercer juego. Springtrap es un animatrónico de conejo que se mueve por la pizzería. Es uno de los animatrónicos más aterradores de la saga. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf3/pringtrap.png",
      "video": "/static/videos/springtrap.mp4", # RUTA MP4
      "juego": "FNAF 3"
    },
    {
      "id": 17,
      "nombre": "Phantom Freddy",
      "descripcion": "Una versión fantasma de Freddy. Phantom Freddy es uno de los animatrónicos fantasma de la saga. Su jumpscare es muy rápido y aterrador. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf3/phantom_freddy.png",
      "video": "/static/videos/phantom_freddy.mp4", # RUTA MP4
      "juego": "FNAF 3"
    },
    {
      "id": 18,
      "nombre": "Phantom Foxy",
      "descripcion": "Una versión fantasma de Foxy. Phantom Foxy es uno de los animatrónicos fantasma de la saga. Su jumpscare es muy rápido y aterrador. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf3/phantom_foxy.png",
      "video": "/static/videos/phantom_foxy.mp4", # RUTA MP4
      "juego": "FNAF 3"
    },
    {
      "id": 19,
      "nombre": "Phantom Chica",
      "descripcion": "Una versión fantasma de Chica. Phantom Chica es uno de los animatrónicos fantasma de la saga. Su jumpscare es muy rápido y aterrador. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf3/phantom_chica.png",
      "video": "/static/videos/phantom_chica.mp4", # RUTA MP4
      "juego": "FNAF 3"
    },
    {
      "id": 20,
      "nombre": "Phantom Mangle",
      "descripcion": "Una versión fantasma de Mangle. Phantom Mangle es uno de los animatrónicos fantasma de la saga. Su jumpscare es muy rápido y aterrador. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf3/phantom_mangle.png",
      "video": "/static/videos/phantom_mangle.mp4", # RUTA MP4
      "juego": "FNAF 3"
    },
    {
      "id": 21,
      "nombre": "Nightmare Freddy",
      "descripcion": "Una versión de pesadilla de Freddy. Nightmare Freddy es mucho más agresivo y te atacará si no lo vigilas. Es uno de los animatrónicos más aterradores de la saga. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf4/nightmare_freddy.png",
      "video": "/static/videos/nightmare_freddy.mp4", # RUTA MP4
      "juego": "FNAF 4"
    },
    {
      "id": 22,
      "nombre": "Nightmare Bonnie",
      "descripcion": "Una versión de pesadilla de Bonnie. Nightmare Bonnie es mucho más agresivo y te atacará si no lo vigilas. Es uno de los animatrónicos más aterradores de la saga. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf4/nightmare_bonnie.png",
      "video": "/static/videos/nightmare_bonnie.mp4", # RUTA MP4
      "juego": "FNAF 4"
    },
    {
      "id": 23,
      "nombre": "Nightmare Chica",
      "descripcion": "Una versión de pesadilla de Chica. Nightmare Chica es mucho más agresiva y te atacará si no la vigilas. Es una de las animatrónicas más aterradoras de la saga. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf4/nightmare_chica.png",
      "video": "/static/videos/nightmare_chica.mp4", # RUTA MP4
      "juego": "FNAF 4"
    },
    {
      "id": 24,
      "nombre": "Nightmare Foxy",
      "descripcion": "Una versión de pesadilla de Foxy. Nightmare Foxy es mucho más rápido y agresivo que Foxy. Es uno de los animatrónicos más aterradores de la saga. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf4/nightmare_foxy.png",
      "video": "/static/videos/nightmare_foxy.mp4", # RUTA MP4
      "juego": "FNAF 4"
    },
    {
      "id": 25,
      "nombre": "Nightmare Fredbear",
      "descripcion": "Una versión de pesadilla de Fredbear. Nightmare Fredbear es uno de los animatrónicos más aterradores de la saga. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf4/nightmare_fredbear.png",
      "video": "/static/videos/nightmare_fredbear.mp4", # RUTA MP4
      "juego": "FNAF 4"
    },
    {
      "id": 26,
      "nombre": "Nightmare (The Shade)",
      "descripcion": "La versión de pesadilla de Golden Freddy. Nightmare es el animatrónico más aterrador de la saga. Es uno de los animatrónicos más aterradores de la saga. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf4/nightmare.png",
      "video": "/static/videos/nightmare_the_shade.mp4", # RUTA MP4
      "juego": "FNAF 4"
    },
    {
      "id": 27,
      "nombre": "Plushtrap",
      "descripcion": "Una versión de peluche de Springtrap. Plushtrap es un animatrónico muy pequeño y rápido. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnaf4/plushtrap.png",
      "video": "/static/videos/plushtrap.mp4", # RUTA MP4
      "juego": "FNAF 4"
    },
    {
      "id": 28,
      "nombre": "Circus Baby",
      "descripcion": "La animatrónica principal de Sister Location. Circus Baby es una animatrónica de payaso. Su jumpscare es muy rápido y aterrador. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnafsl/circus_baby.png",
      "video": "/static/videos/circus_baby.mp4", # RUTA MP4
      "juego": "Sister Location"
    },
    {
      "id": 29,
      "nombre": "Funtime Freddy",
      "descripcion": "Un animatrónico de Freddy. Funtime Freddy es mucho más agresivo y te atacará si no lo vigilas. Es uno de los animatrónicos más aterradores de la saga. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnafsl/funtime_freddy.png",
      "video": "/static/videos/funtime_freddy.mp4", # RUTA MP4
      "juego": "Sister Location"
    },
    {
      "id": 30,
      "nombre": "Funtime Foxy",
      "descripcion": "Un animatrónico de zorro. Funtime Foxy es mucho más rápido y agresivo que Foxy. Es uno de los animatrónicos más aterradores de la saga. Su jumpscare es muy rápido.",
      "imagen": "/static/images/fnafsl/funtime_foxy.png",
      "video": "/static/videos/funtime_foxy.mp4", # RUTA MP4
      "juego": "Sister Location"
    }
  ],
  "mordida_del_86": {
    "titulo": "La Mordida del '87",
    "historia": "La 'Mordida del '87' es un evento trágico en la historia de 'Five Nights at Freddy's'. Se cree que un animatrónico, posiblemente Foxy o Mangle, atacó a un niño, dejándolo gravemente herido. Este incidente es la razón por la que el restaurante cerró.",
    "imagen": "/static/images/bite_of_87.jpg",
    "video_explicativo": "/static/videos/mordida_del_87_explicacion.mp4" # RUTA MP4
  }
}

@app.route('/')
def inicio():
    return render_template('index.html', db=db)

# ELIMINADO: La parte que iniciaba el servidor local (app.run(debug=True))
# Render usa Gunicorn para iniciar la aplicación, por lo que estas líneas no son necesarias
# en el servidor.