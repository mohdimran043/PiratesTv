
# Biggest Pirates IPTV on GitHub

This project is designed to merge and keep up-to-date M3U playlists collected from public sources. It features automated playlist generation, template-based filtering, and manual update capabilities for IPTV streaming.

## 🚀 Features

- **Automated Playlist Generation**: Combines multiple M3U sources with priority ordering
- **Template-Based Filtering**: Filter massive playlists using your custom template
- **Live Channel Validation**: Checks if channels are actually working before including them
- **Manual Updates**: Easy-to-use script for on-demand playlist updates
- **GitHub Actions Integration**: Automated updates via CI/CD pipeline

## 📁 Project Structure

- `generate_playlist.py` - Main script for combining multiple playlist sources
- `manual_update.py` - Template-based filtering and manual updates
- `template.m3u` - Reference template for channel filtering
- `config.json` - Configuration file with download URLs and metadata
- `freetv.m3u` - Filtered output playlist (generated)
- `combinedplaylist.m3u` - Combined playlist from multiple sources

## 🔗 IPTV Sources

This project collects M3U files from multiple public sources:

https://github.com/iptv-org/awesome-iptv?tab=readme-ov-file#providers
https://github.com/search?q=iptv&type=repositories&p=1

### Referenced Repositories:
- https://github.com/ngo5/IPTV
- https://github.com/4gray/iptvnator
- https://github.com/lucifersun/China-Telecom-ShangHai-IPTV-list
- https://github.com/kimcrowing/IPTV
- https://github.com/woniuzfb/iptv
- https://github.com/Moexin/IPTV
- https://github.com/suxuang/myIPTV
- https://github.com/dongyubin/IPTV


<p align="center">

  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Made_With-Python_3.12%2B-blue"
         alt="Python Version">
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify">
    <img src="https://img.shields.io/badge/Made%20in-Bangladesh_🇧🇩-green?colorA=%23ff0000&colorB=%23017e40&style=flat-square"
         alt="Made in Bangladesh">
  </a>
  <a href="https://github.com/FunctionError/PiratesTv/actions/workflows/main.yml">
    <img src="https://github.com/FunctionError/PiratesTv/actions/workflows/main.yml/badge.svg"
         alt="Build Status">
  </a>
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FFunctionError%2FPiratesTv&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Visitors&edge_flat=false"/></a>

![Logo](https://i.ibb.co/nQQn7yx/Pirates-Tv-1.png)


## Authors

- [@FunctionError](https://www.github.com/FunctionError)

### 📺 Join us 👇

[![telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/piratestv_ch)
[![discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/piratestv403)


## Screenshots

![App Screenshot](https://i.ibb.co/ssVqx8c/ssofvlc.png)


## 📺 Playlist Links

Primarily focused on Bangladeshi users (Use VLC for PC)

### Main Combined Playlist:
```bash
https://raw.githubusercontent.com/FunctionError/PiratesTv/main/combined_playlist.m3u
```

### All-in-One Link (Toffee + TSports + M3U):
Use this link for comprehensive coverage 👇 ([Use OTT Navigator for Android](https://t.me/piratestvdb/2))
```bash
https://iptv.piratestv.workers.dev/all
```

### Filtered Playlist (Template-based):
```bash
https://raw.githubusercontent.com/FunctionError/PiratesTv/main/freetv.m3u
```

## 🛠️ Usage Instructions

### Prerequisites
```bash
pip install -r requirements.txt
```

### Manual Update with Template Filtering

The `manual_update.py` script provides intelligent filtering based on your template:

```bash
python manual_update.py
```

**What it does:**
- 📥 Downloads the latest M3U file from the configured source
- 🎯 Filters channels using `template.m3u` as reference
- 💾 Saves filtered results to `freetv.m3u`
- 📊 Provides detailed statistics and progress updates

**Example Output:**
```
🚀 Manual M3U Update with Template Filtering
==================================================
🔗 Source URL: http://freeiptv.ottc.xyz:80/get.php?username=...
📁 Output file: freetv.m3u

📋 Loaded 1,094 channel names from template
📥 Downloading M3U file from source...
✅ Downloaded M3U file successfully
📺 Total channels in downloaded file: 1,241,883
🎯 Filtered channels matching template: 1,119
💾 Filtered playlist saved to: freetv.m3u

✅ Successfully updated freetv.m3u
📊 File size: 329,795 bytes
📺 Filtered channels: 1,119
```

### Automated Playlist Generation

For combining multiple sources with live validation:

```bash
python generate_playlist.py
```

### Configuration

Edit `config.json` to customize:
- M3U download URLs
- Update timestamps
- Channel count tracking

## 🎯 How Template Filtering Works

1. **Template Analysis**: Reads `template.m3u` and extracts all channel names
2. **Source Download**: Downloads the massive source playlist (1M+ channels)
3. **Smart Matching**: Compares channel names (case-insensitive) 
4. **Filtered Output**: Saves only matching channels with updated URLs
5. **Fresh Links**: Ensures all URLs are current and working

# Contributing

Contributions are always welcome! Feel Free To Clone This Project. For Major Changes, Please Open An Issue First To Discuss What You Would Like To Change Or Add, Thank You ! 🖤



# Credits
 <details close>
<summary> See hare 😍

</summary>

This repository collects m3u files collected from multiple public sources. There is no specific source here. If you think the m3u source used in this repository is yours, please open an issue and let us know, we will remove your source. We will always try to give you full credit, because I believe that everyone has the right to showcase their talent to this beautiful world.

   </details>

# Play List sources
 <details close>
<summary> See hare 😍

</summary>


- [@FunctionError](https://www.github.com/FunctionError)

- [@subir](https://github.com/subirkumarpaul/)

- [@HimelOP_Official](@HimelOP_Official)

- ### 

   </details>

# **License**
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://github.com/FunctionError/PiratesTv/blob/main/LICENSE)
