## Agricultural information extracter
# Updated as of 9/24/26:

# description:
    # The software consists of two primary modules:
        # `my_utils.py`: COntains data-extraction functions built with safe file operations and type handling.
        #`print_fires.py`: Program that uses parameter flags to locate and print relevant emission metrics using my_utils.py.
    # Updates 9/24/26:
    # - **`my_utils.py`**: Added helper functions `get_mean()`, `get_median()`, and `get_std_dev()` to compute basic summary statistics on numeric arrays with proper exception handling (`ValueError`, `TypeError`).
        # - **`test_my_utils.py`**: Implemented unit tests using `unittest` covering positive cases (with `random` data generation) and negative/error edge cases.
       # **`print_fires.py`**: Added an optional `--op` argument (`mean`, `median`, `std_dev`) via `argparse` to run statistical operations on extracted columns.
        # **`test_print_fires.sh`**: Added functional tests using `ssshtest` along with a minimal sample dataset (`test_data.csv`) to verify program output and exit codes.
# Usage:
    #imput data is expected to be a csv file
    # required parameters are: --file_name, --country, --country_column, --fires_column

    #Example:
        python3 print_fires.py --file_name test_data.csv --country "United States of America" --country_column 0 --fires_column 3 --op mean

    # run.sh: automated shell script to demonstrate working execution along with expected error handling (e.g., missing arguments or invalid file paths)
     # runing unit tests: python3 test_my_utils.py
     # functional tests: test_print_fires.sh
     
# Installation and Setup:
    # Dependencies are managed using conda

    #Setup:
    # recreate environment
    1. mamba env create -f environment.yml
    
    # activate environment 
    2. conda activate swe4s

    