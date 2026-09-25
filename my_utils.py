import math


def get_column(file_name, query_column, query_value, result_column=1):
    """Extract and convert values from a CSV file matching a query.

    Parameters
    ----------
    file_name : str
        Path to the target CSV file.
    query_column : int
        Column to search for query_value.
    query_value : str
        Target string value to match in query_column.
    result_column : int, optional
        Column containing values to extract. Defaults to 1.

    Returns
    -------
    list of int
        List of integer values extracted from result_column for matching rows.
    """
    result = []

    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return result
    except PermissionError:
        print(f"Error: Permission denied when accessing '{file_name}'.")
        return result

    for line in f:
        line_data = line.strip().split(',')

        if len(line_data) <= max(query_column, result_column):
            continue

        if line_data[query_column] == query_value:
            val_str = line_data[result_column]
            try:
                # Converts float strings (e.g. "12.0") or ints safely
                result.append(int(float(val_str)))
            except ValueError:
                print(f"Warning: Could not convert '{val_str}' to int.")
                continue

    f.close()
    return result


def get_mean(array):
    """Calculate the arithmetic mean of an array of numbers."""
    if array is None:
        raise TypeError("Input array cannot be None")
    if len(array) == 0:
        raise ValueError("Cannot calculate mean of an empty array")

    return sum(array) / len(array)


def get_median(array):
    """Calculate the median of an array of numbers."""
    if array is None:
        raise TypeError("Input array cannot be None")
    if len(array) == 0:
        raise ValueError("Cannot calculate median of an empty array")

    sorted_arr = sorted(array)
    n = len(sorted_arr)
    mid = n // 2

    if n % 2 == 1:
        return sorted_arr[mid]
    else:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2.0


def get_std_dev(array):
    """Calculate the population standard deviation of an array of numbers."""
    if array is None:
        raise TypeError("Input array cannot be None")
    if len(array) == 0:
        raise ValueError("Cannot calculate std dev of an empty array")

    mean = get_mean(array)
    variance = sum((x - mean) ** 2 for x in array) / len(array)
    return math.sqrt(variance)
