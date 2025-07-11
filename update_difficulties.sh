#!/bin/bash

# LeetCode Difficulty Updater
# This script helps manage problem difficulties dynamically

NOTES_DIR="src/notes"
DIFFICULTY_FILE=".difficulty_mapping"

# Function to show usage
show_usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -a, --add <problem_number> <difficulty>    Add/update difficulty for a problem"
    echo "  -r, --remove <problem_number>              Remove difficulty mapping for a problem"
    echo "  -l, --list                                 List all difficulty mappings"
    echo "  -u, --update-notes                         Update all note files with correct difficulties"
    echo "  -h, --help                                 Show this help message"
    echo ""
    echo "Difficulties: Easy, Medium, Hard"
    echo ""
    echo "Examples:"
    echo "  $0 -a 1 Easy"
    echo "  $0 -a 4 Hard"
    echo "  $0 -r 1"
    echo "  $0 -l"
    echo "  $0 -u"
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

# Function to add/update difficulty mapping
add_difficulty() {
    local problem_num=$1
    local difficulty=$2
    
    # Validate difficulty
    case $difficulty in
        "Easy"|"Medium"|"Hard")
            ;;
        *)
            echo "❌ Error: Invalid difficulty '$difficulty'. Use Easy, Medium, or Hard."
            exit 1
            ;;
    esac
    
    # Create difficulty file if it doesn't exist
    touch "$DIFFICULTY_FILE"
    
    # Remove existing entry if it exists
    sed -i.bak "/^$problem_num:/d" "$DIFFICULTY_FILE"
    
    # Add new entry
    echo "$problem_num:$difficulty" >> "$DIFFICULTY_FILE"
    
    echo "✅ Added difficulty mapping: Problem $problem_num -> $difficulty"
}

# Function to remove difficulty mapping
remove_difficulty() {
    local problem_num=$1
    
    if [ -f "$DIFFICULTY_FILE" ]; then
        sed -i.bak "/^$problem_num:/d" "$DIFFICULTY_FILE"
        echo "✅ Removed difficulty mapping for problem $problem_num"
    else
        echo "⚠️  No difficulty mapping file found"
    fi
}

# Function to list all difficulty mappings
list_difficulties() {
    if [ -f "$DIFFICULTY_FILE" ] && [ -s "$DIFFICULTY_FILE" ]; then
        echo "📋 Current Difficulty Mappings:"
        echo "Problem | Difficulty"
        echo "--------|-----------"
        sort -n "$DIFFICULTY_FILE" | while IFS=':' read -r problem difficulty; do
            printf "%-7s | %s\n" "$problem" "$difficulty"
        done
    else
        echo "📋 No difficulty mappings found"
    fi
}

# Function to get difficulty from mapping file
get_difficulty_from_file() {
    local problem_num=$1
    
    if [ -f "$DIFFICULTY_FILE" ]; then
        local difficulty=$(grep "^$problem_num:" "$DIFFICULTY_FILE" | cut -d':' -f2)
        if [ -n "$difficulty" ]; then
            echo "$difficulty"
            return 0
        fi
    fi
    
    # Default to Medium if no mapping found
    echo "Medium"
    return 1
}

# Function to update note files with correct difficulties
update_notes() {
    echo "🔄 Updating note files with correct difficulties..."
    
    local updated_count=0
    
    if [ -d "$NOTES_DIR" ]; then
        for note_file in "$NOTES_DIR"/*.md; do
            if [ -f "$note_file" ]; then
                # Extract problem number from filename
                local filename=$(basename "$note_file")
                local problem_num=$(echo "$filename" | sed 's/^\([0-9]*\)_.*/\1/')
                
                if [ -n "$problem_num" ] && [ "$problem_num" != "$filename" ]; then
                    # Get correct difficulty
                    local correct_difficulty=$(get_difficulty_from_file "$problem_num")
                    local difficulty_color=$(get_difficulty_color "$correct_difficulty")
                    
                    # Update difficulty in note file
                    sed -i.bak "s/\[!\[Difficulty\].*\]/\[!\[Difficulty\](https:\/\/img.shields.io\/badge\/Difficulty-$correct_difficulty-$difficulty_color?style=for-the-badge)\]/" "$note_file"
                    sed -i.bak "s/\*\*Difficulty:\*\* \[.*\]/\*\*Difficulty:\*\* \[$correct_difficulty\](https:\/\/leetcode.com\/problemset\/?difficulty=$(echo "$correct_difficulty" | tr '[:lower:]' '[:upper:]'))/" "$note_file"
                    
                    echo "✅ Updated: $filename -> $correct_difficulty"
                    ((updated_count++))
                fi
            fi
        done
        
        # Clean up backup files
        rm -f "$NOTES_DIR"/*.bak
        rm -f "$DIFFICULTY_FILE.bak"
        
        echo "🎉 Updated $updated_count note files"
    else
        echo "❌ Notes directory not found"
    fi
}

# Main script logic
case "${1:-}" in
    -a|--add)
        if [ $# -eq 3 ]; then
            add_difficulty "$2" "$3"
        else
            echo "❌ Error: Missing arguments for --add"
            show_usage
            exit 1
        fi
        ;;
    -r|--remove)
        if [ $# -eq 2 ]; then
            remove_difficulty "$2"
        else
            echo "❌ Error: Missing problem number for --remove"
            show_usage
            exit 1
        fi
        ;;
    -l|--list)
        list_difficulties
        ;;
    -u|--update-notes)
        update_notes
        ;;
    -h|--help|"")
        show_usage
        ;;
    *)
        echo "❌ Error: Unknown option '$1'"
        show_usage
        exit 1
        ;;
esac 