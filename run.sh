echo "=== Example 1: Successful Execution ==="
python print_fires.py \
    --file_name Agrofood_co2_emission.csv \
    --country "United States of America" \
    --country_column 0 \
    --fires_column 3

echo "=== Example 2: not enough arguments"
python print_fires.py --country "United States of America"

echo "=== Example 3: file path does not exist"
python print_fires.py \
    --file_name non_existent_file.csv \
    --country "United States of America" \
    --country_column 0 \
    --fires_column 3