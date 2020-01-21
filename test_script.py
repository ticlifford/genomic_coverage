import csv


def test_loci():

    """
    I'm opening my edited loci.csv and comparing it
    to known correct values and returning errors
    """

    temp_loci = []
    print('starting dictionary search test')

    with open('processed_loci.csv') as csvfile:
        lociCSV = csv.reader(csvfile, delimiter=',')
        print('reading processed_loci.csv')

        for row in lociCSV:
            temp_loci.append(row)
        errors = 0

        with open('test_numbers.csv') as f:
            testCSV = csv.reader(f, delimiter=',')
            print('reading test_numbers.csv')
            for row in testCSV:
                print('checking this val:', row[0])
                for x in temp_loci:
                    if x[0] == row[0]:
                        if x[1] == row[1]:
                            print('value matches')
                        else:
                            print('error!')
                            errors = errors + 1

    print('number of errors:', errors)
    print('done')

test_loci()
