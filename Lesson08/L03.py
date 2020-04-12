class OwnError(Exception):
    pass


number_list = []
n = None
while n != 'stop':
    try:
        n = input('Enter the number - ').lower()
        if n.isdigit() is False:
            raise OwnError('Not a number!')
    except OwnError as err:
        print(err)
    else:
        number_list.append(int(n))

print(number_list)
