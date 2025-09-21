import pandas as pd

def export_data(df: pd.DataFrame, file_path: str, format: str = "csv"):
    """
    Export a pandas DataFrame into different formats.
    Supported formats: csv, excel, json
    """
    if format == "csv":
        df.to_csv(file_path, index=False)
    elif format == "excel":
        df.to_excel(file_path, index=False)
    elif format == "json":
        df.to_json(file_path, orient="records", indent=2)
    else:
        raise ValueError("Unsupported format. Choose 'csv', 'excel', or 'json'.")

