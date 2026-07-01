# 🛒 Market Bot
A simple Telegram bot for tracking daily expenses, built with **Python**, **Aiogram 3**, and **SQLAlchemy ORM**.
The bot allows each Telegram user to keep their own expense list, calculate total spending, update records, and remove unnecessary items.
---
🤖 Live Demo
Try it now → @yordamchi_hisobch1_bot


## ✨ Features
- ➕ Add a new expense
- 📋 View all saved expenses
- 💰 Calculate total expenses
- ✏️ Update existing expenses
- ❌ Delete an expense by ID
- 🗑️ Clear the entire expense list
- 🆘 Built-in help command
- 📞 Contact support directly from the bot
- 👤 Separate expense list for every Telegram user
- 💾 SQLite database with SQLAlchemy ORM
---
## 🛠 Built With
- Python 3
- Aiogram 3
- SQLAlchemy ORM
- SQLite
- Telegram Bot API
---
## 📂 Project Structure
```text
market_bot/
│
├── app.py
├── database/
│   ├── db.py
│   ├── models.py
│   └── repository.py
│
├── handlers/
│   ├── routers.py
│   └── start.py
│
├── keyboards/
│   ├── inline.py
│   └── reply.py
│
├── orm.db
└── README.md
```
## 📖 Commands
| Command                   | Description       |
|---------------------------|-------------------|
| `/start`                  | Start the bot     |
| `/reg Product Price`      | Add a new expense |
| `/list`                   | Show all expenses |
| `/del ID`                 | Delete an expense |
| `/update Product Price ID`| Update an expense |
| `/res`                    | Clear all expenses|
| `/help`                   | Show help         |
| `/support`                | Contact support   |
---
## 💡 Example
Add a few expenses:
```text
/reg Bread 5000
/reg Milk 12000
```
View the list:
```text
/list
```
Output:
```text
🐳 Expense List
🔹 Bread
💰 5,000 so'm
(ID: 1)
🔹 Milk
💰 12,000 so'm
(ID: 2)
```
---
## 🗄 Database
The bot uses **SQLite** together with **SQLAlchemy ORM**.
### Table: `market`
| Column  | Type    |
|---------|---------|
| id      | Integer |
| user_id | Integer |
| product | String  |
| cost    | Float   |
Each Telegram user has an independent expense list.
---
## 🚀 Future Improvements
- FSM for multi-step input
- Expense categories
- Monthly statistics
- Charts and analytics
- PostgreSQL support
- Async SQLAlchemy
- Docker support
- Logging
- Unit tests
- Export to Excel/PDF
---
## 👨‍💻 Author
**Muhammadjon**
Telegram: https://t.me/outhumanity 