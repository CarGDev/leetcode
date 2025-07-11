# LeetCode Repository Scripts Documentation

This document provides comprehensive guidance on using the automation scripts in this LeetCode solutions repository.

## 📋 Table of Contents

- [Overview](#overview)
- [Scripts Overview](#scripts-overview)
- [Installation & Setup](#installation--setup)
- [create_missing_notes.sh](#create_missing_notessh)
- [update_difficulties.sh](#update_difficultiessh)
- [Workflow Examples](#workflow-examples)
- [File Structure](#file-structure)
- [Troubleshooting](#troubleshooting)
- [Advanced Usage](#advanced-usage)

## 🎯 Overview

This repository contains two powerful automation scripts designed to streamline your LeetCode learning journey:

1. **`create_missing_notes.sh`** - Automatically generates structured note templates for solved problems
2. **`update_difficulties.sh`** - Manages problem difficulty mappings dynamically

These scripts help maintain a professional, well-organized repository with proper documentation, badges, and links.

## 🔧 Scripts Overview

| Script | Purpose | Key Features |
|--------|---------|--------------|
| `create_missing_notes.sh` | Generate note templates | • Auto-detects solved problems<br>• Creates structured markdown notes<br>• Includes badges and links<br>• Skips existing files |
| `update_difficulties.sh` | Manage difficulty mappings | • Add/remove difficulty mappings<br>• Update all note files<br>• List current mappings<br>• Dynamic difficulty management |

## 🚀 Installation & Setup

### Prerequisites
- Bash shell (macOS, Linux, or WSL on Windows)
- Git repository with LeetCode solutions

### Setup Steps
1. Ensure scripts are executable:
   ```bash
   chmod +x create_missing_notes.sh
   chmod +x update_difficulties.sh
   ```

2. Verify your directory structure:
   ```
   leetcode/
   ├── src/
   │   ├── exercises/     # Your Python solutions
   │   └── notes/        # Generated notes (created automatically)
   ├── create_missing_notes.sh
   ├── update_difficulties.sh
   └── SCRIPTS_DOCUMENTATION.md
   ```

## 📝 create_missing_notes.sh

### Purpose
Automatically generates structured markdown note files for all solved problems that don't have notes yet.

### Usage
```bash
./create_missing_notes.sh
```

### What It Does
1. **Scans** `src/exercises/` directory for Python solution files
2. **Extracts** problem numbers and titles from filenames
3. **Creates** corresponding note files in `src/notes/` with:
   - Professional badges and shields
   - Links to LeetCode problems
   - Structured sections for learning notes
   - Navigation links
4. **Skips** files that already have notes

### Generated Note Structure
Each note file includes:
- **Header** with problem title and badges
- **Problem metadata** (number, difficulty, category, LeetCode link)
- **Learning sections**:
  - Problem Description
  - My Approach
  - Solution
  - Time & Space Complexity
  - Key Insights
  - Mistakes Made
  - Related Problems
- **Navigation links** back to index and solution

### Example Output
```
🧠 Scanning exercises directory and generating missing LeetCode problem notes...
✅ Created: src/notes/001_two_sum.md
⏭️  Skipped: src/notes/002_add_two_numbers.md (already exists)
✅ Created: src/notes/003_longest_substring_without_repeating_characters.md

🎉 Note generation complete!
📝 Files processed: 95
✅ New notes created: 15
⏭️  Notes skipped (already exist): 80
📁 Notes directory: src/notes
```

## 🎯 update_difficulties.sh

### Purpose
Manages problem difficulty mappings dynamically without hardcoding, and updates note files accordingly.

### Usage Options

#### Add/Update Difficulty
```bash
./update_difficulties.sh -a <problem_number> <difficulty>
```
**Examples:**
```bash
./update_difficulties.sh -a 1 Easy
./update_difficulties.sh -a 4 Hard
./update_difficulties.sh -a 15 Medium
```

#### Remove Difficulty Mapping
```bash
./update_difficulties.sh -r <problem_number>
```
**Example:**
```bash
./update_difficulties.sh -r 1
```

#### List All Mappings
```bash
./update_difficulties.sh -l
```
**Output:**
```
📋 Current Difficulty Mappings:
Problem | Difficulty
--------|-----------
1       | Easy
2       | Medium
4       | Hard
15      | Medium
```

#### Update All Note Files
```bash
./update_difficulties.sh -u
```
Updates all note files to reflect correct difficulties from the mapping file.

#### Show Help
```bash
./update_difficulties.sh -h
```

### Difficulty Mapping File
The script creates and manages a `.difficulty_mapping` file:
```
1:Easy
2:Medium
4:Hard
15:Medium
```

## 🔄 Workflow Examples

### New Problem Workflow
When you solve a new problem:

```bash
# 1. Add your solution to src/exercises/
# 2. Generate note template
./create_missing_notes.sh

# 3. Add correct difficulty
./update_difficulties.sh -a 42 Hard

# 4. Update all notes with correct difficulties
./update_difficulties.sh -u

# 5. Edit the generated note with your insights
# File: src/notes/042_trapping_rain_water.md
```

### Batch Processing
Process multiple problems at once:

```bash
# Generate notes for all solved problems
./create_missing_notes.sh

# Add difficulties for multiple problems
./update_difficulties.sh -a 1 Easy
./update_difficulties.sh -a 2 Medium
./update_difficulties.sh -a 4 Hard
./update_difficulties.sh -a 15 Medium

# Update all notes
./update_difficulties.sh -u
```

### Maintenance Workflow
Regular maintenance tasks:

```bash
# Check current difficulty mappings
./update_difficulties.sh -l

# Remove incorrect mapping
./update_difficulties.sh -r 1

# Add correct mapping
./update_difficulties.sh -a 1 Easy

# Update all notes
./update_difficulties.sh -u
```

## 📁 File Structure

After running the scripts, your repository will have this structure:

```
leetcode/
├── src/
│   ├── exercises/
│   │   ├── 1.two-sum.py
│   │   ├── 2.add-two-numbers.py
│   │   └── ...
│   └── notes/
│       ├── 001_two_sum.md
│       ├── 002_add_two_numbers.md
│       └── ...
├── .difficulty_mapping          # Created by update_difficulties.sh
├── create_missing_notes.sh
├── update_difficulties.sh
├── SCRIPTS_DOCUMENTATION.md
└── README.md
```

### Generated Note Example
```markdown
# Two Sum

[![Problem 1](https://img.shields.io/badge/Problem-1-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/two-sum/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=EASY)
[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/two-sum/)

**Problem Number:** [1](https://leetcode.com/problems/two-sum/)
**Difficulty:** [Easy](https://leetcode.com/problemset/?difficulty=EASY)
**Category:** 
**LeetCode Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

## Problem Description

> **View the full problem description on LeetCode:** [Two Sum](https://leetcode.com/problems/two-sum/)

## My Approach

## Solution

## Time & Space Complexity

## Key Insights

## Mistakes Made

## Related Problems

---

[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/1.two-sum.py)](../exercises/1.two-sum.py)

*Note: This is a work in progress. I'll add more details as I reflect on this problem.*
```

## 🔧 Troubleshooting

### Common Issues

#### Script Permission Denied
```bash
chmod +x create_missing_notes.sh
chmod +x update_difficulties.sh
```

#### Notes Directory Not Found
The script automatically creates the `src/notes/` directory if it doesn't exist.

#### Invalid Difficulty
Valid difficulties are: `Easy`, `Medium`, `Hard` (case-sensitive)

#### File Not Found Errors
Ensure your Python solution files follow the naming convention: `number.problem-name.py`

### Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| `❌ Error: Invalid difficulty` | Wrong difficulty format | Use: Easy, Medium, or Hard |
| `⚠️  Skipped empty file` | Empty solution file | Add solution code |
| `⚠️  Skipped invalid filename` | Wrong file naming | Use: `number.problem-name.py` |

## 🚀 Advanced Usage

### Customizing Note Templates
Edit the `create_note_file()` function in `create_missing_notes.sh` to customize note structure.

### Batch Difficulty Updates
Create a script to update multiple difficulties:

```bash
#!/bin/bash
# batch_update_difficulties.sh

difficulties=(
    "1:Easy"
    "2:Medium"
    "4:Hard"
    "15:Medium"
)

for mapping in "${difficulties[@]}"; do
    problem_num=$(echo $mapping | cut -d':' -f1)
    difficulty=$(echo $mapping | cut -d':' -f2)
    ./update_difficulties.sh -a $problem_num $difficulty
done

./update_difficulties.sh -u
```

### Integration with Git
Add to your workflow:

```bash
# After solving a problem
./create_missing_notes.sh
./update_difficulties.sh -a <problem_number> <difficulty>
./update_difficulties.sh -u
git add .
git commit -m "Add solution and notes for problem <number>"
```

## 📚 Best Practices

1. **Run `create_missing_notes.sh`** after solving new problems
2. **Update difficulties** as you learn them
3. **Use `-u` flag** to keep all notes synchronized
4. **Edit generated notes** with your personal insights
5. **Commit changes** regularly to track your progress

## 🤝 Contributing

To improve these scripts:
1. Test changes thoroughly
2. Update this documentation
3. Follow the existing code style
4. Add error handling for edge cases

---

**Happy Coding! 🎉**

*These scripts are designed to make your LeetCode learning journey more organized and professional.* 