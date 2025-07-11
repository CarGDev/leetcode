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

# Function to determine difficulty based on problem number ranges
get_difficulty() {
    local problem_num=$1
    
    # Hard problems (known)
    case $problem_num in
        4|10|42|135|149|248)
            echo "Hard"
            ;;
        # Easy problems (known)
        1|9|13|14|20|21|28|35|66|69|88|121|125|141|169|202|205|206|217|219|228|242|243|246|290|383|392|704|1200|2053|2441|3442|3445)
            echo "Easy"
            ;;
        # Everything else is Medium
        *)
            echo "Medium"
            ;;
    esac
}

# Function to create note file
create_note_file() {
    local problem_num=$1
    local title=$2
    local difficulty=$3
    local filename="$NOTES_DIR/$(format_problem_number $problem_num)_$(title_to_filename "$title").md"
    
    if [ ! -f "$filename" ]; then
        echo "# $title" > "$filename"
        echo "" >> "$filename"
        echo "**Problem Number:** $problem_num" >> "$filename"
        echo "**Difficulty:** $difficulty" >> "$filename"
        echo "**Category:** " >> "$filename"
        echo "" >> "$filename"
        echo "## Problem Description" >> "$filename"
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
            
            # Get difficulty
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