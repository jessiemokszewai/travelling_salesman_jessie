import pytest
from cities import *

def test_compute_total_distance():
    """
    Scenarios to test method compute_total_distance.
    """
    road_map1 = [("California", "Sacramento", 38.555605, -121.468926),
                ("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Michigan", "Lansing", 42.7335, -84.5467)]

    road_map2 = [("New York", "Albany", 42.659829, -73.781339),
                 ("Ohio", "Columbus", 39.962245, -83.000647),
                 ("New Jersey", "Trenton", 30.266667, -97.75)]

    road_map3 = [("Utah", "Salt Lake City", 40.7547, -111.892622),
                 ("Maryland", "Annapolis", 38.972945, -76.501157),
                 ("Colorado", "Denver", 39.7391667, -104.984167)]

    road_map4 = [("Maine", "Augusta", 32.36, -86.20),
                 ("New Jersey", "Trenton", 38.97, -76.50),
                 ("North Carolina", "Raleigh", 39.74, -104.98)]

    road_map5 = [("Ohio", "Columbus", 37.54, -77.47),
                 ("Texas", "Austin", 32.32, -90.21),
                 ("New York", "Albany", 39.04, -95.69)]

    assert compute_total_distance(road_map1) == pytest.approx(78.31, 0.01)
    assert compute_total_distance(road_map2) == pytest.approx(54.24, 0.01)
    assert compute_total_distance(road_map3) == pytest.approx(70.91, 0.01)
    assert compute_total_distance(road_map4) == pytest.approx(60.41, 0.01)
    assert compute_total_distance(road_map5) == pytest.approx(40.74, 0.01)


def test_swap_cities():
    """
    Scenarios to test method swap_cities.
    """
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    actual_road_map1 = swap_cities(road_map1, 2, 1)

    expected_road_map1 = ([("Kentucky", "Frankfort", 38.197274, -84.86311),
                           ("Minnesota", "Saint Paul", 44.95, -93.094),
                           ("Delaware", "Dover", 39.161921, -75.526755)],
                          38.53)

    road_map2 = [("New York", "Albany", 42.659829, -73.781339),
                 ("Ohio", "Columbus", 39.962245, -83.000647),
                 ("New Jersey", "Trenton", 30.266667, -97.75)]

    actual_road_map2 = swap_cities(road_map2, 0, 1)

    expected_road_map2 = ([("Ohio", "Columbus", 39.962245, -83.000647),
                          ("New York", "Albany", 42.659829, -73.781339),
                          ("New Jersey", "Trenton", 30.266667, -97.75)],
                          54.24)

    road_map3 = [("Utah", "Salt Lake City", 40.7547, -111.892622),
                 ("Maryland", "Annapolis", 38.972945, -76.501157),
                 ("Colorado", "Denver", 39.7391667, -104.984167)]

    actual_road_map3 = swap_cities(road_map3, 0, 2)

    expected_road_map3 = ([("Colorado", "Denver", 39.7391667, -104.984167),
                          ("Maryland", "Annapolis", 38.972945, -76.501157),
                          ("Utah", "Salt Lake City", 40.7547, -111.892622)],
                          70.91)

    road_map4 = [("Maine", "Augusta", 32.36, -86.20),
                 ("New Jersey", "Trenton", 38.97, -76.50),
                 ("North Carolina", "Raleigh", 39.74, -104.98)]

    actual_road_map4 = swap_cities(road_map4, 0, 1)

    expected_road_map4 = ([("New Jersey", "Trenton", 38.97, -76.50),
                          ("Maine", "Augusta", 32.36, -86.20),
                          ("North Carolina", "Raleigh", 39.74, -104.98)],
                          60.41)

    road_map5 = [("Ohio", "Columbus", 37.54, -77.47),
                 ("Texas", "Austin", 32.32, -90.21),
                 ("New York", "Albany", 39.04, -95.69)]

    actual_road_map5 = swap_cities(road_map5, 1, 2)

    expected_road_map5 = ([("Ohio", "Columbus", 37.54, -77.47),
                          ("New York", "Albany", 39.04, -95.69),
                          ("Texas", "Austin", 32.32, -90.21)],
                          40.74)

    assert actual_road_map1[0] == expected_road_map1[0]
    assert actual_road_map1[1] == pytest.approx(expected_road_map1[1], 0.01)

    assert actual_road_map2[0] == expected_road_map2[0]
    assert actual_road_map2[1] == pytest.approx(expected_road_map2[1], 0.01)

    assert actual_road_map3[0] == expected_road_map3[0]
    assert actual_road_map3[1] == pytest.approx(expected_road_map3[1], 0.01)

    assert actual_road_map4[0] == expected_road_map4[0]
    assert actual_road_map4[1] == pytest.approx(expected_road_map4[1], 0.01)

    assert actual_road_map5[0] == expected_road_map5[0]
    assert actual_road_map5[1] == pytest.approx(expected_road_map5[1], 0.01)


