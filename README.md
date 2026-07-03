# Sports Stats Engine

A NumPy-powered statistics tool for analysing Indian Super League player data. Built as a beginner Python project to practise NumPy, CSV reading, JSON output, and pathlib.

---

## Project Structure

```
sports_stats_engine/
├── players.csv          # 50 players across 6 teams
├── sports_stats.py      # main analysis script
├── README.md            # this file
├── .gitignore
└── outputs/             # created automatically on first run
    └── summary.json     # top 5 players + team averages
```

---

## How to Run

Make sure you have Python and NumPy installed, then run:

```bash
python sports_stats.py
```

The script will:
1. Create the `outputs/` folder if it does not exist
2. Load all 50 players from `players.csv`
3. Print a full five-section report in the terminal
4. Save a JSON summary to `outputs/summary.json`

---

## Requirements

- Python 3.8 or higher
- NumPy

Install NumPy if you don't have it:

```bash
pip install numpy
```

No other third-party packages are needed.

---

## The Data — `players.csv`

50 players spread across 6 teams:

| Team | Players |
|---|---|
| Mumbai FC | 9 |
| Delhi United | 9 |
| Bangalore Rovers | 8 |
| Chennai FC | 8 |
| Hyderabad City | 8 |
| Pune Warriors | 8 |

**Columns:** `name`, `team`, `position`, `goals`, `assists`, `matches`, `pass_accuracy`, `rating`

Stats are position-realistic:
- **Forwards** — high goals (11–22), lower pass accuracy
- **Midfielders** — balanced goals, high assists and pass accuracy
- **Defenders** — few goals, solid passing
- **Goalkeepers** — no goals, lower pass stats

---

## What the Report Shows

| Section | Description |
|---|---|
| 1 | All 50 players sorted by rating (highest first) |
| 2 | Top 5 players by rating |
| 3 | Players above the 75th percentile in goals |
| 4 | Team-by-team average stats comparison |
| 5 | Rating z-scores labelled Above / Average / Below Average |

---

## Python Concepts Practised

| Concept | Where used |
|---|---|
| NumPy arrays | Every numeric column stored as `np.ndarray` |
| Vectorised operations | z-score formula, boolean filtering |
| `np.argsort()` | Ranking players by rating |
| Boolean indexing | Percentile filter, team grouping |
| `np.percentile()`, `np.mean()`, `np.std()` | Statistical calculations |
| `np.column_stack()` | Building the 50×5 stats matrix |
| Axis-based ops (`axis=0`) | League-wide column averages |
| `.reshape()` | Reshaping goals array to a 10×5 grid |
| `csv.DictReader` | Reading players.csv |
| `map()` + `lambda` | Converting string columns to float |
| `pathlib.Path` | Creating the outputs/ folder |
| `json.dump` | Saving the summary file |
| f-strings | All formatted terminal output |
| Docstrings | Every function documented |
| `try/except` | Handling missing CSV file gracefully |

---

## Sample Output (`summary.json`)

```json
{
    "top_5_players": [
        {"rank": 1, "name": "Rakesh Chauhan", "rating": 9.5},
        {"rank": 2, "name": "Pavan Patel",    "rating": 9.2}
    ],
    "team_statistics": {
        "Pune Warriors": {
            "avg_goals": 6.88,
            "avg_assists": 6.5,
            "avg_pass_accuracy": 78.85,
            "avg_rating": 7.64
        }
    }
}
```

---

## Future Improvements

- Add data visualisations with Matplotlib/Seaborn
- Export reports to CSV/PDF in addition to JSON
- Add unit tests for statistical functions
- Build a simple CLI with argument options (e.g. filter by team/position)

---

## Author

**Prajwal Naik**
