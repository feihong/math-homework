import matplotlib.pyplot as plt
import sympy
import shapely
from shapely.geometry import Polygon, Point
import geopandas

point_count = 1_000_000

t = sympy.Triangle(sss=(10,10,10))
verts = [Point(p.x, p.y) for p in t.vertices] # triangle vertices
p = Polygon(verts + [verts[0]])
xs, ys = p.exterior.xy
f, ax = plt.subplots()
ax.plot(xs, ys)

o = Point(t.incenter.x, t.incenter.y) # center of triangle
series = geopandas.GeoSeries([o])
series.plot(ax=ax, color='purple')

sample_points = lambda p: geopandas.GeoSeries([p]).sample_points(point_count)

series = sample_points(p)
series.plot(ax=ax, color='red', markersize=1)

successes = 0

for i, p in enumerate(series[0].geoms, 1):
  do = shapely.distance(o, p)
  if all(do < shapely.distance(v, p) for v in verts):
    successes += 1

# plt.show()

print(f'Total={i}, successes={successes}, rate={successes/i}')
