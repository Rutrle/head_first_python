try:
    with open('myfile.txt') as fh:
        file_data = fh.read
    print(file_data)
except FileNotFoundError:
    print('The data file is missing')
except PermissionError:
    print('not allowed')
except Exception as err:
    print('Something elese occured', str(err))
