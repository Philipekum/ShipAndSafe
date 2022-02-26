from Ship import Ship

if __name__ == '__main__':
    imo = '9408138'
    evergreen = Ship(imo)
    print(evergreen.expected_path())
