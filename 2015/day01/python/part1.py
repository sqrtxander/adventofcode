if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        directions = f.read()

    print(directions.count("(") - directions.count(")"))
