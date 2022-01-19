import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "venv/eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

lons, lats, mags, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mag = eq_dict["properties"]["mag"]
    title = eq_dict["properties"]["title"]
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)
    hover_texts.append(title)

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": hover_texts,
    "marker": {
        "size": [3*mag for mag in mags],
        "color": mags,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"},
    }
}]
my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")