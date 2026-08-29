# Remote Expense Tracker

A powerful MCP (Model Context Protocol) server for managing and tracking personal expenses. This project provides async-enabled tools to add, retrieve, and summarize expenses with category-based organization.

## Features

- ✨ **Add Expenses** - Record new expenses with date, amount, category, subcategory, and notes
- 📊 **List Expenses** - Query expenses within a date range with detailed information
- 📈 **Summarize Expenses** - Get expense totals grouped by category
- 🏷️ **Category-Based Organization** - Pre-defined categories (food, transport, housing, utilities, etc.) with subcategories
- ⚡ **Async Database Operations** - Non-blocking SQLite operations using aiosqlite
- 🔒 **Reliable Storage** - WAL (Write-Ahead Logging) mode for robust database management
- 🌐 **MCP Compatible** - Seamlessly integrates with Claude and other MCP clients

## Project Structure

```
remote-expense-tracker/
├── main.py                 # MCP server with expense tracking tools
├── pyproject.toml         # Project configuration and dependencies
├── categories.json        # Pre-defined expense categories and subcategories
├── README.md              # This file
└── src/
    └── remote_expense_tracker/
        └── __init__.py    # Package initialization
```

## Requirements

- Python 3.12 or higher
- pip or uv package manager

## Installation

### Using uv (recommended)

```bash
uv sync
```

### Using pip

```bash
pip install -r requirements.txt
```

### Dependencies

- `fastmcp>=3.4.7` - Model Context Protocol framework
- `aiosqlite>=0.22.1` - Async SQLite driver

## Getting Started

### 1. Activate Virtual Environment

```bash
# On Windows
.venv\Scripts\Activate.ps1

# On macOS/Linux
source .venv/bin/activate
```

### 2. Initialize the Server

```bash
python main.py
```

The server will:
- Initialize an SQLite database at a temporary location
- Create the `expenses` table if it doesn't exist
- Enable WAL mode for reliable concurrent access
- Print the database path to the console

### 3. Connect with MCP Client

Once the server is running, connect it to Claude or your preferred MCP client.

## Available Tools

### 1. `add_expense`

Add a new expense entry to the database.

**Parameters:**
- `date` (string, required) - Date in YYYY-MM-DD format
- `amount` (float, required) - Expense amount
- `category` (string, required) - Expense category
- `subcategory` (string, optional) - Expense subcategory
- `note` (string, optional) - Additional notes

**Example:**
```
add_expense(
  date="2024-08-29",
  amount=45.50,
  category="food",
  subcategory="dining_out",
  note="Lunch with team"
)
```

**Response:**
```json
{
  "status": "success",
  "id": 1,
  "message": "Expense added successfully"
}
```

### 2. `list_expenses`

List all expenses within a date range (inclusive).

**Parameters:**
- `start_date` (string, required) - Start date in YYYY-MM-DD format
- `end_date` (string, required) - End date in YYYY-MM-DD format

**Example:**
```
list_expenses(
  start_date="2024-08-01",
  end_date="2024-08-31"
)
```

**Response:**
```json
[
  {
    "id": 1,
    "date": "2024-08-29",
    "amount": 45.50,
    "category": "food",
    "subcategory": "dining_out",
    "note": "Lunch with team"
  },
  ...
]
```

### 3. `summarize`

Get expense summary grouped by category within a date range.

**Parameters:**
- `start_date` (string, required) - Start date in YYYY-MM-DD format
- `end_date` (string, required) - End date in YYYY-MM-DD format
- `category` (string, optional) - Filter by specific category

**Example:**
```
summarize(
  start_date="2024-08-01",
  end_date="2024-08-31",
  category="food"
)
```

**Response:**
```json
[
  {
    "category": "food",
    "total_amount": 450.75,
    "count": 12
  },
  ...
]
```

## Database Schema

The `expenses` table structure:

```sql
CREATE TABLE expenses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date TEXT NOT NULL,
  amount REAL NOT NULL,
  category TEXT NOT NULL,
  subcategory TEXT DEFAULT '',
  note TEXT DEFAULT ''
)
```

## Expense Categories

The project includes pre-defined categories in `categories.json`:

- **Food** - groceries, dining out, coffee, delivery fees, etc.
- **Transport** - fuel, public transport, cab rides, parking, tolls, etc.
- **Housing** - rent, maintenance, property tax, repairs, etc.
- **Utilities** - electricity, water, internet, phone, etc.
- **Entertainment** - movies, games, subscriptions, hobbies, etc.
- **Shopping** - clothing, electronics, home goods, etc.
- **Healthcare** - medical, pharmacy, fitness, wellness, etc.
- **Personal Care** - salon, grooming, spa, etc.
- **Education** - courses, books, training, etc.
- **Financial** - insurance, taxes, investments, etc.
- **Other** - miscellaneous expenses

