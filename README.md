# Sports Stats Engine 

A lightweight, NumPy-powered command-line tool for analysing Indian Super League (ISL) player statistics. It reads raw player data from a CSV file, performs a series of statistical computations, prints a formatted console report, and exports a structured JSON summary.

## Features

- **CSV Ingestion** — Loads player records using `csv.DictReader` and safely converts numeric fields to floats.
- **Vectorised Analysis** — Uses NumPy arrays and `column_stack` to compute league-wide averages across all key metrics.
- **Top Player Rankings** — Identifies and ranks the top 5 players by performance rating.
- **Percentile Filtering** — Surfaces standout players above a configurable percentile threshold (default: 75th) for any given metric.
- **Team Comparison** — Aggregates and compares average goals, assists, pass accuracy, and rating across all teams.
- **Z-Score Analysis** — Classifies each player as *Above Average*, *Average*, or *Below Average* relative to the league using standardised z-scores.
- **JSON Export** — Saves a clean, structured summary report (`outputs/summary.json`) for downstream use or integration.

## Project Structure

```
.
├── sports_stats.py     # Main analysis engine
├── players.csv          # Input dataset (player statistics)
└── outputs/
    └── summary.json      # Generated summary report
```

## Requirements

- Python 3.8+
- [NumPy](https://numpy.org/)

Install dependencies with:

```bash
pip install numpy
```

## Usage

1. Place your player dataset in the project root as `players.csv`, using the following columns:

   | Column          | Type   | Description                        |
   |-----------------|--------|-------------------------------------|
   | `name`          | string | Player name                         |
   | `team`          | string | Team name                           |
   | `position`      | string | Playing position                    |
   | `goals`         | float  | Goals scored                        |
   | `assists`       | float  | Assists made                        |
   | `matches`       | float  | Matches played                      |
   | `pass_accuracy` | float  | Pass accuracy (%)                   |
   | `rating`        | float  | Overall performance rating          |

2. Run the script:

   ```bash
   python sports_stats.py
   ```

3. View the console report, or open the generated summary:

   ```bash
   cat outputs/summary.json
   ```





### outputs/summary.json`

```json
{
    "top_5_players": [
        { "rank": 1, "name": "Rakesh Chauhan", "rating": 9.5 },
        { "rank": 2, "name": "Pavan Patel", "rating": 9.2 }
    ],
    "team_statistics": {
        "Mumbai FC": {
            "avg_goals": 6.56,
            "avg_assists": 5.89,
            "avg_pass_accuracy": 75.63,
            "avg_rating": 7.53
        }
    }
}
```

## How It Works

- **Data Loading** — `load_players()` parses the CSV and converts numeric columns using `map()` and a lambda function.
- **Array Construction** — `build_arrays()` transforms player records into NumPy arrays and stacks them into a single matrix for efficient vectorised operations.
- **Statistical Functions** — Modular functions (`top_players`, `above_percentile`, `team_comparison`, `zscore`) each handle a single analytical task, keeping the codebase easy to extend.
- **Reporting** — `print_full_report()` orchestrates all sections into a single formatted console output.
- **Persistence** — `save_summary()` writes the top performers and team statistics to a JSON file in `outputs/`.

## Notes

- The dataset used during development contains 50 ISL player records across 6 teams.
- The `outputs/` directory is created automatically if it doesn't already exist.
- This project was built as a hands-on exercise in NumPy, CSV parsing, and JSON serialisation.

## Author

Prajwal S Naik

GitHub: https://github.com/prajwalnaik98
LinkedIn: www.linkedin.com/in/prajwal-naik-9362b0327
