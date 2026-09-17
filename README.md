## Agricultural information extracter
# Updates as of 9/17/26:

# description:
    # The software consists of two primary modules:
        # `my_utils.py`: COntains data-extraction functions built with safe file operations and type handling.
        #`print_fires.py`: Program that uses parameter flags to locate and print relevant emission metrics using my_utils.py.

# Usage:
    #imput data is expected to be a csv file
    # required parameters are: --file_name, --country, --country_column, --fires_column

    #Example:
        python print_fires.py \
    --file_name Agrofood_co2_emission.csv \
    --country "United States of America" \
    --country_column 0 \
    --fires_column 3

    # run.sh: automated shell script to demonstrate working execution along with expected error handling (e.g., missing arguments or invalid file paths)

# Installation and Setup:
    # Dependencies are managed using conda

    #Setup:
    # recreate environment
    1. mamba env create -f environment.yml
    
    # activate environment 
    2. conda activate swe4s

    