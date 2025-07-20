# 🚀 Vercel Auto-Deployment Setup Guide

This guide will help you set up automatic deployment to Vercel using GitHub Actions.

## 📋 Prerequisites

- GitHub repository (this one!)
- Vercel account (free tier works)
- Basic understanding of environment variables

## 🔧 Step-by-Step Setup

### 1. Create Vercel Account & Project

1. **Sign up at [vercel.com](https://vercel.com)** using your GitHub account
2. **Import your repository:**
   - Click "New Project"
   - Select your forked repository
   - Click "Deploy" (Vercel will auto-detect the configuration)

### 2. Vercel Credentials (Already Configured!)

✅ **Good news!** Your Vercel credentials are already configured in the deployment scripts:
- **Vercel Token:** `OatPNpDygWF6Fvy6KfVYiypQ`
- **Team ID:** `team_y7MAfsqbHwuAchO2PZzTK6kV`

No need to set up GitHub secrets - everything is ready to go!

### 3. Configure Environment Variables in Vercel

1. **Go to your Vercel project dashboard**
2. **Navigate to Settings → Environment Variables**
3. **Add the following variables:**

   | Variable Name | Value | Environment |
   |---------------|-------|-------------|
   | `GITHUB_REPOSITORY` | `yourusername/yourrepo` | Production |

### 4. Test the Setup

1. **Trigger a deployment:**
   - Push a change to your main branch, OR
   - Go to Actions tab → "Deploy & Update System" → "Run workflow"

2. **Check the results:**
   - Monitor the GitHub Actions workflow
   - Check your Vercel dashboard for deployment status
   - Visit your Vercel URL to test the web app

## 🎯 What Happens Now?

### Automatic Deployments
- **Every push to main branch** triggers a Vercel deployment
- **Every 30 minutes** the playlist gets updated
- **Generated M3U files** are automatically committed to your repo

### Manual Deployments
- Use GitHub Actions "Run workflow" button
- Or push changes to trigger deployment

## 🛠️ Troubleshooting

### Deployment Fails
1. **Check GitHub Secrets:**
   - Ensure `VERCEL_TOKEN` is valid
   - Verify `VERCEL_PROJECT_ID` is correct
   - Check `VERCEL_ORG_ID` if using a team

2. **Check Vercel Settings:**
   - Ensure `GITHUB_REPOSITORY` environment variable is set
   - Verify project is connected to the correct GitHub repo

3. **Check GitHub Actions Logs:**
   - Go to Actions tab in your repository
   - Click on the failed workflow
   - Review the error messages

### Web App Not Working
1. **Check Vercel Function Logs:**
   - Go to Vercel dashboard → Functions tab
   - Check for runtime errors

2. **Verify Template File:**
   - Ensure `template.m3u` exists in your repository
   - Check that it contains valid channel names

3. **Test API Endpoint:**
   - Visit `https://yourapp.vercel.app/api/filter` directly
   - Should return a method not allowed error (normal for GET requests)

## 🎉 Success Indicators

✅ **GitHub Actions workflow completes successfully**
✅ **Vercel deployment shows "Ready" status**
✅ **Web app loads at your Vercel URL**
✅ **API responds to POST requests**
✅ **Filtered M3U files appear in your repository**

## 🔄 Updating Your Setup

### To Update the Web App:
1. Modify `index.html` or `api/filter.py`
2. Push changes to main branch
3. GitHub Actions will auto-deploy to Vercel

### To Update Filtering:
1. Modify `template.m3u` with your preferred channels
2. Changes take effect immediately for new requests

### To Change Update Frequency:
1. Edit `.github/workflows/deploy-and-update.yml`
2. Modify the cron schedule (currently every 30 minutes)

## 💡 Pro Tips

- **Monitor your Vercel usage** to stay within free tier limits
- **Use meaningful commit messages** for easier tracking
- **Test locally first** before pushing major changes
- **Keep your template.m3u updated** with current channel names
- **Check GitHub Actions regularly** to ensure updates are working

## 🆘 Need Help?

If you encounter issues:
1. Check the troubleshooting section above
2. Review GitHub Actions logs for error details
3. Check Vercel function logs for runtime errors
4. Ensure all secrets and environment variables are set correctly

Your M3U Filter Web App should now be fully automated and deployed! 🎉