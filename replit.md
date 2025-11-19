# Discord Bot - Furti (Heists Tracker)

## Overview
A Discord bot that tracks "furti" (heists/thefts) for a gaming community. Users can record their heists, view leaderboards, and track their statistics using Discord slash commands.

**Status**: ✅ Running and operational  
**Bot Name**: BotFurti#4389  
**Last Updated**: November 18, 2025

## Features
- **Slash Commands** (4 total):
  - `/furto <soldi>` - Record a heist with money earned
  - `/classifica` - View leaderboard ranked by total money
  - `/totalefurti` - View personal statistics
  - `/resetfurti` - Clear all heist data

- **Persistent Data Storage** - JSON file-based storage (`furti.json`)
- **User Tracking** - Tracks individual user heists and earnings
- **Leaderboard System** - Ranks users by total dirty money earned

## Project Structure
```
.
├── bot.py              # Main Discord bot application
├── furti.json          # Data storage (auto-generated, gitignored)
├── .gitignore          # Python and data file exclusions
└── replit.md           # This documentation file
```

## Technical Stack
- **Language**: Python 3.11
- **Main Library**: discord.py 2.6.4
- **Storage**: JSON file persistence
- **Hosting**: Replit with workflow automation

## Configuration
- **Discord Token**: Stored securely in Replit Secrets as `DISCORD_TOKEN`
- **Intents**: Default intents (no privileged intents required)
- **Command Prefix**: `!` (not used, slash commands only)

## Data Structure
Each user's data is stored as:
```json
{
  "user_id": {
    "conteggio": 0,    // Number of heists
    "soldi": 0         // Total dirty money earned
  }
}
```

## Recent Changes
- **Nov 18, 2025**: Initial deployment
  - Fixed syntax errors from original code
  - Removed privileged intent requirement
  - Configured secure token management
  - Set up automated workflow

## Running the Bot
The bot runs automatically via the "Discord Bot" workflow executing `python bot.py`. It will:
1. Load heist data from `furti.json` (if exists)
2. Connect to Discord using the token from secrets
3. Sync slash commands
4. Listen for user interactions

## User Preferences
- Language: Italian (all bot messages in Italian)
- Style: Gaming/casual theme with emojis
