import os
import subprocess
from datetime import datetime

vault_path = "C:/Users/erinh.HYPERVSERVER/OneDrive/ObsidianVaults/Development/GroundUpRestart - Backup"

# Change to the vault directory
os.chdir(vault_path)

# Add all changes to Git
subprocess.run(["git", "add", "."])

# Commit the changes with a timestamp
commit_message = f"Backup on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocess.run(["git", "commit", "-m", commit_message])

print("Backup completed with Git.")
