import os
import yaml
import pandas as pd
from datetime import datetime
from tabulate import tabulate

# Define the path to your Obsidian vault
vault_path = "C:/Users/erinh.HYPERVSERVER/OneDrive/ObsidianVaults/Development/GroundUpRestart - Backup"

# Define folders to ignore
ignored_folders = ["Templates", "Attachments", "Archive"]

# Function to extract metadata from a file
def extract_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Extract YAML front matter
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                yaml_content = content[3:end].strip()
                try:
                    metadata = yaml.safe_load(yaml_content)
                    return metadata
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML in {file_path}: {e}")
    return {}

# Initialize an empty list to store metadata
metadata_list = []

# Walk through all files in the vault directory
for root, dirs, files in os.walk(vault_path):
    # Skip ignored folders
    if any(ignored_folder in root for ignored_folder in ignored_folders):
        continue
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            metadata = extract_metadata(file_path)
            if metadata:
                metadata['File'] = os.path.relpath(file_path, vault_path).replace("\\", "/")
                metadata_list.append(metadata)

# Create a DataFrame from the metadata
df = pd.DataFrame(metadata_list)

# Ensure all columns are present
columns = ["tags", "Description", "parent_moc", "related_notes", "created", "updated", "author", "status", "priority", "File"]
for column in columns:
    if column not in df.columns:
        df[column] = None

# Format list values as strings to ensure proper display
for column in ["tags", "related_notes"]:
    df[column] = df[column].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)

# Convert DataFrame to markdown table string
markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)

# Add table header and format
header = "# Master MOC\n\n"

# Save the markdown table to a file
output_file = os.path.join(vault_path, 'metadataMKD.md')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(header + markdown_table)

print(f"Metadata has been saved to {output_file}")
