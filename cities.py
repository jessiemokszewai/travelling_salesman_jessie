import csv
import math
import random
import matplotlib.pyplot as plt
import pyfiglet


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

     Args:
         file_name (text file): File name to read in

     Return:
         List : Contains a list of tuples in the following format of eg. [(state, city, latitude, longitude), ...]
    """

    # Read in text file
    print('Reading in ' + file_name + '...')
    with open(file_name, 'r') as f:
        raw = csv.reader(f, delimiter='\t')
        # Mapping data into list of 4-tuples
        data_list = [tuple([row[0], row[1], float(row[2]), float(row[3])]) for row in raw]
    return data_list


def print_cities(road_map):
    """
    Prints a list of cities, along with their locations.

    Args:
        road_map (List): List of tuples each with city names and their attributes

    Return:
        List: Prints a list of cities, along with their locations. Print only one or two digits after the decimal point.
    """
    print('State City Latitude Longitude')
    for city in road_map:
        print(' '.join([city[0],
                        city[1],
                        str(round(city[2], 2)),
                        str(round(city[3], 2))
                        ]))
    print('\n')


def compute_distance(x1, y1, x2, y2):
    """
    Method to calculate 2d distance

    Args:
        x1 (Float): Longitude of city 1
        y1 (Float): Longitude of city 1
        x2 (Float): Longitude of city 2
        y2 (Float): Longitude of city 2

    Return:
        Float: The distance between the two cities
    """
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def compute_total_distance(road_map):
    d = compute_city_distance(road_map)
    return sum(d)


def compute_city_distance(road_map):
    """
    Method to compute the distance between each of the cities and return as a list.
    Args:
        road_map (List): List of tuples each with city names and their attributes
    Return:
        List: Distances of floats between each of the cities in the road map
    """
    # Initialise list variable and previous_city variable
    distance_list = []
    prev_city = ['', '', 0.0, 0.0]
    for city in road_map:
        # calculate the distance between each cities and append into the list above
        distance_list.append(compute_distance(city[3], city[2], prev_city[3], prev_city[2]))
        prev_city = city
    # Removing first element as first element is variable prev_city with empty values
    distance_list.pop(0)
    # Calculating distance from the last city back to the starting city
    first_elem, last_elem = road_map[0], road_map[-1]
    distance_list.append(compute_distance(last_elem[2], last_elem[3], first_elem[2], first_elem[3]))
    return distance_list


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple

        (new_road_map, new_total_distance)

    Args:
        road_map (List): List of tuples each with city names and their attributes
        index1 (Int): Index in the list to swap with index2
        index2 (Int): Index in the list to sawp with index1

    Returns:
        Tuple: List of tuples each with city names and their attributes after the index change,
        and a total distance
    """
    road_map[index1], road_map[index2] = road_map[index2], road_map[index1]
    return tuple([road_map, compute_total_distance(road_map)])


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map.
    """
    return road_map[-1:] + road_map[:-1]


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`,
    try `10000` swaps/shifts, and each time keep the best cycle found so far.
    After `10000` swaps/shifts, return the best cycle found so far.

    Args:
        road_map (List): List of tuples each with city names and their attributes

    Return:
        List: List of tuples each with city names and their attributes after optimising routes
    """
    n = 0
    max_len = len(road_map) - 1
    total_distance = compute_total_distance(road_map)
    while n < 10000:

        # Shift road map
        shifted_road_map = shift_cities(road_map)

        # Initiate index variables for while statement
        rand_index1 = 0
        rand_index2 = 0

        # To avoid situation where index1 = index2
        while rand_index1 == rand_index2:
            rand_index1 = random.randint(0, max_len)
            rand_index2 = random.randint(0, max_len)

        # Swap cities randomly
        road_map_dist_tup = swap_cities(shifted_road_map, rand_index1, rand_index2)

        # If distance after swapping is less than original, replace original route
        if road_map_dist_tup[1] < total_distance:
            total_distance = road_map_dist_tup[1]
            road_map = road_map_dist_tup[0]

        n += 1
    return road_map


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.

    Args:
        road_map (List): List of tuples each with city names and their attributes
    """
    # Returning a list of distances
    dist_list = compute_city_distance(road_map)

    # Combining list of distances and the road map and map it into a printable format
    # eg. 1) city_1 (2.1) ->  2) city_2 (2.44)
    city_dist = [str(n) + ') ' + city[0] + ' (' + str(round(distance, 2)) + ') -> '
                 for city, distance, n in zip(road_map, dist_list, range(1, len(road_map) + 1))]

    print('Road Map After Optimising (City and cost between each connection)')
    print(' '.join(city_dist), '1) ', road_map[0][0])
    print('\n')


def visualise(road_map, total_distance):
    """
    Plots the road map visualising the route for travelling between the cities.
    City highlighted in dark blue indicating the first stop and
    dark purple indicating the last stop

    Args:
        road_map (List): List of tuples each with city names and their attributes
        total_distance (Float): Current total cost of the route
    """
    # Appending Longitude and Latitude for each city in the road map
    x = []
    y = []
    for i in road_map:
        x.append(i[3])
        y.append(i[2])

    # Connecting the last city back to the first city
    x.append(road_map[0][3])
    y.append(road_map[0][2])

    plt.figure(figsize=(13, 7))
    plt.plot(x, y, '-ok', alpha=0.4, color='lightskyblue')
    plt.xlabel(('Longitude'))
    plt.ylabel(('Latitude'))
    plt.title('Travelling Salesman Optimised Road-map with Total Distance of {}'.format(total_distance))

    n = 1
    for i in road_map:
        city_label = ''.join([str(n), '). ', i[0]])
        # Adjusting different font properties for start and end city
        if i == road_map[0]:
            plt.text(i[3], i[2], city_label, fontdict={'color': 'darkblue',
                                                       'size': 8, 'alpha': 0.8,
                                                       'weight': 'bold'})
        elif i == road_map[-1]:
            plt.text(i[3], i[2], city_label, fontdict={'color': 'darkviolet',
                                                       'size': 8, 'alpha': 0.8,
                                                       'weight': 'bold'})
        else:
            plt.text(i[3], i[2], city_label, fontdict={'color': 'indigo',
                                                       'size': 8,
                                                       'alpha': 0.7})
        n += 1
    plt.show()


def main():
    """
    Run the program
    """
    # Initialise
    print(pyfiglet.figlet_format('FDM TSP PROJECT', font="slant"))
    iterations_n = 10000
    file_path = 'city-data.txt'

    # Read in text file
    road_map = read_cities(file_path)
    # Print original road map
    print_cities(road_map)

    # Compute initial distance
    total_distance = compute_total_distance(road_map)
    # Prints initial distance
    print('Initial distance is {}\n'.format(str(round(total_distance, 2))))

    # Run find best cycle
    print('Proceeding with {} iterations.'.format(iterations_n))
    print('Optimising best cycle...')
    new_road_map = find_best_cycle(road_map)
    new_distance = compute_total_distance(new_road_map)

    # Prints final
    print_map(new_road_map)
    print('Final distance is {}'.format(str(round(new_distance, 2))))

    # Visualise final road map
    visualise(new_road_map, str(round(new_distance, 2)))


if __name__ == "__main__":
    main()