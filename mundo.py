import pyfiglet
import pygal
import sys
ascii_banner = pyfiglet.figlet_format("THE WORLD")
print(ascii_banner)
print("CREADO POR TRIPLE YEI")

n = len(sys.argv)
print("name " , sys.argv[0])
print("Argumentos pasados", end = " ")
title = sys.argv[1]
data1 = sys.argv[2]
data2 = sys.argv[3]
data3 = sys.argv[4]


worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = title
worldmap_chart.add(data1,[data1])
worldmap_chart.add(data2,[data2])
worldmap_chart.add(data3,[data3])
worldmap_chart.render_to_file('mundo.svg')


