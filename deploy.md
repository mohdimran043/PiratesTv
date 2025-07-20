# 🚀 Quick Deploy Guide

## Step 1: Fork & Setup Repository
1. Fork this repository to your GitHub account
2. Go to repository Settings → Actions → General
3. Enable "Allow all actions and reusable workflows"

## Step 2: Deploy to Vercel
1. Visit [vercel.com](https://vercel.com) and sign in with GitHub
2. Click "New Project" → Import your forked repository
3. Deploy (Vercel auto-detects the configuration)

## Step 3: Configure Environment
In Vercel project settings, add environment variable:
- **Key**: `GITHUB_REPOSITORY`
- **Value**: `yourusername/yourreponame` (replace with your actual repo)

## Step 4: Test Your App
1. Visit your Vercel URL (e.g., `yourproject.vercel.app`)
2. Enter an M3U URL to test filtering
3. Get your filtered playlist with GitHub raw URL

## 🎯 Your App Features:
- ✨ Dark themed UI with glassmorphism design
- 🎬 Real-time M3U playlist filtering
- 🔗 Direct GitHub raw URLs for sharing
- 📱 Mobile-responsive design
- 🤖 Auto-commit workflow for file management

## 🔧 Customization:
- Edit `template.m3u` to change filtered channels
- Modify `index.html` for UI customization
- Update `api/filter.py` for filtering logic changes

That's it! Your M3U filter service is now live and ready to use! 🎉