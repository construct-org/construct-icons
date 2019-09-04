# -*- coding: utf-8 -*-
import json


def main():

    # Read variables.scss
    with open('variables.scss', 'r') as f:
        lines = f.readlines()

    # Create charmap from variables.scss
    charmap = {}
    for line in lines:
        if not line.startswith('$icon-'):
            continue

        name, char = [p.strip(' ";') for p in line[6:-1].split(':')]
        char = char.replace('\\e', '\\ue')
        charmap[name] = char.decode('unicode-escape')

    # Write charmap.json
    with open('construct_charmap.json', 'w') as f:
        f.write(json.dumps(charmap, sort_keys=True, indent=4).encode('utf-8'))


if __name__ == '__main__':
    main()
