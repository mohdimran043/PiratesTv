# M3U Filter Web UI Setup Guide

## 🚀 Deploy to GitHub Pages + Vercel

### Option 1: Deploy to Vercel (Recommended)

1. **Fork this repository** to your GitHub account

2. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Sign up/login with your GitHub account
   - Click "New Project"
   - Import your forked repository
   - Deploy (Vercel will auto-detect the configuration)

3. **Set Environment Variables in Vercel:**
   - Go to your project settings in Vercel
   - Add environment variable:
     - `GITHUB_REPOSITORY`: `yourusername/yourreponame`

4. **Enable GitHub Actions:**
   - Go to your repository settings
   - Navigate to Actions → General
   - Enable "Allow all actions and reusable workflows"

### Option 2: GitHub Pages + External API

1. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: main / (root)

2. **For the API, you'll need a separate service** (Vercel, Netlify, or your own server)

## 🎯 How It Works

1. **User enters M3U URL** in the web interface
2. **API downloads** the M3U file from the provided URL
3. **Filters channels** using your `template.m3u` file
4. **Generates random filename** and saves the filtered playlist
5. **Returns GitHub raw URL** for direct access to the filtered file

## 🔧 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally (for testing)
python -m http.server 8000
```

## 📁 File Structure

```
├── index.html              # Web UI (dark theme)
├── api/filter.py          # Vercel serverless function
├── template.m3u           # Channel filter template
├── vercel.json           # Vercel configuration
├── requirements.txt      # Python dependencies
└── .github/workflows/    # Auto-commit workflow
```

## 🎨 Features

- **Dark themed UI** with glassmorphism design
- **Real-time filtering** based on template
- **Random filename generation** for each filtered playlist
- **Direct GitHub raw URLs** for easy sharing
- **Auto-commit workflow** to keep files in repository
- **Responsive design** works on mobile and desktop

## 🔗 Usage

Once deployed, users can:
1. Visit your Vercel URL
2. Enter any M3U playlist URL
3. Get a filtered playlist with only channels from your template
4. Receive a direct GitHub raw link to download the filtered file

## 🛠️ Customization

- Edit `template.m3u` to change which channels are filtered
- Modify `index.html` to customize the UI
- Update `api/filter.py` to change filtering logic