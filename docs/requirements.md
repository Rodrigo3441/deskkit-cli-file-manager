# Deskkit File Manager

A command-line application that allows users to inspect directories, search for files, organize files, and generate reports about directory contents.

## Functional Requirements

- FR-01 — Command-line interface: The system must allow users to interact with the application through a text-based interface.
- FR-02 — Directory inspection: The system must allow users to specify a directory and inspect its contents.
- FR-03 — File search: The system must allow users to search for files within a specified directory.
- FR-04 — File statistics: The system must generate reports containing the total number of files and the number of files grouped by extension.
- FR-05 — File information: The system must display relevant information about individual files, such as their names, extensions, sizes, and last modification dates.
- FR-06 — User confirmation: The system must request explicit user confirmation before performing operations that modify files or directories.
- FR-07 — File organization: The system must allow users to organize or move files according to defined criteria, subject to user confirmation.

## Non-Functional Requirements

- NFR-01 — Safety: The system must not modify or delete files without explicit user confirmation.
- NFR-02 — Error handling: The system must provide understandable error messages when operations fail.
- NFR-03 — Usability: The system must present results and instructions in a clear, readable format.
- NFR-04 — Maintainability: The code should be organized so that individual features can be tested and modified independently.


### Directory Statistics

- The system must scan only the selected directory, without including its subdirectories.
- The report must display the total number of files found across the entire directory tree.
- The report must display the number of files grouped by extension across the entire directory tree.
- The report must not separate the overall statistics by individual subdirectory.