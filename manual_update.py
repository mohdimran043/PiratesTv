#!/usr/bin/env python3
"""
Manual M3U updater - Downloads M3U file from config and filters using template
"""

import requests
import os
import json
import re
from datetime import datetime

def load_config():
    """Load configuration from config.json"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config.get('m3u_download_url')
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error loading config: {e}")
        return None

def parse_m3u_content(content):
    """Parse M3U content and return list of channels"""
    channels = []
    lines = content.strip().split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('#EXTINF:'):
            # Extract channel info from EXTINF line
            extinf_line = line
            
            # Get the next non-empty line as URL
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            
            if i < len(lines):
                url = lines[i].strip()
                if url and not url.startswith('#'):
                    channels.append({
                        'extinf': extinf_line,
                        'url': url
                    })
        i += 1
    
    return channels

def load_template_channels():
    """Load channel names from template.m3u"""
    try:
        with open('template.m3u', 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        template_channels = parse_m3u_content(template_content)
        
        # Extract channel names for matching
        template_names = set()
        for channel in template_channels:
            # Extract channel name from EXTINF line
            match = re.search(r',(.+)$', channel['extinf'])
            if match:
                channel_name = match.group(1).strip()
                template_names.add(channel_name.lower())
        
        print(f"📋 Loaded {len(template_names)} channel names from template")
        return template_names
        
    except FileNotFoundError:
        print("❌ template.m3u not found")
        return set()
    except Exception as e:
        print(f"Error loading template: {e}")
        return set()

def download_and_filter_m3u(url, template_names, output_file):
    """Download M3U file and filter based on template"""
    try:
        print(f"📥 Downloading M3U file from: {url}")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=60)
        response.raise_for_status()
        
        content = response.text
        if not content.strip().startswith('#EXTM3U') and '#EXTINF:' not in content:
            print("⚠️  Warning: Downloaded content doesn't appear to be a valid M3U file")
            return False
        
        print(f"✅ Downloaded M3U file successfully")
        
        # Parse downloaded content
        all_channels = parse_m3u_content(content)
        print(f"📺 Total channels in downloaded file: {len(all_channels)}")
        
        # Filter channels based on template
        filtered_channels = []
        for channel in all_channels:
            # Extract channel name from EXTINF line
            match = re.search(r',(.+)$', channel['extinf'])
            if match:
                channel_name = match.group(1).strip().lower()
                if channel_name in template_names:
                    filtered_channels.append(channel)
        
        print(f"🎯 Filtered channels matching template: {len(filtered_channels)}")
        
        # Write filtered content to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("#EXTM3U\n")
            f.write("# Filtered playlist based on template.m3u\n")
            f.write(f"# Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total channels: {len(filtered_channels)}\n")
            f.write("\n")
            
            for channel in filtered_channels:
                f.write(f"{channel['extinf']}\n")
                f.write(f"{channel['url']}\n")
        
        print(f"💾 Filtered playlist saved to: {output_file}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading file: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    print("🚀 Manual M3U Update with Template Filtering")
    print("=" * 50)
    
    # Load M3U URL from config
    m3u_url = load_config()
    if not m3u_url:
        print("❌ Could not load M3U download URL from config.json")
        return 1
    
    print(f"🔗 Source URL: {m3u_url}")
    print(f"📁 Output file: freetv.m3u")
    print("")
    
    # Load template channel names
    template_names = load_template_channels()
    if not template_names:
        print("❌ No template channels loaded, cannot filter")
        return 1
    
    # Download and filter
    if download_and_filter_m3u(m3u_url, template_names, "freetv.m3u"):
        print(f"\n✅ Successfully updated freetv.m3u at {datetime.now()}")
        
        # Get file size for verification
        try:
            file_size = os.path.getsize("freetv.m3u")
            print(f"📊 File size: {file_size:,} bytes")
            
            # Count number of channels in output
            with open("freetv.m3u", 'r', encoding='utf-8') as f:
                content = f.read()
                channel_count = content.count('#EXTINF:')
                print(f"📺 Filtered channels: {channel_count}")
        except Exception as e:
            print(f"⚠️  Could not get file stats: {e}")
        
        return 0
    else:
        print("❌ Failed to update playlist")
        return 1

if __name__ == "__main__":
    exit(main())