## Configuration

### Database Path

The database is stored in your system's temporary directory by default. The path is printed when the server starts:

```
Database path: /tmp/expenses.db  # Linux/macOS
Database path: C:\Users\...\AppData\Local\Temp\expenses.db  # Windows
```

### Modifying Categories

Edit `categories.json` to add or modify expense categories and their subcategories.

## Development

### Running Tests

```bash
# Run with Python
python -m pytest
```

### Code Structure

- `main.py` - Contains the FastMCP server and all tool definitions
- Async/await patterns for non-blocking database operations
- Error handling for database connectivity and permissions

## Troubleshooting

### Database Read-Only Error

If you see "Database is in read-only mode", check:
1. File permissions on the temporary directory
2. Available disk space
3. Antivirus software blocking file access

### Import Errors

Ensure all dependencies are installed:

```bash
uv sync
# or
pip install -r requirements.txt
```

### Database Path Issues

The database path is printed when the server starts. Verify:
1. The path is accessible
2. The directory exists and is writable
3. No other processes are locking the database

## Performance Notes

- Database queries are executed asynchronously to prevent blocking
- WAL mode enables better concurrent access
- Large date ranges may take longer to process; consider querying smaller date windows
- Database is created in a temporary directory for isolation

## Security Considerations

- ⚠️ This is a development-focused tool. For production use:
  - Implement user authentication
  - Add input validation for all parameters
  - Use environment variables for sensitive configuration
  - Encrypt the database file
  - Implement access control lists
  - Add audit logging

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source. See LICENSE file for details.

## Author

**Aditya Jaiswal**
- Email: adibhai212005@gmail.com

## Changelog

### Version 0.1.0
- Initial release
- Core tools: add_expense, list_expenses, summarize
- Category-based organization
- Async SQLite support
- MCP server integration

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

## MCP Integration Guide

### Setting Up the Expense Tracker as an MCP Server

The Remote Expense Tracker can be integrated into Claude Desktop or other MCP-compatible clients. Follow these steps to enable seamless expense tracking within your AI workflow.

### Option 1: Local Development Setup (Recommended for Testing)

1. **Start the MCP Server**
   ```bash
   python main.py
   ```
   The server will output connection details to your terminal.

2. **Configure Claude Desktop**
   - Open Claude Desktop settings (⚙️ icon)
   - Navigate to "Developer" → "MCP Settings"
   - Add this configuration to your `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "expense-tracker": {
         "command": "python",
         "args": ["path/to/main.py"]
       }
     }
   }
   ```
   Replace `path/to/main.py` with the absolute path to your main.py file.

3. **Restart Claude Desktop** for changes to take effect.

### Option 2: Remote Server Setup

To use a deployed MCP server (e.g., hosted on Render or similar):

1. **Update Your MCP Configuration**
   ```json
   {
     "mcpServers": {
       "mcp-expense": {
         "transport": "streamable_http",
         "url": "https://your-deployed-server.onrender.com/mcp"
       }
     }
   }
   ```

2. **Transport Protocol Options**
   - `streamable_http` - Primary protocol, reliable for most deployments
   - `sse` - Server-Sent Events, fallback option if HTTP streaming fails
   - Use `sse` if you encounter timeout or connection issues

3. **Example Configuration** (when deployed to Render)
   ```json
   {
     "mcp-expense": {
       "transport": "streamable_http",
       "url": "https://expense-tracker-st6p.onrender.com/mcp"
     }
   }
   ```

### Option 3: Using with Claude API (via Gateway)

For programmatic access through Claude's API:

```python
from anthropic import Anthropic

client = Anthropic()

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=[
        # MCP tools will be available here
    ],
    messages=[
        {
            "role": "user",
            "content": "Add an expense for $50 on groceries today"
        }
    ]
)
```

### Testing the Integration

Once configured, test with a simple prompt in Claude:

```
Please add an expense of $45.50 for lunch on 2024-08-29 in the food/dining_out category.
```

Claude should execute the `add_expense` tool and confirm the expense was added.

### Troubleshooting MCP Connection

| Issue | Solution |
|-------|----------|
| **"Tool not found" error** | Restart Claude Desktop after updating config, ensure server is running |
| **Connection timeout** | Try switching transport from `streamable_http` to `sse` |
| **"Permission denied"** | Check file permissions on main.py and the database directory |
| **Database locked error** | Ensure only one server instance is running |
| **SSL certificate errors** | For remote servers, ensure proper HTTPS configuration |

### Next Steps

- [Claude MCP Documentation](https://modelcontextprotocol.io)
- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io)
- Explore advanced configurations for production deployments

---

**Last Updated:** August 2024
**Status:** Active Development