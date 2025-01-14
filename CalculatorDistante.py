from math import radians, sin, cos, sqrt, atan2
from typing import Dict, List

stations_with_coords = {
    "Centru": [46.564, 26.912],
    "Mall": [46.580, 26.915],
    "Autogara": [46.571, 26.920],
    "Cartier Nord": [46.578, 26.898],
    "Cartier Sud": [46.550, 26.912]
}

def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def calculate_distances(coords: Dict[str, List[float]]) -> Dict[str, Dict[str, float]]:
    distances = {}
    locations = list(coords.keys()) 
    for i, loc1 in enumerate(locations):
        for loc2 in locations[i + 1:]:
            lat1, lon1 = coords[loc1]
            lat2, lon2 = coords[loc2]
            distance = haversine(lat1, lon1, lat2, lon2)
            if loc1 not in distances:
                distances[loc1] = {}
            if loc2 not in distances:
                distances[loc2] = {}
            distances[loc1][loc2] = distance
            distances[loc2][loc1] = distance
    return distances

def main():
    distances = calculate_distances(stations_with_coords)
    for loc1, others in distances.items():
        for loc2, dist in others.items():
            print(f"graph.add_edge(\"{loc1}\", \"{loc2}\", {dist:.2f})")

if __name__ == "__main__":
    main()

