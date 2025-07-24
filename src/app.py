from flask import Flask, jsonify, request, render_template
import mysql.connector
import rasterio
import numpy as np
from pyproj import CRS, Transformer
from shapely.geometry import LineString, mapping
import json

app = Flask(__name__)

# ---- DATABASE CONNECTION ----
def get_db_connection():
    return mysql.connector.connect(
        host='mysql',
        user='myuser',
        password='mypassword',
        database='mydb'
    )

# ---- LOAD DEM AND PRECOMPUTE SLOPE/ASPECT ----
dataset = rasterio.open('dataset/copernicus.tif')
elevation_data = dataset.read(1).astype(np.float32)
transform = dataset.transform

nodata_value = dataset.nodata
if nodata_value is not None:
    elevation_data[elevation_data == nodata_value] = np.nan

# Coordinate transformations
lunar_geo_crs = CRS.from_proj4("+proj=longlat +a=1737400 +b=1737400 +no_defs")
projected_crs = CRS.from_wkt(dataset.crs.wkt)
geo_to_proj_transformer = Transformer.from_crs(lunar_geo_crs, projected_crs, always_xy=True)

def coords_to_pixel(lon, lat):
    x, y = geo_to_proj_transformer.transform(lon, lat)
    row, col = ~transform * (x, y)
    return int(row), int(col)

def calculate_slope_aspect(elevation, resolution):
    gy, gx = np.gradient(elevation, resolution[1], resolution[0])
    slope_rad = np.arctan(np.sqrt(gx**2 + gy**2))
    slope_deg = np.degrees(slope_rad)
    aspect_rad = np.arctan2(-gx, gy)
    aspect_deg = np.degrees(aspect_rad)
    aspect_deg = np.where(aspect_deg < 0, 360 + aspect_deg, aspect_deg)
    return slope_deg, aspect_deg

slope_data, aspect_data = calculate_slope_aspect(elevation_data, dataset.res)

@app.route('/')
def index():
    return render_template('index.html')

# ---- TERRAIN APIs ----
@app.route('/api/elevation', methods=['GET'])
def get_elevation():
    lon = request.args.get('lon', type=float)
    lat = request.args.get('lat', type=float)
    if lon is None or lat is None:
        return jsonify({"error": "Provide 'lon' and 'lat' parameters."}), 400
    try:
        row, col = coords_to_pixel(lon, lat)
        elev = elevation_data[row, col]
        if np.isnan(elev):
            return jsonify({"error": "No elevation data at location."}), 404
        return jsonify({
            "longitude": lon,
            "latitude": lat,
            "elevation_meters": float(elev)
        })
    except IndexError:
        return jsonify({"error": "Coordinates out of bounds."}), 400

@app.route('/api/slope', methods=['GET'])
def get_slope():
    lon = request.args.get('lon', type=float)
    lat = request.args.get('lat', type=float)
    if lon is None or lat is None:
        return jsonify({"error": "Provide 'lon' and 'lat' parameters."}), 400
    try:
        row, col = coords_to_pixel(lon, lat)
        slope = slope_data[row, col]
        if np.isnan(slope):
            return jsonify({"error": "No slope data at location."}), 404
        return jsonify({
            "longitude": lon,
            "latitude": lat,
            "slope_degrees": float(slope)
        })
    except IndexError:
        return jsonify({"error": "Coordinates out of bounds."}), 400

@app.route('/api/aspect', methods=['GET'])
def get_aspect():
    lon = request.args.get('lon', type=float)
    lat = request.args.get('lat', type=float)
    if lon is None or lat is None:
        return jsonify({"error": "Provide 'lon' and 'lat' parameters."}), 400
    try:
        row, col = coords_to_pixel(lon, lat)
        aspect = aspect_data[row, col]
        if np.isnan(aspect):
            return jsonify({"error": "No aspect data at location."}), 404
        return jsonify({
            "longitude": lon,
            "latitude": lat,
            "aspect_degrees": float(aspect)
        })
    except IndexError:
        return jsonify({"error": "Coordinates out of bounds."}), 400



# ---- SKI ROUTE GENERATOR ----
@app.route('/api/ski-routes', methods=['GET'])
def get_ski_routes():
    """
    Return beginner and pro ski routes based on slope ranges.
    """
    # Define slope thresholds
    beginner_mask = (slope_data >= 0) & (slope_data < 15)
    pro_mask = slope_data >= 30

    # Generate dummy centerlines for each mask (for simplicity)
    beginner_route = LineString([(col * transform.a + transform.c, row * transform.e + transform.f)
                                for row, col in zip(*np.where(beginner_mask))])
    pro_route = LineString([(col * transform.a + transform.c, row * transform.e + transform.f)
                            for row, col in zip(*np.where(pro_mask))])

    # Return as GeoJSON
    return jsonify({
        "beginner_route": mapping(beginner_route),
        "pro_route": mapping(pro_route)
    })



# ---- TERRAIN PROFILE API ----
@app.route('/api/terrain-profile', methods=['POST'])
def get_terrain_profile():
    """
    Return terrain profile (elevation, slope, aspect) along a path.
    """
    data = request.get_json()
    points = data.get('path', [])
    if not points:
        return jsonify({"error": "Provide 'path' as a list of {lon, lat}."}), 400

    profile = []
    for pt in points:
        lon, lat = pt.get('lon'), pt.get('lat')
        try:
            row, col = coords_to_pixel(lon, lat)
            elev = elevation_data[row, col]
            slope = slope_data[row, col]
            aspect = aspect_data[row, col]
            profile.append({
                "lon": lon,
                "lat": lat,
                "elevation_meters": float(elev),
                "slope_degrees": float(slope),
                "aspect_degrees": float(aspect)
            })
        except IndexError:
            profile.append({
                "lon": lon,
                "lat": lat,
                "error": "Coordinates out of bounds."
            })

    return jsonify(profile)



# ---- RUN FLASK ----
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
