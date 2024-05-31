---
tags:
  - MOC-Documentation/Obsidian
  - "#MOC-Documentation/Git"
Description: A detailed walkthrough on setting up Git using Conda, initializing a Git repository, and automating backups in your Obsidian vault.
parent_moc: MOCs/Documentation MOC
related_notes:
  - MOCs/Documentation MOC.md
  - Inbox/necessary metadata.md
  - Project - Obsidian Development.md
created: 2024-05-28
updated: 2024-05-28
author: Aaron
status: final
priority:
  - high
---

# Setting Up Git and Automating Backups with Conda

## Introduction
This document provides a step-by-step guide on how to set up Git using Conda, initialize a Git repository in your Obsidian vault, and automate the backup process. This ensures your notes are safely stored and easily recoverable.

## Step 1: Install Git via Conda

1. **Open Anaconda Prompt**:
   - Search for "Anaconda Prompt" in your start menu and open it.

2. **Create a New Conda Environment (Optional)**:
   - If you want to keep Git in a separate environment, create a new environment:
     ```sh
     conda create --name git_env
     conda activate git_env
     ```

3. **Install Git**:
   - Install Git in your Conda environment:
     ```sh
     conda install -c anaconda git
     ```

4. **Verify Installation**:
   - Verify that Git has been installed correctly:
     ```sh
     git --version
     ```
   - You should see the Git version information if the installation was successful.

## Step 2: Initialize a Git Repository in Your Vault

1. **Navigate to Your Vault Directory**:
   - Change to the directory of your Obsidian vault. Replace the path with your actual vault path:
     ```sh
     cd "C:/Users/erinh.HYPERVSERVER/OneDrive/ObsidianVaults/Development/GroundUpRestart - Backup"
     ```

2. **Initialize a Git Repository**:
   - Initialize a new Git repository in your vault directory:
     ```sh
     git init
     ```

3. **Configure Git**:
   - Set your Git user name and email:
     ```sh
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```

4. **Commit Your Files**:
   - Add all files to the repository:
     ```sh
     git add .
     ```
   - Commit the files:
     ```sh
     git commit -m "Initial commit"
     ```

## Step 3: Automating Backups with Git

1. **Create a Python Script**:
   - Create a Python script to automate the backup process. You can name it `backup_script.py` and place it in your vault directory.
   - Here’s the script:
     ```python
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
     ```

2. **Run the Script**:
   - Run the script using the Anaconda Prompt:
     ```sh
     python backup_script.py
     ```

## Step 4: Optional - Pushing to a Remote Repository

If you want to push your commits to a remote repository like GitHub or GitLab:

1. **Add a Remote Repository**:
   - Add your remote repository (replace the URL with your repository URL):
     ```sh
     git remote add origin https://github.com/yourusername/your-repo.git
     ```

2. **Push to the Remote Repository**:
   - Push your initial commit to the remote repository:
     ```sh
     git push -u origin master
     ```

## Additional Tips

- **Regular Commits**: Schedule this script to run regularly (e.g., daily) using Task Scheduler (Windows) or Cron (Linux/Mac).
- **Check for Errors**: Ensure that the script logs errors or issues during the backup process, which you can review periodically.

By following these steps, you’ll set up Git for version control and automate the backup process for your Obsidian vault, ensuring your data is safely stored and easily recoverable.
