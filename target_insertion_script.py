import pandas as pd


def generate_sql_from_csv(csv_file_path, output_file_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # SQL statement start
    sql_statement = "INSERT INTO perf_bi_reference.targets (campaign_name, target_month, target_amount)\nVALUES\n"

    # Processing each row to create the SQL values
    value_lines = []
    for _, row in df.iterrows():
        campaign_name = row['CAMPAIGN_NAME']
        target_amount = row['Final Target']
        # Removing the dollar sign and converting to an integer
        target_amount = int(target_amount.replace('$', '').replace(',', ''))
        value_line = f"    ('{campaign_name}', '2024-02-01', {target_amount})"
        value_lines.append(value_line)

    # Combining all lines and ending the statement
    sql_statement += ",\n".join(value_lines) + ";"

    # Writing the SQL statement to a file
    with open(output_file_path, 'w') as file:
        file.write(sql_statement)

    print(f"SQL statement generated and saved to {output_file_path}")


# Example usage
csv_file_path = './target_insertion_script.csv'  # Replace with your CSV file path
# Replace with your desired output file path
output_file_path = './target_insertion_script.txt'
generate_sql_from_csv(csv_file_path, output_file_path)
