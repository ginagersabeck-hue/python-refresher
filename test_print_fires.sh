#!/bin/bash

# Download ssshtest if not present and source it
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Define test file path
TEST_CSV="test_data.csv"

# ==========================================
# 1. DEFAULT BEHAVIOR (NO --op)
# ==========================================
run test_no_op python3 print_fires.py --file_name $TEST_CSV --country "United States of America" --country_column 0 --fires_column 3
assert_exit_code 0
assert_in_stdout "10"
assert_in_stdout "20"
assert_in_stdout "30"

# ==========================================
# 2. STATISTICAL OPERATIONS (--op)
# ==========================================
# Test Mean (10 + 20 + 30) / 3 = 20.0
run test_mean python3 print_fires.py --file_name $TEST_CSV --country "United States of America" --country_column 0 --fires_column 3 --op mean
assert_exit_code 0
assert_in_stdout "20"

# Test Median
run test_median python3 print_fires.py --file_name $TEST_CSV --country "United States of America" --country_column 0 --fires_column 3 --op median
assert_exit_code 0
assert_in_stdout "20"

# Test Standard Deviation
run test_std_dev python3 print_fires.py --file_name $TEST_CSV --country "United States of America" --country_column 0 --fires_column 3 --op std_dev
assert_exit_code 0
assert_in_stdout "8.16"

# ==========================================
# 3. EXIT CODES AND ERROR MODES
# ==========================================
# Test missing/non-existent file
run test_missing_file python3 print_fires.py --file_name non_existent.csv --country "United States of America" --country_column 0 --fires_column 3
assert_exit_code 1
assert_in_stderr "Warning"

# Test query for a country not in the CSV
run test_bad_country python3 print_fires.py --file_name $TEST_CSV --country "Atlantis" --country_column 0 --fires_column 3
assert_exit_code 1
assert_in_stderr "Warning"

# Test missing required argument (argparse exit code 2)
run test_missing_args python3 print_fires.py --file_name $TEST_CSV
assert_exit_code 2