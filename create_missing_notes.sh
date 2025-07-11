#!/bin/bash

# LeetCode Notes Generator
# This script automatically creates missing note files for solved problems

NOTES_DIR="src/notes"
EXERCISES_DIR="src/exercises"

# Create notes directory if it doesn't exist
mkdir -p "$NOTES_DIR"

echo "🧠 Scanning exercises directory and generating missing LeetCode problem notes..."

# Function to convert problem number to 3-digit format
format_problem_number() {
    local num=$1
    printf "%03d" $num
}

# Function to convert title to filename format
title_to_filename() {
    echo "$1" | tr ' ' '_' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9_]//g'
}

# Function to extract problem number from filename
extract_problem_number() {
    local filename=$1
    echo "$filename" | sed 's/^\([0-9]*\)\..*/\1/'
}

# Function to convert filename to problem title
filename_to_title() {
    local filename=$1
    # Remove the .py extension and problem number
    local title=$(echo "$filename" | sed 's/^[0-9]*\.//' | sed 's/\.py$//')
    # Convert kebab-case to Title Case with proper handling
    echo "$title" | sed 's/-/ /g' | sed 's/\b\w/\U&/g' | sed 's/\bii\b/II/g' | sed 's/\biii\b/III/g'
}

# Function to get difficulty color for shields
get_difficulty_color() {
    local difficulty=$1
    case $difficulty in
        "Easy")
            echo "brightgreen"
            ;;
        "Medium")
            echo "orange"
            ;;
        "Hard")
            echo "red"
            ;;
        *)
            echo "blue"
            ;;
    esac
}

# Function to determine difficulty dynamically (default to Medium for unknown problems)
get_difficulty() {
    local problem_num=$1
    
    # For now, default to Medium for all problems
    # This can be enhanced later with API calls or a separate difficulty mapping file
    echo "Medium"
}

# Function to create note file
create_note_file() {
    local problem_num=$1
    local title=$2
    local difficulty=$3
    local filename="$NOTES_DIR/$(format_problem_number $problem_num)_$(title_to_filename "$title").md"
    
    if [ ! -f "$filename" ]; then
        local difficulty_color=$(get_difficulty_color "$difficulty")
        local leetcode_url="https://leetcode.com/problems/$(echo "$title" | tr ' ' '-')/"
        
        echo "# $title" > "$filename"
        echo "" >> "$filename"
        echo "[![Problem $problem_num](https://img.shields.io/badge/Problem-$problem_num-blue?style=for-the-badge&logo=leetcode)](https://leetcode.com/problems/$(echo "$title" | tr ' ' '-')/)" >> "$filename"
        echo "[![Difficulty](https://img.shields.io/badge/Difficulty-$difficulty-$difficulty_color?style=for-the-badge)](https://leetcode.com/problemset/?difficulty=$(echo "$difficulty" | tr '[:lower:]' '[:upper:]'))" >> "$filename"
        echo "[![LeetCode](https://img.shields.io/badge/LeetCode-View%20Problem-orange?style=for-the-badge&logo=leetcode)]($leetcode_url)" >> "$filename"
        echo "" >> "$filename"
        echo "**Problem Number:** [$problem_num]($leetcode_url)" >> "$filename"
        echo "**Difficulty:** [$difficulty](https://leetcode.com/problemset/?difficulty=$(echo "$difficulty" | tr '[:lower:]' '[:upper:]'))" >> "$filename"
        echo "**Category:** " >> "$filename"
        echo "**LeetCode Link:** [$leetcode_url]($leetcode_url)" >> "$filename"
        echo "" >> "$filename"
        echo "## Problem Description" >> "$filename"
        echo "" >> "$filename"
        echo "> **View the full problem description on LeetCode:** [$title]($leetcode_url)" >> "$filename"
        echo "" >> "$filename"
        echo "## My Approach" >> "$filename"
        echo "" >> "$filename"
        echo "## Solution" >> "$filename"
        echo "" >> "$filename"
        echo "## Time & Space Complexity" >> "$filename"
        echo "" >> "$filename"
        echo "## Key Insights" >> "$filename"
        echo "" >> "$filename"
        echo "## Mistakes Made" >> "$filename"
        echo "" >> "$filename"
        echo "## Related Problems" >> "$filename"
        echo "" >> "$filename"
        echo "---" >> "$filename"
        echo "" >> "$filename"
        echo "[![Back to Index](../../README.md#-problem-index)](../../README.md#-problem-index) | [![View Solution](../exercises/$problem_num.$(echo "$title" | tr ' ' '-').py)](../exercises/$problem_num.$(echo "$title" | tr ' ' '-').py)" >> "$filename"
        echo "" >> "$filename"
        echo "*Note: This is a work in progress. I'll add more details as I reflect on this problem.*" >> "$filename"
        
        echo "✅ Created: $filename"
        return 0
    else
        echo "⏭️  Skipped: $filename (already exists)"
        return 1
    fi
}

# Counter for statistics
created_count=0
skipped_count=0

# Scan exercises directory for Python files
if [ -d "$EXERCISES_DIR" ]; then
    for file in "$EXERCISES_DIR"/*.py; do
        if [ -f "$file" ]; then
            # Extract filename without path
            filename=$(basename "$file")
            
            # Skip empty files
            if [ ! -s "$file" ]; then
                echo "⚠️  Skipped empty file: $filename"
                continue
            fi
            
            # Extract problem number
            problem_num=$(extract_problem_number "$filename")
            
            # Skip if no problem number found
            if [ -z "$problem_num" ] || [ "$problem_num" = "$filename" ]; then
                echo "⚠️  Skipped invalid filename: $filename"
                continue
            fi
            
            # Convert filename to title
            title=$(filename_to_title "$filename")
            
            # Get difficulty (default to Medium for now)
            difficulty=$(get_difficulty "$problem_num")
            
            # Create note file
            if create_note_file "$problem_num" "$title" "$difficulty"; then
                ((created_count++))
            else
                ((skipped_count++))
            fi
        fi
    done
else
    echo "❌ Error: Exercises directory '$EXERCISES_DIR' not found!"
    exit 1
fi

echo ""
echo "🎉 Note generation complete!"
echo "📝 Files processed: $((created_count + skipped_count))"
echo "✅ New notes created: $created_count"
echo "⏭️  Notes skipped (already exist): $skipped_count"
echo "📁 Notes directory: $NOTES_DIR"
echo ""
echo "💡 Tip: Run this script whenever you solve new problems to automatically create note templates."
echo "🔧 Note: All problems default to 'Medium' difficulty. You can manually update difficulties in the notes." 