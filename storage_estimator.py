print("Added a estimation feature!!!")
def estimate_storage(file_count: int, average_file_size_mb: float) -> None:
    """Calculates total storage needed and prints the result in MB and GB."""
    # Calculate total size in Megabytes
    total_mb = file_count * average_file_size_mb
    
    # Convert Megabytes to Gigabytes (1 GB = 1024 MB)
    total_gb = total_mb / 1024
    
    # Display the results
    print("--- Storage Estimate Results ---")
    print(f"Total Files: {file_count:,}")
    print(f"Estimated Size (MB): {total_mb:,.2f} MB")
    print(f"Estimated Size (GB): {total_gb:,.2f} GB")  # Added GB conversion line

# Example usage:
# If you have 5,000 files that average 4.5 MB each:
estimate_storage(file_count=5000, average_file_size_mb=4.5)
