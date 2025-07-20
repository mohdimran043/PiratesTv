# IPTV Playlist Auto-Updater

This system automatically updates your `freetv.m3u` playlist file every 5 minutes using GitHub Actions.

## 🚀 Quick Start

### Method 1: Using Config File (Recommended)

1. **Get the M3U Download URL manually:**
   - Visit https://freeiptv2023-d.ottc.xyz/?action=view
   - Wait 8 seconds for the "Create IPTV account" button to be enabled
   - Complete the CAPTCHA if required
   - Click the "Create free IPTV account" button
   - Copy the URL from the `m3uLink` input field

2. **Update the config file:**
   ```bash
   # Edit config.json and paste your M3U URL
   {
     "m3u_download_url": "http://freeiptv.ottc.xyz:80/get.php?username=123456&password=789012&type=m3u_plus&output=ts",
     "update_interval_minutes": 5,
     "last_updated": ""
   }
   ```

3. **Test the update:**
   ```bash
   python update_playlist.py
   ```

### Method 2: Manual Update

If you have a fresh M3U download URL:

```bash
python manual_update.py "http://freeiptv.ottc.xyz:80/get.php?username=123456&password=789012&type=m3u_plus&output=ts"
```

## 🤖 GitHub Actions Auto-Update

The system runs automatically every 5 minutes via GitHub Actions:

- **File:** `.github/workflows/update-playlist.yml`
- **Frequency:** Every 5 minutes (`*/5 * * * *`)
- **Triggers:** 
  - Schedule (every 5 minutes)
  - Manual trigger (workflow_dispatch)
  - Push to main branch (when scripts change)

### How it works:

1. Checks out the repository
2. Sets up Python environment
3. Installs dependencies
4. Runs the update script
5. Commits and pushes changes if the playlist was updated

## 📁 Files

- `update_playlist.py` - Main update script (tries multiple methods)
- `manual_update.py` - Manual update script (requires M3U URL)
- `config.json` - Configuration file (store your M3U URL here)
- `freetv.m3u` - Your IPTV playlist file
- `.github/workflows/update-playlist.yml` - GitHub Action workflow

## 🔧 Configuration

Edit `config.json`:

```json
{
  "m3u_download_url": "YOUR_M3U_URL_HERE",
  "update_interval_minutes": 5,
  "last_updated": "",
  "instructions": {
    "how_to_get_url": [
      "1. Visit https://freeiptv2023-d.ottc.xyz/?action=view",
      "2. Wait 8 seconds for the 'Create IPTV account' button to be enabled",
      "3. Complete the CAPTCHA if required",
      "4. Click the 'Create free IPTV account' button",
      "5. Copy the URL from the m3uLink input field",
      "6. Paste it in the 'm3u_download_url' field above"
    ]
  }
}
```

## 🛠️ Troubleshooting

### Script fails to update:
1. Check if your M3U URL in `config.json` is still valid
2. Get a fresh URL from the website (credentials expire)
3. Check GitHub Actions logs for errors

### GitHub Action fails:
1. Ensure `config.json` has a valid M3U URL
2. Check repository permissions
3. Verify the workflow file syntax

### No channels found:
1. Verify the downloaded M3U file is valid
2. Check if the source website is accessible
3. Try getting a fresh M3U URL

## 📊 Monitoring

The script provides detailed output:
- File size verification
- Channel count
- Last update timestamp
- Error messages and suggestions

Check GitHub Actions logs to monitor automatic updates.

## 🔄 Update Methods (Priority Order)

1. **Config URL** - Uses URL from `config.json`
2. **Extract Credentials** - Extracts from existing `freetv.m3u`
3. **Website Scraping** - Tries to get fresh URL (usually fails due to CAPTCHA)

## 💡 Tips

- Keep your M3U URL updated in `config.json`
- The URL typically contains username/password that may expire
- Monitor GitHub Actions for successful updates
- Use manual update when automatic methods fail

## 🚨 Important Notes

- The source website uses CAPTCHA protection
- M3U URLs may expire and need manual refresh
- GitHub Actions has usage limits (but 5-minute intervals should be fine)
- Always test locally before relying on automation