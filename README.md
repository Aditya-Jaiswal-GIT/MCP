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

**Last Updated:** August 2024
**Status:** Active Development
