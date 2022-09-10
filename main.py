# https://stackoverflow.com/questions/41585078/how-do-i-read-and-write-csv-files-with-python

import csv
import Truck
from Package import Package
from PackageHashMap import PackageHashMap

# Calculate the distance between two addresses
def calculate_distance_between_addresses(filename, start, end):
    with open(filename) as distance_list:
        distance_data = csv.DictReader(distance_list, delimiter=",")
        for distance in distance_data:
            if start == distance['']:
                print(distance[end])


# Loads the package data
def load_package_data(filename):
    with open(filename) as package_list:
        package_data = csv.reader(package_list, delimiter=",")
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_deadline = package[5]
            package_weight = package[6]

            package = Package(package_id, package_address, package_city, package_state, package_zipcode,
                              package_deadline, package_weight)

            package_hash_map.insert(package_id, package)


# Creates an instance of the hash table.
package_hash_map = PackageHashMap()

# Loads package data into the hash table from the WGUPS Package File by calling the load_package_data() function.
load_package_data("WGUPS_Package_File.csv")

# Fetch data from hash table
# for i in range(len(package_hash_map.table)):
#    print("Key: {} and Package: {}".format(i + 1, package_hash_map.search(i + 1)))

calculate_distance_between_addresses("WGUPS_Distance_Table.csv", "1060 Dalton Ave S (84104)", "Western Governors University 4001 South 700 East, Salt Lake City, UT 84107")