import json
import os
import requests
import random
import string
from datetime import datetime
import re

def generate_random_filename():
    """Generate a random filename for the filtered M3U file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"filtered_{timestamp}_{random_suffix}.m3u"

def load_template_channels():
    """Load channel names from template.m3u"""
    template_path = "template.m3u"
    if not os.path.exists(template_path):
        raise Exception("Template file not found")
    
    channels = []
    with open(template_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#EXTINF:'):
                # Extract channel name from EXTINF line
                match = re.search(r',(.+)$', line)
                if match:
                    channels.append(match.group(1).strip())
    
    return channels

def filter_m3u_content(content, template_channels):
    """Filter M3U content based on template channels"""
    lines = content.split('\n')
    filtered_lines = ['#EXTM3U']
    
    i = 0
    matched_channels = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith('#EXTINF:'):
            # Check if this channel matches any in template
            channel_match = re.search(r',(.+)$', line)
            if channel_match:
                channel_name = channel_match.group(1).strip()
                
                # Check if channel name matches any template channel
                if any(template_channel.lower() in channel_name.lower() or 
                      channel_name.lower() in template_channel.lower() 
                      for template_channel in template_channels):
                    
                    # Add the EXTINF line
                    filtered_lines.append(line)
                    
                    # Add the URL line (next line)
                    if i + 1 < len(lines):
                        url_line = lines[i + 1].strip()
                        if url_line and not url_line.startswith('#'):
                            filtered_lines.append(url_line)
                            matched_channels += 1
                    
                    i += 2  # Skip both lines
                    continue
        
        i += 1
    
    return '\n'.join(filtered_lines), matched_channels

def handler(request):
    """Vercel serverless function handler"""
    try:
        # Handle CORS
        if hasattr(request, 'method') and request.method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type',
                },
                'body': ''
            }
        
        # Parse request body
        if hasattr(request, 'get_json'):
            body = request.get_json()
        elif hasattr(request, 'body'):
            body = json.loads(request.body)
        else:
            # Fallback for different request formats
            body = json.loads(request)
        
        m3u_url = body.get('url')
        
        if not m3u_url:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'URL is required'})
            }
        
        # Load template channels
        template_channels = load_template_channels()
        
        # Download M3U file
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(m3u_url, timeout=30, headers=headers)
        response.raise_for_status()
        
        # Filter content
        filtered_content, channel_count = filter_m3u_content(response.text, template_channels)
        
        # Generate random filename
        filename = generate_random_filename()
        
        # Save filtered file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(filtered_content)
        
        # Get file size
        file_size = os.path.getsize(filename)
        file_size_str = f"{file_size:,} bytes"
        
        # Generate GitHub raw URL (you'll need to set GITHUB_REPOSITORY env var)
        repo = os.environ.get('GITHUB_REPOSITORY', 'yourusername/yourrepo')
        github_raw_url = f"https://raw.githubusercontent.com/{repo}/main/{filename}"
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'success': True,
                'filename': filename,
                'channelCount': channel_count,
                'fileSize': file_size_str,
                'githubRawUrl': github_raw_url
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }