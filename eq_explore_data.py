import json

filename = "venv/eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(f"magnitudes: {mags[:10]}")
print(f"longitudes: {lons[:10]}")
print(f"latitudes: {lats[:20]}")

readable_file = "venv/readable_eq_data.json"
with open(readable_file, "w") as f:
    json.dump(all_eq_data, f, indent=4)

