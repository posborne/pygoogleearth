def point_dict_from_terrain_point(terrain_point):
    """Return a dict from an IPointOnTerrainGE object"""
    return {
        'lat': terrain_point.Latitude,
        'lon': terrain_point.Longitude,
        'alt': terrain_point.Altitude,
        'projected_onto_glob': terrain_point.ProjectedOntoGlobe,
        'zero_elevation_exaggeration': terrain_point.ZeroElevationExageration,
    }
    
