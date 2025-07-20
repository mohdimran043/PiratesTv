#!/usr/bin/env python3
"""
Quick deployment test script for M3U Filter Web App
"""

import requests
import json
import os
from datetime import datetime

def test_vercel_deployment():
    """Test if the Vercel deployment is working"""
    print("🧪 Testing Vercel Deployment...")
    print("=" * 50)
    
    # You'll need to update this with your actual Vercel URL after deployment
    vercel_url = "https://vercel.com/mohds-projects-0610fd96"
    
    try:
        # Test 1: Check if the main page loads
        print("📄 Testing main page...")
        response = requests.get(vercel_url, timeout=10)
        if response.status_code == 200:
            print("✅ Main page loads successfully")
        else:
            print(f"❌ Main page failed: {response.status_code}")
            
        # Test 2: Check if API endpoint exists
        print("🔌 Testing API endpoint...")
        api_url = f"{vercel_url}/api/filter"
        response = requests.get(api_url, timeout=10)
        # Should return 405 (Method Not Allowed) for GET requests
        if response.status_code == 405:
            print("✅ API endpoint is accessible")
        else:
            print(f"⚠️ API endpoint response: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")
        print("💡 Make sure to update the vercel_url variable with your actual Vercel URL")

def test_local_filtering():
    """Test the filtering logic locally"""
    print("\n🔧 Testing Local Filtering Logic...")
    print("=" * 50)
    
    try:
        # Check if template file exists
        if os.path.exists("template.m3u"):
            with open("template.m3u", 'r', encoding='utf-8') as f:
                template_content = f.read()
                channel_count = template_content.count('#EXTINF:')
                print(f"✅ Template file found with {channel_count} channels")
        else:
            print("❌ Template file not found")
            
        # Check if API file exists
        if os.path.exists("api/filter.py"):
            print("✅ API filter script found")
        else:
            print("❌ API filter script not found")
            
        # Check if main HTML exists
        if os.path.exists("index.html"):
            print("✅ Main HTML file found")
        else:
            print("❌ Main HTML file not found")
            
    except Exception as e:
        print(f"❌ Error testing local files: {e}")

def test_github_actions():
    """Check GitHub Actions configuration"""
    print("\n🤖 Checking GitHub Actions Configuration...")
    print("=" * 50)
    
    workflows = [
        ".github/workflows/deploy-and-update.yml",
        ".github/workflows/deploy-vercel.yml",
        ".github/workflows/auto-commit.yml"
    ]
    
    for workflow in workflows:
        if os.path.exists(workflow):
            print(f"✅ {workflow} found")
        else:
            print(f"❌ {workflow} missing")

def main():
    print("🎬 M3U Filter Web App - Deployment Test")
    print("=" * 50)
    print(f"🕐 Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Run tests
    test_local_filtering()
    test_github_actions()
    test_vercel_deployment()
    
    print("\n" + "=" * 50)
    print("📋 Next Steps:")
    print("1. Update vercel_url in this script with your actual Vercel URL")
    print("2. Push changes to GitHub to trigger deployment")
    print("3. Check GitHub Actions tab for deployment status")
    print("4. Visit your Vercel URL to test the web app")
    print("5. Set GITHUB_REPOSITORY environment variable in Vercel")

if __name__ == "__main__":
    main()