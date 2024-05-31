---
tags:
  - MOC-Documentation/Obsidian/vaultDocumentation
Description: A reference guide for the metadata schema used in my Obsidian system.
parent_moc: MOCs/Documentation MOC
related_notes:
  - MOCs/Documentation MOC.md
  - Project - Obsidian Development.md
created: 2024-05-27
updated: 2024-05-27
author: Aaron
status: final
priority:
  - high
---


**Objective:** Develop a comprehensive and structured tagging system in Obsidian that integrates with AI to manage and generate content efficiently.

---

## Current Tagging System

**Tags and Related Files:**

- **Tag: MOC-Project/ObsidianDevelopment**
  - **Files:**
    - `Project - Obsidian Development.md`: Regarding the development of my Obsidian system project

- **Tag: #MOC-Documentation/Obsidian/vaultDocumentation**
  - **Files:**
    - `Inbox/Tagging System Overview.md`: Overview of the tagging system used in my Obsidian vault, including related files and examples

- **Tag: MOC-DailyNotes**
  - **Files:**
    - `MOCs/Daily/ Notes MOC.md`: Hosts all my daily notes

- **Tag: MOC-Documentation**
  - **Files:**
    - `MOCs/Documentation/.md`: Documentation related to software

- **Tag: MOC-Flashcards**
  - **Files:**
    - `MOCs/Flashcards MOC.md`: My Flashcards

- **Tag: MOC-Habits**
  - **Files:**
    - `MOCs/Habits/ MOC.md`: Items to review regularly. Can be related to any topic

- **Tag: MOC-JobSearch**
  - **Files:**
    - `MOCs/Job Search MOC.md`: Job search-related items

- **Tag: MOC-MeetingNotes**
  - **Files:**
    - `MOCs/Meetings MOC.md`: My Meeting Notes

- **Tag: MOC-Projects**
  - **Files:**
    - `MOCs/Projects MOC.md`: My Projects

- **Tag: MOC-StudyMaterials**
  - **Files:**
    - `MOCs/Study Materials MOC.md`: My study materials

- **Tag: MOC-Tasks**
  - **Files:**
    - `MOCs/Tasks MOC.md`: No description available

- **Tag: MOC-Templates**
  - **Files:**
    - `MOCs/Templates MOC.md`: My MOC templates

- **Tag: #Template**
  - **Files:**
    - `Templates/Daily Note Template.md`: Daily note of the day
    - `Templates/MOC Template.md`: MOC template
    - `Templates/Project Template.md`: Project template

- **Tag: Template**
  - **Files:**
    - `Templates/Meeting Note Template.md`: Meeting note template

## Metadata Schema

**Metadata Fields and Descriptions:**

- **tags**
  - **Purpose:** Categorizes the note for easy retrieval and organization.
  - **Description:** A list of tags that categorize the note.
  - **Example:** 
    ```yaml
    tags: [Project/ObsidianDevelopment, Tasks]
    ```

- **Description**
  - **Purpose:** Provides a brief summary of the note’s content.
  - **Description:** A short description of what the note is about.
  - **Example:**
    ```yaml
    Description: "Task list for the development of my Obsidian system."
    ```

- **parent_moc**
  - **Purpose:** Links the note to its parent MOC for hierarchical organization.
  - **Description:** The path to the parent Map of Content (MOC) note.
  - **Example:**
    ```yaml
    parent_moc: "MOCs/Projects MOC"
    ```

- **related_notes**
  - **Purpose:** Lists other notes that are related to this note for easy cross-referencing.
  - **Description:** A list of notes that are relevant to the current note.
  - **Example:**
    ```yaml
    related_notes: ["Project - Obsidian Development.md", "MOCs/Projects MOC.md", "Templates/Project Template.md"]
    ```

- **created**
  - **Purpose:** Records the creation date of the note.
  - **Description:** The date when the note was created.
  - **Example:**
    ```yaml
    created: 2024-05-27
    ```

- **updated**
  - **Purpose:** Records the last update date of the note.
  - **Description:** The date when the note was last updated.
  - **Example:**
    ```yaml
    updated: 2024-05-27
    ```

- **author**
  - **Purpose:** Identifies the creator of the note, useful in collaborative environments.
  - **Description:** The name of the person who created the note.
  - **Example:**
    ```yaml
    author: "Aaron"
    ```

- **status**
  - **Purpose:** Indicates the completion status of the note.
  - **Description:** The current status of the note (e.g., draft, in-progress, final).
  - **Example:**
    ```yaml
    status: "in-progress"
    ```

- **priority**
  - **Purpose:** Assigns a priority level to the note or task.
  - **Description:** The priority level of the note (e.g., high, medium, low).
  - **Example:**
    ```yaml
    priority: "high"
    ```