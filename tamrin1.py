import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file("D:\Term-8\mabahes\drawing asia/ne_110m_admin_0_countries.shp")  

asia = world[world['CONTINENT'] == 'Asia']

iran = asia[asia['NAME'] == 'Iran']

fig, ax = plt.subplots(figsize=(10, 6))
asia.plot(ax=ax, color="lightgray", edgecolor="black")
iran.plot(ax=ax, color="red", edgecolor="black")
ax.set_title("Map of Asia (Iran Highlighted)", fontsize=14)
plt.axis("off")
plt.show()
