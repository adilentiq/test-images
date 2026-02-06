#!/usr/bin/env python3
"""
Script to automatically generate image-paths.json by scanning the workspace
for image and audio files and creating entries with GitHub URLs.
"""

import os
import json
from pathlib import Path

# Configuration
GITHUB_BASE_URL = "https://raw.githubusercontent.com/adilentiq/test-images/refs/heads/main"
WORKSPACE_ROOT = Path(__file__).parent
OUTPUT_FILE = "image-paths.json"

# Supported file extensions
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp', '.tiff', '.svg'}
AUDIO_EXTENSIONS = {'.mp3', '.wav', '.aiff', '.mp2', '.ogg', '.flac', '.m4a', '.aac'}
SUPPORTED_EXTENSIONS = IMAGE_EXTENSIONS | AUDIO_EXTENSIONS

# Directories to exclude from scanning
EXCLUDE_DIRS = {'.git', 'node_modules', '__pycache__', '.vscode', 'temp'}


def scan_files(root_dir):
    """
    Scan the workspace for supported files and return their paths.
    
    Args:
        root_dir: Root directory to scan
        
    Returns:
        List of Path objects for supported files
    """
    files = []
    
    for item in root_dir.rglob('*'):
        # Skip excluded directories
        if any(exclude in item.parts for exclude in EXCLUDE_DIRS):
            continue
            
        # Check if it's a file with a supported extension
        if item.is_file() and item.suffix.lower() in SUPPORTED_EXTENSIONS:
            files.append(item)
    
    return files


def generate_entries(files, root_dir):
    """
    Generate JSON entries for each file.
    
    Args:
        files: List of Path objects
        root_dir: Root directory for calculating relative paths
        
    Returns:
        List of dictionaries with path and url keys
    """
    entries = []
    
    for file_path in sorted(files):
        # Calculate relative path from workspace root
        relative_path = file_path.relative_to(root_dir)
        # Convert Windows path to forward slashes for URLs
        path_str = str(relative_path).replace('\\', '/')
        
        entry = {
            "path": path_str,
            "url": f"{GITHUB_BASE_URL}/{path_str}"
        }
        entries.append(entry)
    
    return entries


def main():
    """Main function to generate image-paths.json"""
    print(f"Scanning workspace: {WORKSPACE_ROOT}")
    
    # Scan for files
    files = scan_files(WORKSPACE_ROOT)
    print(f"Found {len(files)} files")
    
    # Generate entries
    entries = generate_entries(files, WORKSPACE_ROOT)
    
    # Create output structure
    output = {
        "images": entries
    }
    
    # Write to file
    output_path = WORKSPACE_ROOT / OUTPUT_FILE
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully wrote {len(entries)} entries to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
