def cylinder():
    radius = float(input('Enter radius: '))
    length = float(input('Enter length: '))

    #ALGORITHM
    area = radius * radius * 3.141592
    volume = area * length

    print('Area of cylinder: ' + str(area))
    print('Volume of cylinder: ' + str(volume))

print('*** VOLUME OF THAT CYLINDER ***')
cylinder()