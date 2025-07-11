#!/bin/bash

# LeetCode Notes Generator
# This script creates missing note files for solved problems

NOTES_DIR="src/notes"
EXERCISES_DIR="src/exercises"

# Create notes directory if it doesn't exist
mkdir -p "$NOTES_DIR"

echo "🧠 Generating missing LeetCode problem notes..."

# Function to convert problem number to 3-digit format
format_problem_number() {
    local num=$1
    printf "%03d" $num
}

# Function to convert title to filename format
title_to_filename() {
    echo "$1" | tr ' ' '_' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9_]//g'
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
    else
        echo "⏭️  Skipped: $filename (already exists)"
    fi
}

# Define all solved problems with their details
declare -A problems=(
    ["1"]="Two Sum:Easy"
    ["2"]="Add Two Numbers:Medium"
    ["3"]="Longest Substring Without Repeating Characters:Medium"
    ["4"]="Median of Two Sorted Arrays:Hard"
    ["5"]="Longest Palindromic Substring:Medium"
    ["6"]="Zigzag Conversion:Medium"
    ["7"]="Reverse Integer:Medium"
    ["9"]="Palindrome Number:Easy"
    ["10"]="Regular Expression Matching:Hard"
    ["11"]="Container With Most Water:Medium"
    ["13"]="Roman to Integer:Easy"
    ["14"]="Longest Common Prefix:Easy"
    ["15"]="3Sum:Medium"
    ["20"]="Valid Parentheses:Easy"
    ["21"]="Merge Two Sorted Lists:Easy"
    ["22"]="Generate Parentheses:Medium"
    ["28"]="Find the Index of the First Occurrence in a String:Easy"
    ["35"]="Search Insert Position:Easy"
    ["36"]="Valid Sudoku:Medium"
    ["42"]="Trapping Rain Water:Hard"
    ["45"]="Jump Game II:Medium"
    ["50"]="Pow(x, n):Medium"
    ["55"]="Jump Game:Medium"
    ["66"]="Plus One:Easy"
    ["69"]="Sqrt(x):Easy"
    ["74"]="Search a 2D Matrix:Medium"
    ["80"]="Remove Duplicates from Sorted Array II:Medium"
    ["88"]="Merge Sorted Array:Easy"
    ["89"]="Gray Code:Medium"
    ["90"]="Subsets II:Medium"
    ["91"]="Decode Ways:Medium"
    ["92"]="Reverse Linked List II:Medium"
    ["121"]="Best Time to Buy and Sell Stock:Easy"
    ["122"]="Best Time to Buy and Sell Stock II:Medium"
    ["125"]="Valid Palindrome:Easy"
    ["128"]="Longest Consecutive Sequence:Medium"
    ["135"]="Candy:Hard"
    ["141"]="Linked List Cycle:Easy"
    ["149"]="Max Points on a Line:Hard"
    ["150"]="Evaluate Reverse Polish Notation:Medium"
    ["153"]="Find Minimum in Rotated Sorted Array:Medium"
    ["155"]="Min Stack:Medium"
    ["167"]="Two Sum II - Input Array Is Sorted:Medium"
    ["169"]="Majority Element:Easy"
    ["172"]="Factorial Trailing Zeroes:Medium"
    ["189"]="Rotate Array:Medium"
    ["202"]="Happy Number:Easy"
    ["205"]="Isomorphic Strings:Easy"
    ["206"]="Reverse Linked List:Easy"
    ["217"]="Contains Duplicate:Easy"
    ["219"]="Contains Duplicate II:Easy"
    ["228"]="Summary Ranges:Easy"
    ["238"]="Product of Array Except Self:Medium"
    ["242"]="Valid Anagram:Easy"
    ["243"]="Shortest Word Distance:Easy"
    ["244"]="Shortest Word Distance II:Medium"
    ["245"]="Shortest Word Distance III:Medium"
    ["246"]="Strobogrammatic Number:Easy"
    ["248"]="Strobogrammatic Number III:Hard"
    ["290"]="Word Pattern:Easy"
    ["383"]="Ransom Note:Easy"
    ["392"]="Is Subsequence:Easy"
    ["704"]="Binary Search:Easy"
    ["875"]="Koko Eating Bananas:Medium"
    ["990"]="Satisfiability of Equality Equations:Medium"
    ["1200"]="Minimum Absolute Difference:Easy"
    ["1298"]="Maximum Candies You Can Get from Boxes:Medium"
    ["1820"]="Maximum Number of Accepted Invitations:Medium"
    ["2040"]="Kth Smallest Product of Two Sorted Arrays:Medium"
    ["2053"]="Kth Distinct String in an Array:Easy"
    ["2116"]="Check if a Parentheses String Can Be Valid:Medium"
    ["2294"]="Partition Array Such That Maximum Difference Is K:Medium"
    ["2441"]="Largest Positive Integer That Exists With Its Negative:Easy"
    ["2616"]="Minimize the Maximum Difference of Pairs:Medium"
    ["2966"]="Divide Array Into Arrays With Max Difference:Medium"
    ["3442"]="Maximum Difference Between Even and Odd Frequency I:Easy"
    ["3445"]="Maximum Difference Between Even and Odd Frequency II:Easy"
)

# Create note files for all problems
for problem_num in "${!problems[@]}"; do
    IFS=':' read -r title difficulty <<< "${problems[$problem_num]}"
    create_note_file "$problem_num" "$title" "$difficulty"
done

echo ""
echo "🎉 Note generation complete!"
echo "📝 Total problems processed: ${#problems[@]}"
echo "📁 Notes directory: $NOTES_DIR"
echo ""
echo "💡 Tip: Run this script whenever you solve new problems to automatically create note templates." 