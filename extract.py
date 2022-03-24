"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    Name mapping with original feature names in 'neos.csv' file:
        designation: pdes
        name: name
        diameter: diameter
        hazardous: pha

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    NEO_collection = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            designation = row[3]
            name = row[4]
            diameter = float(row[15]) if row[15] else float('nan')
            hazardous = True if row[7] == 'Y' else False
            neo = NearEarthObject(designation=designation,
                                  name=name,
                                  diameter=diameter,
                                  hazardous=hazardous)
            NEO_collection.append(neo)
    return NEO_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    Name mapping with original feature names in 'cad.json' file:
    _designation: des 
    time: cd
    distance: dist
    velocity: v_rel

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    CAD_collection = []
    with open(cad_json_path) as infile:
        data = json.load(infile)['data']
        for sample in data:
            designation = sample[0]
            time = sample[3]
            distance = float(sample[4])
            velocity = float(sample[7])
            cad = CloseApproach(designation=designation,
                                time=time,
                                distance=distance,
                                velocity=velocity)
            CAD_collection.append(cad)
    return CAD_collection
