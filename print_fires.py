import argparse
import sys
import my_utils


def main():
    parser = argparse.ArgumentParser(
        description="Process agricultural fire emission data from CSV."
    )

    # Required arguments from Assignment 2 & 3
    parser.add_argument(
        '--file_name',
        type=str,
        required=True,
        help="Path to CSV dataset"
    )
    parser.add_argument(
        '--country',
        type=str,
        required=True,
        help="Target country name"
    )
    parser.add_argument(
        '--country_column',
        type=int,
        required=True,
        help="Column index for country"
    )
    parser.add_argument(
        '--fires_column',
        type=int,
        required=True,
        help="Column index for fire emissions"
    )

    # Task 3: Optional argument for statistical operation
    parser.add_argument(
        '--op',
        type=str,
        choices=['mean', 'median', 'std_dev'],
        required=False,
        default=None,
        help="Optional operation: mean, median, or std_dev"
    )

    args = parser.parse_args()

    # --- DEFINE 'fires' HERE ---
    fires = my_utils.get_column(
        args.file_name,
        args.country_column,
        args.country,
        args.fires_column
    )

    if not fires:
        print("Warning: No matching data found or array is empty.",
              file=sys.stderr)
        sys.exit(1)

    # Task 3 operation handling
    if args.op == 'mean':
        print(my_utils.get_mean(fires))
    elif args.op == 'median':
        print(my_utils.get_median(fires))
    elif args.op == 'std_dev':
        print(my_utils.get_std_dev(fires))
    else:
        for val in fires:
            print(val)


if __name__ == '__main__':
    main()
