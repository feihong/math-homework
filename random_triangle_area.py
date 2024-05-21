import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
import geopandas

point_count = 10_000
f, ax = plt.subplots()

x = Point(0,12)
y = Point(0,0)
z = Point(6,0)
t = Polygon([x, y, z, x]) # triangle xyz
xs, ys = t.exterior.xy
ax.plot(xs, ys)

sample_points = lambda p: geopandas.GeoSeries([p]).sample_points(point_count)

series = sample_points(t)
series.plot(ax=ax, color='red', markersize=1)

successes = 0

for i, d in enumerate(series[0].geoms, 1):
  xyd = Polygon([x, y, d, x])
  if xyd.area <= 24:
    successes += 1

print(f'Total={i}, successes={successes}, rate={successes/i}')

plt.show()
