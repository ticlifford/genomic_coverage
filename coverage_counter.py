import csv
import json
from operator import itemgetter
import timeit

# the dictionary I'm tallying coverage in
coverage_dict = {}


def read_reads(coverage_dict):
    """read through reads.csv and tally coverage to a dictionary"""

    with open('reads.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        print('starting csv read and dictionary creation')
        for row in readCSV:
            iterative = int(row[0])
            count = int(row[1])

            while count:
                if iterative in coverage_dict:
                    coverage_dict[iterative] += 1
                else:
                    coverage_dict[iterative] = 1

                count = count - 1
                iterative = iterative + 1

# the list I'm sorting into
coverage_list = []


def ordered_list(coverage_dict):
    """
    create an ordered list of values from the coverage data
    this is necessary to perform a binary search, but not a linear search
    """

    print('creating list from dictionary')
    for key, value in coverage_dict.items():
        temp = [key, value]
        coverage_list.append(temp)

    # sort the list by the first value
    print('sorting the list')
    sorted_list = sorted(coverage_list, key=itemgetter(0))
    return sorted_list


def bin_search(item_list, target):
    """
    the binary search function
    binary uses O(log n) versus linear's O(n)
    (this is still slower than the dictionary search)
    """

    first = 0
    last = len(item_list)-1

    while first <= last:
        mid = (first + last)//2

        if int(item_list[mid][0]) == target:
            return item_list[mid][1]

        elif target < int(item_list[mid][0]):
            last = mid - 1

        else:
            first = mid + 1
    return False

def temp_loci():
    """this creates a temporary list of the locations i'm searching for"""
    temp_loci = []

    with open('loci.csv') as csvfile:
        lociCSV = csv.reader(csvfile, delimiter=',')
        next(lociCSV)

        for row in lociCSV:
            temp_loci.append(row)
        return temp_loci

def loci_bin(temp_loci):
    """
    loads the loci.csv, runs the binary search function
    saves a new loci.csv with coverage values
    """

    with open('new_loci.csv', 'w') as f:
        csvWriter = csv.writer(f, delimiter=',')
        for row in temp_loci:
            csvWriter.writerow([row[0], (bin_search(sorted_list, int(row[0])))])


def dict_search(coverage_dict,temp_loci):
    """
    a dictionary search to see if its faster than binary
    speed is amortized O(1)
    """

    with open('processed_loci.csv', 'w', newline='') as f:
        csvWriter = csv.writer(f, delimiter=',')
        csvWriter.writerow(['position', 'coverage'])
        for row in temp_loci:
            try:
                coverageVal = coverage_dict[int(row[0])]
            except:
                coverageVal = 0
            csvWriter.writerow([int(row[0]), coverageVal])


def wrapper(func, *args, **kwargs):
    """this is a wrapper for using the timeit function"""
    def wrapped():
        return func(*args, **kwargs)
    return wrapped



if __name__ == "__main__":
    """ I run my functions here"""
    try:
        read_reads(coverage_dict)
        sorted_list = ordered_list(coverage_dict)
    except:
        print('something went wrong reading reads and sorting')
    # I have two search methods here, the binary is faster

    try:
        temp_loci = temp_loci()
    except:
        print('creation of temp_loci failed')

    try:
        wrapped = wrapper(loci_bin, temp_loci)
        print('binary search time:', timeit.timeit(wrapped, number=10)/10)
    except:
        print('something went wrong with the binary search')
    
    try:
        wrapped = wrapper(dict_search, coverage_dict, temp_loci)
        print('dictionary search time:', timeit.timeit(wrapped, number=10)/10)
    except:
        print('something went wrong with the dictionary search')