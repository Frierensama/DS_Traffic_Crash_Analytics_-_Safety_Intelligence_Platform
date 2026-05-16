# Traffic Crash Analytics & Safety Intelligence Platform

This project analyzes traffic crash data using **MySQL** and presents the results in a **Streamlit** dashboard. The goal is to study crash patterns, high-risk locations, crash causes, and time-based trends using SQL queries.

## What this project does

- Loads a cleaned crash dataset into MySQL
- Runs SQL queries for analysis
- Shows the results in tables on a Streamlit dashboard
- Adds short insights for each result

## Tools used

- Python
- MySQL
- Streamlit
- Pandas
- pymysql
- python-dotenv

## Dataset

The dataset contains traffic crash records with details such as:

- crash date and hour
- weather and lighting conditions
- crash type
- street and location information
- injury counts
- contributory causes
- traffic control device information

## Project structure

```bash
Traffic_Crash_Analytics_-_Safety_Intelligence_Platform/
│
├── app.py
├── .env
├── README.md
├── data/
│   └── Traffic_CrashesData.csv
├── scripts/
│   ├── db_create_table.py
│   ├── db_config.py
│   ├── db_insert_data.py
│   └── db_queries.py
└── requirements.txt
```

## Environment variables

Create a `.env` file in the project root with the following values:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password_here
DB_DBNAME=traffic_crash_analysis
CSV_PATH=C:/path/to/your/Traffic_CrashesData.csv
```

Do not commit the `.env` file to GitHub.

## How to run

### 0. Install dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, install the packages manually:

```bash
pip install pandas streamlit pymysql python-dotenv cryptography
```

### 1. Create a python script for database connection

```bash
python scripts/db_config.py
```

### 2. Create table in MySQL

```bash
python scripts/db_create_table.py
```

### 3. Load data into MySQL

```bash
python scripts/db_insert_data.py
```

### 4. Make a script to import the quries and insights

```bash
python scripts/db_queries.py
```

### 5. Start the dashboard

```bash
streamlit run app.py
```

## Analysis included

The dashboard includes analysis for:

1. Dangerous weather and crash-type combinations
2. Streets with the highest injury crashes
3. Injury percentage by crash type
4. Peak crash hour for each month
5. Night-time crash causes
6. Average injuries in daylight vs darkness
7. Traffic control device type with the highest average injuries
8. Crash locations with the highest frequency
9. Streets with the highest injury rate
10. Most common crash type for each year
11. Day of week with the highest average crashes per hour
12. High-risk time slots
13. Top contributing causes for each crash type
14. Year-over-year crash growth rate
15. Hotspot zones using rounded coordinates

## Notes

- All query results are fetched directly from the database.
- The dashboard is built for simple analysis and presentation.
- The `.env` file is used to keep sensitive details out of the code.

## License

bleeh.