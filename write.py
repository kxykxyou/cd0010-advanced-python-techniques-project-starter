"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
import datetime


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    # Write the results to a CSV file, following the specification in the instructions.
    with open(filename, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)
        for approach in results:
            row = (
                approach.time_str,
                approach.distance, approach.velocity,
                approach.neo.designation, approach.neo.name, approach.neo.diameter,
                approach.neo.hazardous
            )
            writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # Write the results to a JSON file, following the specification in the instructions.
    approaches = []
    fieldnames_approach = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
    )
    fieldnames_neo = (
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    for approach in results:
        approach_json_format = {}
        row_json_approach = (
            approach.time_str,
            approach.distance, approach.velocity,
        )
        row_json_neo = (
            approach.neo.designation, approach.neo.name, approach.neo.diameter,
            approach.neo.hazardous
        )
        for field, value in zip(fieldnames_approach, row_json_approach):
            approach_json_format[field] = value
        approach_json_format['neo'] = {}
        for field, value in zip(fieldnames_neo, row_json_neo):
            approach_json_format['neo'][field] = value
        approaches.append(approach_json_format)
    with open(filename, 'w') as outfile:
        json.dump(approaches, outfile)
