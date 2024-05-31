import os
import re
import yaml
from collections import defaultdict

# Define the path to your Obsidian vault
vault_path = "C:/Users/erinh.HYPERVSERVER/OneDrive/ObsidianVaults/Development/GroundUpRestart - Backup"

def extract_metadata(file_path):
    """Extracts tags and description from a markdown file."""
    tags = set()
    description = "No description available"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if yaml_match:
                yaml_content = yaml_match.group(1)
                yaml_content_clean = '\n'.join(line for line in yaml_content.split('\n') if '{{' not in line and '}}' not in line)
                yaml_data = yaml.safe_load(yaml_content_clean)
                if yaml_data:
                    tags.update(yaml_data.get('tags', []))
                    description = yaml_data.get('Description', description)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return tags, description

def collect_tags(vault_path):
    """Collects tags and their corresponding files and descriptions from the vault."""
    tags_dict = defaultdict(list)
    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                tags, description = extract_metadata(file_path)
                relative_path = os.path.relpath(file_path, vault_path).replace("\\", "/")
                for tag in tags:
                    tags_dict[tag].append((relative_path, description))
    return tags_dict

def save_tags_to_file(tags_dict, output_file):
    """Saves the tags and their corresponding files and descriptions to a file."""
    with open(output_file, "w", encoding='utf-8') as f:
        for tag, entries in tags_dict.items():
            f.write(f"Tag: {tag}\n")
            for file, description in entries:
                f.write(f"  - {file}: {description}\n")
            f.write("\n")
    print(f"Tags and their corresponding files and descriptions have been saved to {output_file}")

def main():
    """Main function to extract and save tags."""
    tags_dict = collect_tags(vault_path)
    output_file = "tags_with_files_and_descriptions.txt"
    save_tags_to_file(tags_dict, output_file)

if __name__ == "__main__":
    main()
