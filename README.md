# Discord Server Administration Bot (Python)

This project is a **Discord administration bot built with Python** using the `discord.py` library.  
It demonstrates how **server-level administrative actions** can be automated via the Discord API.

The bot includes commands that can **modify critical server resources**, such as channels, roles, and server metadata.  
Because of its capabilities, it is intended **only for controlled environments and authorized administrators**.

> ⚠️ **Critical Warning**  
> This bot performs **destructive administrative actions**.  
> Running it without proper authorization may violate **Discord’s Terms of Service** and result in account or server penalties.  
> Use **only on servers you own or explicitly have permission to manage**.

---

## Overview

This project is designed to demonstrate:
- Discord server permission models
- Administrative automation
- Role and channel management via API
- Risks associated with excessive bot permissions

It is useful for:
- Learning Discord bot development
- Understanding server administration APIs
- Security awareness around privilege abuse

---

## Features

- **Delete All Channels**
  - Removes all text and voice channels from the server
- **Create Role**
  - Creates a new role with a specified name
- **Change Server Name**
  - Updates the server’s name dynamically
- **Permission-Based Execution**
  - Requires administrator-level permissions

---

## Requirements

- Python 3.7 or higher
- Discord Bot Token
- `discord.py` library
- Administrator permissions on the target server

---

## Installation

Clone the repository:

```bash
git clone https://github.com/okntscgl/discord-bot.git
cd discord-bot
Install dependencies:

bash
pip install discord.py
Configuration
Create a bot via the Discord Developer Portal

Enable required Gateway Intents

Assign Administrator permissions to the bot

Add your bot token to the script (preferably via environment variables)

Example:

python
TOKEN = "YOUR_DISCORD_BOT_TOKEN"
Usage
Run the bot:

bash
python bot.py
Once the bot is online, authorized administrators can execute commands to:

Delete all channels

Create new roles

Change the server name

⚠️ Strongly recommended:
Test commands on a private test server, not on production communities.

How It Works (High-Level)
Bot Authentication

Connects to Discord using a bot token

Permission Validation

Commands require administrator privileges

Administrative Actions

Executes server modification requests via Discord API

API Enforcement

Discord enforces rate limits and permission checks

Security & Abuse Considerations
This bot highlights:

How dangerous excessive permissions can be

Why bots should follow the principle of least privilege

How compromised bots can lead to full server takeover

Security best practices:

Never grant administrator permissions unnecessarily

Rotate bot tokens regularly

Restrict bot access to trusted environments

Project Structure
bash
.
├── bot.py       # Discord administration bot
├── README.md    # Documentation
Responsible Usage
✔ Use for:

Learning Discord server administration

Testing permission models

Security research in private servers

✖ Do NOT use for:

Server vandalism

Unauthorized access

Public servers without consent

License
This project is licensed under the MIT License.
See the LICENSE file for details.

Final Note
Powerful permissions come with serious responsibility.
Understanding how administrative abuse happens is key to preventing it.
