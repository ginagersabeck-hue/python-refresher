"""Script to extract and print emission values using my_utils.
"""

import argparse
import my_utils


def main():
    parser = argparse.ArgumentParser(
        description='Extract and print emission values for a specified country.',
        prog='print_fires'
    )
    parser.add_argument(
        '--country',
        type=str,
        required=True,
        help='Country name to query'
    )
    parser.add_argument(
        '--country_column',
        type=int,
        required=True,
        help='Zero-indexed column containing country names'
    )
    parser.add_argument(
        '--fires_column',
        type=int,
        required=True,
        help='Zero-indexed column containing fire emission values'
    )
    parser.add_argument(
        '--file_name',
        type=str,
        required=True,
        help='Path to the CSV dataset file'
    )

    args = parser.parse_args()

    emissions = my_utils.get_column(
        file_name=args.file_name,
        query_column=args.country_column,
        query_value=args.country,
        result_column=args.fires_column
    )

    for value in emissions:
        print(value)


if __name__ == '__main__':
    main()