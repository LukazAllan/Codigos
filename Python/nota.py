nta = ['C0', ['C#0', 'Db0'], 'D0', ['D#0', 'Eb0'], 'E0', 'F0', ['F#0', 'Gb0'], 'G0', ['G#0', 'Ab0'], 'A0', ['A#0', 'Bb0'], 'B0', 'C1', ['C#1', 'Db1'], 'D2', ['D#1', 'Eb1'], 'E1', 'F1', ['F#1', 'Gb1'], 'G1', ['G#1', 'Ab1'], 'A1', ['A#1', 'Bb1'], 'B1', 'C2', ['C#2', 'Db2'], 'D2', ['D#2', 'Eb2'], 'E2', 'F2', ['F#2', 'Gb2'], 'G2', ['G#2', 'Ab2'], 'A2', ['A#2', 'Bb2'], 'B2', 'C3', ['C#3', 'Db3'], 'D3', ['D#3', 'Eb3'], 'E3', 'F3', ['F#3', 'Gb3'], 'G3', ['G#3', 'Ab3'], 'A3', ['A#3', 'Bb3'], 'B3', 'C4']
for c in range(12):
    print(f'{1+c}.', end=' ')
    if type(nta[c]) != list:
        print(f'{nta[c]}→', end='')
        if type(nta[c + 2]) == list:
            print(f'{nta[c+2][0]}→', end='')
        else:
            print(f'{nta[c+2]}→', end='')

        if type(nta[c + 4]) == list:
            print(f'{nta[c+4][0]}→', end='')
        else:
            print(f'{nta[c+4]}→', end='')

        if type(nta[c + 5]) == list:
            print(f'{nta[c+5][0]}→', end='')
        else:
            print(f'{nta[c+5]}→', end='')

        if type(nta[c + 7]) == list:
            print(f'{nta[c+7][0]}→', end='')
        else:
            print(f'{nta[c+7]}→', end='')

        if type(nta[c + 9]) == list:
            print(f'{nta[c+9][0]}→', end='')
        else:
            print(f'{nta[c+9]}→', end='')

        if type(nta[c + 11]) == list:
            print(f'{nta[c+11][0]}→', end='')
        else:
            print(f'{nta[c+11]}→', end='')

        if type(nta[c + 12]) == list:
            print(f'{nta[c+12][0]}\n')
        else:
            print(f'{nta[c+12]}\n')
    else:
        if c % 12 in (1, 3, 8, 10):
            print(f'{nta[c][1]}→', end='')
            if type(nta[c + 2]) == list:
                print(f'{nta[c+2][1]}→', end='')
            else:
                print(f'{nta[c+2]}→', end='')

            if type(nta[c + 4]) == list:
                print(f'{nta[c+4][1]}→', end='')
            else:
                print(f'{nta[c+4]}→', end='')

            if type(nta[c + 5]) == list:
                print(f'{nta[c+5][1]}→', end='')
            else:
                print(f'{nta[c+5]}→', end='')

            if type(nta[c + 7]) == list:
                print(f'{nta[c+7][1]}→', end='')
            else:
                print(f'{nta[c+7]}→', end='')

            if type(nta[c + 9]) == list:
                print(f'{nta[c+9][1]}→', end='')
            else:
                print(f'{nta[c+9]}→', end='')

            if type(nta[c + 11]) == list:
                print(f'{nta[c+11][1]}→', end='')
            else:
                print(f'{nta[c+11]}→', end='')

            if type(nta[c + 12]) == list:
                print(f'{nta[c+12][1]}\n')
            else:
                print(f'{nta[c+12]}\n')
        else:
            print(f'{nta[c][0]}→', end='')
            if type(nta[c + 2]) == list:
                print(f'{nta[c+2][0]}→', end='')
            else:
                print(f'{nta[c+2]}→', end='')

            if type(nta[c + 4]) == list:
                print(f'{nta[c+4][0]}→', end='')
            else:
                print(f'{nta[c+4]}→', end='')

            if type(nta[c + 5]) == list:
                print(f'{nta[c+5][0]}→', end='')
            else:
                print(f'{nta[c+5]}→', end='')

            if type(nta[c + 7]) == list:
                print(f'{nta[c+7][0]}→', end='')
            else:
                print(f'{nta[c+7]}→', end='')

            if type(nta[c + 9]) == list:
                print(f'{nta[c+9][0]}→', end='')
            else:
                print(f'{nta[c+9]}→', end='')

            if type(nta[c + 11]) == list:
                print(f'{nta[c+11][0]}→', end='')
            else:
                print(f'{nta[c+11]}→', end='')

            if type(nta[c + 12]) == list:
                print(f'{nta[c+12][0]}\n')
            else:
                print(f'{nta[c+12]}\n')