def test_shift_cities():
    """
    Scenarios to test method shift_cities.
    """
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    actual_road_map1 = shift_cities(road_map1)

    expected_road_map1 = [("Minnesota", "Saint Paul", 44.95, -93.094),
                         ("Kentucky", "Frankfort", 38.197274, -84.86311),
                         ("Delaware", "Dover", 39.161921, -75.526755)]

    road_map2 = [("New York", "Albany", 42.659829, -73.781339),
                 ("Ohio", "Columbus", 39.962245, -83.000647),
                 ("New Jersey", "Trenton", 30.266667, -97.75)]

    actual_road_map2 = shift_cities(road_map2)

    expected_road_map2 = [("New Jersey", "Trenton", 30.266667, -97.75),
                          ("New York", "Albany", 42.659829, -73.781339),
                          ("Ohio", "Columbus", 39.962245, -83.000647)]

    road_map3 = [("Utah", "Salt Lake City", 40.7547, -111.892622),
                 ("Maryland", "Annapolis", 38.972945, -76.501157),
                 ("Colorado", "Denver", 39.7391667, -104.984167)]

    actual_road_map3 = shift_cities(road_map3)

    expected_road_map3 = [("Colorado", "Denver", 39.7391667, -104.984167),
                          ("Utah", "Salt Lake City", 40.7547, -111.892622),
                          ("Maryland", "Annapolis", 38.972945, -76.501157)]

    road_map4 = [("Maine", "Augusta", 32.36, -86.20),
                 ("New Jersey", "Trenton", 38.97, -76.50),
                 ("North Carolina", "Raleigh", 39.74, -104.98)]

    actual_road_map4 = shift_cities(road_map4)

    expected_road_map4 = [("North Carolina", "Raleigh", 39.74, -104.98),
                          ("Maine", "Augusta", 32.36, -86.20),
                          ("New Jersey", "Trenton", 38.97, -76.50)]

    road_map5 = [("Ohio", "Columbus", 37.54, -77.47),
                 ("Texas", "Austin", 32.32, -90.21),
                 ("New York", "Albany", 39.04, -95.69)]

    actual_road_map5 = shift_cities(road_map5)

    expected_road_map5 = [("New York", "Albany", 39.04, -95.69),
                          ("Ohio", "Columbus", 37.54, -77.47),
                          ("Texas", "Austin", 32.32, -90.21)]

    assert actual_road_map1 == expected_road_map1
    assert actual_road_map2 == expected_road_map2
    assert actual_road_map3 == expected_road_map3
    assert actual_road_map4 == expected_road_map4
    assert actual_road_map5 == expected_road_map5


def test_compute_distance():
    """
    Scenarios to test method calc_distance.
    """
    city1 = (-121.47, 38.56)
    city2 = (-84.86, 38.20)

    city3 = (-73.78, 42.66)
    city4 = (-83.00, 39.96)

    city5 = (-111.89, 40.75)
    city6 = (-76.50, 38.97)

    city7 = (-86.20, 32.36)
    city8 = (-76.50, 38.97)

    city9 = (-77.46, 37.54)
    city10 = (-90.21, 32.32)

    assert compute_distance(city1[0], city1[1], city2[0], city2[1]) == pytest.approx(36.61, 0.01)
    assert compute_distance(city3[0], city3[1], city4[0], city4[1]) == pytest.approx(9.61, 0.01)
    assert compute_distance(city5[0], city5[1], city6[0], city6[1]) == pytest.approx(35.44, 0.01)
    assert compute_distance(city7[0], city7[1], city8[0], city8[1]) == pytest.approx(11.74, 0.01)
    assert compute_distance(city9[0], city9[1], city10[0], city10[1]) == pytest.approx(13.77, 0.01)


def test_compute_city_distance():
    """
    Scenarios to test method compute_city_distance.
    """
    road_map1 = [("California", "Sacramento", 38.555605, -121.468926),
                ("Kentucky", "Frankfort", 38.197274, -84.86311),
                ("Michigan", "Lansing", 42.7335, -84.5467)]

    actual_distance_list1 = compute_city_distance(road_map1)
    expected_distance_list1 = [36.61, 4.55, 37.16]

    road_map2 = [("New York", "Albany", 42.659829, -73.781339),
                 ("Ohio", "Columbus", 39.962245, -83.000647),
                 ("New Jersey", "Trenton", 30.266667, -97.75)]

    actual_distance_list2 = compute_city_distance(road_map2)
    expected_distance_list2 = [9.61, 17.65, 26.98]

    road_map3 = [("Utah", "Salt Lake City", 40.7547, -111.892622),
                 ("Maryland", "Annapolis", 38.972945, -76.501157),
                 ("Colorado", "Denver", 39.7391667, -104.984167)]

    actual_distance_list3 = compute_city_distance(road_map3)
    expected_distance_list3 = [35.44, 28.49, 6.98]

    road_map4 = [("Maine", "Augusta", 32.36, -86.20),
                 ("New Jersey", "Trenton", 38.97, -76.50),
                 ("North Carolina", "Raleigh", 39.74, -104.98)]

    actual_distance_list4 = compute_city_distance(road_map4)
    expected_distance_list4 = [11.74, 28.49, 20.18]

    road_map5 = [("Ohio", "Columbus", 37.54, -77.47),
                 ("Texas", "Austin", 32.32, -90.21),
                 ("New York", "Albany", 39.04, -95.69)]

    actual_distance_list5 = compute_city_distance(road_map5)
    expected_distance_list5 = [13.77, 8.67, 18.29]

    assert actual_distance_list1 == pytest.approx(expected_distance_list1, 0.1)
    assert actual_distance_list2 == pytest.approx(expected_distance_list2, 0.1)
    assert actual_distance_list3 == pytest.approx(expected_distance_list3, 0.1)
    assert actual_distance_list4 == pytest.approx(expected_distance_list4, 0.1)
    assert actual_distance_list5 == pytest.approx(expected_distance_list5, 0.1)
