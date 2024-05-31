---
tags:
  - MOC-Documentation/Obsidian
  - "#MOC-Documentation/Jupyter"
title: Jupyter Documentation Hub
date: <% tp.date.now("YYYY-MM-DD") %>
author: Aaron
status: In Progress
priority:
  - High
---


## Overview
This note serves as a centralized hub for all Jupyter-related documentation within my Obsidian vault. It includes setup guides, best practices, and integration tips for using Jupyter Notebooks and JupyterLab.

## Table of Contents
- [Setup and Installation](#setup-and-installation)
- [Popular Extensions and Plugins](#popular-extensions-and-plugins)
- [Best Practices](#best-practices)
- [Integration with Obsidian](#integration-with-obsidian)
- [References and Resources](#references-and-resources)

## Setup and Installation

### Anaconda Environment
To ensure Jupyter Notebook runs from your designated Anaconda environment, follow these steps:

```bash
# Activate your environment
conda activate Obsidian_env

# Install Jupyter Notebook
conda install jupyter

# Install ipykernel if not already installed
conda install ipykernel

# Add the environment as a Jupyter kernel
python -m ipykernel install --user --name Obsidian_env --display-name "Python (Obsidian_env)"

# Launch Jupyter Notebook
cd path/to/your/obsidian/vault
jupyter notebook
