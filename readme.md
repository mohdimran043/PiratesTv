# 🎬 M3U Playlist Filter & Web UI

A complete IPTV playlist management system with automatic updates and a beautiful web interface for filtering M3U playlists.

## ✨ Features

### 🌐 Web Interface
- **Dark themed UI** with glassmorphism design
- **Real-time M3U filtering** using your template
- **Random filename generation** for each filtered playlist
- **Direct GitHub raw URLs** for easy sharing
- **Mobile-responsive** design
- **CORS-enabled API** for cross-origin requests

### 🤖 Automated Updates
- **Auto-updates** every 5 minutes via GitHub Actions
- **Template-based filtering** using `template.m3u`
- **Multiple update methods** with fallback options
- **Auto-deployment** to Vercel

## 🚀 Quick Deploy

### Option 1: One-Click Deploy to Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/yourrepo)

### Option 2: Manual Setup

1. **Fork this repository**
2. **Connect to Vercel:**
   - Visit [vercel.com](https://vercel.com)
   - Import your forked repository
   - Deploy automatically

3. **Set Environment Variables in Vercel:**
   ```
   GITHUB_REPOSITORY = yourusername/yourrepo
   ```

4. **Enable GitHub Actions:**
   - Go to repository Settings → Actions → General
   - Enable "Allow all actions and reusable workflows"

## 🎯 How to Use

### Web Interface
1. Visit your deployed Vercel URL
2. Enter any M3U playlist URL
3. Click "Filter & Generate"
4. Get your filtered playlist with GitHub raw URL

### Manual Updates
```bash
# Run manual update with existing config
python manual_update.py

# Or specify a URL directly
python manual_update.py "http://example.com/playlist.m3u"
```

## 📁 Project Structure

```
├── index.html              # Web UI (dark theme)
├── api/filter.py          # Vercel serverless function
├── template.m3u           # Channel filter template
├── manual_update.py       # Manual update script
├── config.json           # Configuration file
├── vercel.json           # Vercel deployment config
├── requirements.txt      # Python dependencies
└── .github/workflows/    # GitHub Actions
    ├── auto-commit.yml   # Auto-commit filtered files
    └── deploy-vercel.yml # Auto-deploy to Vercel
```

## 🔧 Configuration

### Web App Configuration
Edit environment variables in Vercel:
- `GITHUB_REPOSITORY`: Your GitHub repository (username/repo)

### Auto-Update Configuration
Edit `config.json`:
```json
{
  "m3u_download_url": "YOUR_M3U_URL_HERE",
  "update_interval_minutes": 5,
  "last_updated": ""
}
```

### Template Configuration
Edit `template.m3u` to define which channels to filter:
- Add channel names you want to keep
- The filter matches channels containing these names
- Case-insensitive matching

## 🤖 GitHub Actions

### Auto-Commit Workflow
- **File:** `.github/workflows/auto-commit.yml`
- **Frequency:** Every 6 hours
- **Purpose:** Commits generated M3U files to repository

### Vercel Deploy Workflow
- **File:** `.github/workflows/deploy-vercel.yml`
- **Triggers:** Push to main branch
- **Purpose:** Automatically deploys to Vercel on code changes

### Playlist Update Workflow
- **File:** `.github/workflows/update-playlist.yml`
- **Frequency:** Every 5 minutes
- **Purpose:** Updates main playlist files

## 🎨 Web UI Features

- **Glassmorphism Design:** Modern frosted glass effect
- **Gradient Backgrounds:** Beautiful color transitions
- **Smooth Animations:** Hover effects and transitions
- **Loading States:** Visual feedback during processing
- **Error Handling:** User-friendly error messages
- **Copy to Clipboard:** One-click link copying
- **Responsive Layout:** Works on all devices

## 🛠️ API Endpoints

### POST /api/filter
Filters an M3U playlist using your template.

**Request:**
```json
{
  "url": "https://example.com/playlist.m3u"
}
```

**Response:**
```json
{
  "success": true,
  "filename": "filtered_20250720_123456_abc123.m3u",
  "channelCount": 1119,
  "fileSize": "329,795 bytes",
  "githubRawUrl": "https://raw.githubusercontent.com/user/repo/main/filtered_20250720_123456_abc123.m3u"
}
```

## 🔄 Update Methods (Priority Order)

1. **Config URL** - Uses URL from `config.json`
2. **Extract Credentials** - Extracts from existing `freetv.m3u`
3. **Website Scraping** - Tries to get fresh URL (limited by CAPTCHA)

## 🛠️ Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run local server
python -m http.server 8000

# Test manual update
python manual_update.py
```

## 📊 Monitoring

- **GitHub Actions:** Check workflow logs for update status
- **Vercel Dashboard:** Monitor deployment and function logs
- **File Timestamps:** Check last update times in generated files

## 🚨 Important Notes

- M3U URLs may expire and need manual refresh
- Template matching is case-insensitive and partial
- Generated files are automatically committed to repository
- Vercel functions have execution time limits
- GitHub Actions has usage limits for free accounts

## 💡 Tips

- Keep your M3U URL updated in `config.json`
- Monitor GitHub Actions for successful updates
- Use the web interface for one-off filtering
- Check Vercel logs if the API isn't working
- Customize `template.m3u` for your preferred channels

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.