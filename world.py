import pygal

# Mapa del mundo, donde se ve España, Francia y Italia, al ejecutar se crea un mapa en svg
# Creado por TripleYei

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Spain France and Italy'
worldmap_chart.add('Spain',['es'])
worldmap_chart.add('France',['fr'])
worldmap_chart.add('Italy',['it'])
worldmap_chart.render_to_file('world_map.svg')