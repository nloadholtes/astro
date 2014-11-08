

def load_orbital_parameters(filename):
    elements = {}
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        reading = False
        for line in lines:
            chunks = line.split(' ')
            if chunks[0] == '$$SOE':
                print("Start seen")
                reading = True
                continue
            if chunks[0] == '$$EOE':
                print('End seen')
                reading = False
                break
            if reading:
                print('Going to try and read: %s' % chunks)
                continue
    return elements


if __name__ == '__main__':
    elements = load_orbital_parameters('ephemeris/triton_horizons.cgi.txt')
    print(elements)
