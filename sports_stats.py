"""
Sports Stats Engine
===================
A NumPy-powered statistics tool for analysing Indian Super League player data.
Built as a beginner Python project to practise NumPy, CSV reading, JSON output, and pathlib.
"""

import csv
import json
import numpy as np
from pathlib import Path



# SETUP


def setup_folders():
    """
    Create the outputs/ directory if it does not already exist.

    Uses pathlib.Path so the path works on any operating system.
    The exist_ok=True flag means no error is raised if the folder
    already exists — safe to call every time the script runs.
    """
    outputs_dir = Path("outputs")
    outputs_dir.mkdir(exist_ok=True)
    print(f"  Folder ready: {outputs_dir.resolve()}")


# DATA LOADING

def load_players(filename):
    """
    Read player data from a CSV file using csv.DictReader.

    Each row becomes a dictionary keyed by the column headers.
    Numeric columns are converted from strings to floats using map()
    and a lambda function so all maths works correctly later.

    Parameters
    ----------
    filename : str
        Path to the CSV file (e.g. 'players.csv').

    Returns
    -------
    list[dict]
        A list where every item is one player's data as a dictionary.
        Numeric fields (goals, assists, matches, pass_accuracy, rating)
        are stored as Python floats. Returns an empty list on error.
    """

    numeric_columns = [
        "goals",
        "assists",
        "matches",
        "pass_accuracy",
        "rating",
    ]

    try:
        players = []

        with open(filename, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:

                float_values = map(
                    lambda value: float(value),
                    [row[col] for col in numeric_columns],
                )

                row.update(zip(numeric_columns, float_values))
                players.append(row)

        print(f"Loaded {len(players)} players from '{filename}'.")
        return players

    except FileNotFoundError:
        print(f"ERROR: '{filename}' was not found.")
        return []
    

# ARRAY BUILDING


def build_arrays(players):
    """
    Convert the list of player dictionaries into separate NumPy arrays.

    Also demonstrates:
      - np.column_stack()
      - axis=0 operations
      - reshape()
    """

    # Text columns
    names = [p["name"] for p in players]
    teams = [p["team"] for p in players]

    # Numeric NumPy arrays
    goals = np.array([p["goals"] for p in players])
    assists = np.array([p["assists"] for p in players])
    matches = np.array([p["matches"] for p in players])
    pass_accuracy = np.array([p["pass_accuracy"] for p in players])
    ratings = np.array([p["rating"] for p in players])

    # Stack all numeric arrays into one matrix
    stats_matrix = np.column_stack(
        [
            goals,
            assists,
            matches,
            pass_accuracy,
            ratings,
        ]
    )

    # Calculate league averages
    league_averages = np.mean(stats_matrix, axis=0)

    stat_labels = [
        "Goals",
        "Assists",
        "Matches",
        "Pass%",
        "Rating",
    ]

    print("\nLeague-Wide Averages")
    print("-" * 40)

    for label, avg in zip(stat_labels, league_averages):
        print(f"{label:<12}: {avg:.2f}")

    # Reshape example
    goals_grid = goals.reshape(10, 5)
    _ = goals_grid

    return (
        names,
        teams,
        goals,
        assists,
        matches,
        pass_accuracy,
        ratings,
    )



# RANKING


def top_players(names, ratings, n=5):
    """
    Return the top n players ranked by rating.
    """

    sorted_indices = np.argsort(ratings)[::-1]
    top_indices = sorted_indices[:n]

    return [
        (names[i], ratings[i])
        for i in top_indices
    ]



# PERCENTILE FILTER


def above_percentile(
    names,
    values,
    metric_name,
    p=75,
):
    """
    Print players above the chosen percentile.
    """

    threshold = np.percentile(values, p)

    names_array = np.array(names)

    mask = values > threshold

    filtered_names = names_array[mask]
    filtered_values = values[mask]

    order = np.argsort(filtered_values)[::-1]

    print(
        f"\nPlayers above {p}th percentile in {metric_name}"
    )

    print(
        f"(Threshold > {threshold:.1f})"
    )

    print(f"\n{'Player':<25}{metric_name}")

    print("-" * 40)

    for name, value in zip(
        filtered_names[order],
        filtered_values[order],
    ):
        print(
            f"{name:<25}{value:.1f}"
        )


# TEAM COMPARISON


def team_comparison(
    players,
    teams,
    goals,
    assists,
    pass_accuracy,
    ratings,
):


# PERCENTILE FILTER

 
 def bove_percentile(names, values, metric_name, p=75):
    """
    Find all players above the given percentile.
    """

    threshold = np.percentile(values, p)

    names_array = np.array(names)

    above_mask = values > threshold

    filtered_names = names_array[above_mask]

    filtered_values = values[above_mask]

    sort_order = np.argsort(
        filtered_values
    )[::-1]

    print(
        f"\nPlayers above the {p}th percentile in "
        f"{metric_name} (>{threshold:.1f})"
    )

    print(f"{'Player':<25}{metric_name:>12}")
    print("-" * 40)

    for name, value in zip(
        filtered_names[sort_order],
        filtered_values[sort_order],
    ):
        print(f"{name:<25}{value:>12.1f}")


# TEAM COMPARISON


def team_comparison(
    players,
    teams,
    goals,
    assists,
    pass_accuracy,
    ratings,
):
    """
    Calculate average statistics for every team.
    """

    teams_array = np.array(teams)

    unique_teams = sorted(
        set(teams)
    )

    team_stats = {}

    print()

    print(
        f"{'Team':<22}"
        f"{'Goals':>10}"
        f"{'Assists':>12}"
        f"{'Pass%':>10}"
        f"{'Rating':>10}"
    )

    print("-" * 66)

    for team_name in unique_teams:

        mask = teams_array == team_name

        avg_goals = np.mean(goals[mask])

        avg_assists = np.mean(assists[mask])

        avg_pass = np.mean(
            pass_accuracy[mask]
        )

        avg_rating = np.mean(
            ratings[mask]
        )

        team_stats[team_name] = {

            "avg_goals":
                round(float(avg_goals), 2),

            "avg_assists":
                round(float(avg_assists), 2),

            "avg_pass_accuracy":
                round(float(avg_pass), 2),

            "avg_rating":
                round(float(avg_rating), 2),
        }

        print(
            f"{team_name:<22}"
            f"{avg_goals:>10.2f}"
            f"{avg_assists:>12.2f}"
            f"{avg_pass:>10.2f}"
            f"{avg_rating:>10.2f}"
        )

    return team_stats

# Z-SCORE


def zscore(values):
    """
    Calculate z-score for every value.
    """

    mean = np.mean(values)

    std = np.std(values)

    return (values - mean) / std



# SAVE SUMMARY


def save_summary(
    filename,
    top5,
    team_stats,
):
    """
    Save report as JSON.
    """

    top5_serialisable = [

        {
            "rank": rank + 1,
            "name": name,
            "rating": round(
                float(rating),
                2,
            ),
        }

        for rank, (name, rating)
        in enumerate(top5)
    ]

    summary = {

        "top_5_players":
            top5_serialisable,

        "team_statistics":
            team_stats,
    }

    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as json_file:

        json.dump(
            summary,
            json_file,
            indent=4,
        )

    print(
        f"\nSummary saved -> {filename}"
    )



# FULL REPORT


def print_full_report(
    names,
    teams,
    goals,
    assists,
    ratings,
    pass_accuracy,
):
    """
    Print complete report.
    """

    divider = "=" * 72

    print()

    print(divider)
    print("SPORTS STATS ENGINE")
    print(divider)

    print(
        "\nSECTION 1 : ALL PLAYERS"
    )

    print("-" * 72)

    print(
        f"{'#':<4}"
        f"{'Name':<25}"
        f"{'Team':<20}"
        f"{'Goals':>6}"
        f"{'Assist':>8}"
        f"{'Pass%':>8}"
        f"{'Rating':>8}"
    )

    print("-" * 72)

    sorted_indices = np.argsort(
        ratings
    )[::-1]

    for rank, idx in enumerate(
        sorted_indices,
        start=1,
    ):

        print(
            f"{rank:<4}"
            f"{names[idx]:<25}"
            f"{teams[idx]:<20}"
            f"{int(goals[idx]):>6}"
            f"{int(assists[idx]):>8}"
            f"{pass_accuracy[idx]:>8.1f}"
            f"{ratings[idx]:>8.1f}"
        )

    print()

    print(divider)

    print(
        "SECTION 2 : TOP 5 PLAYERS"
    )

    print("-" * 40)

    top5 = top_players(
        names,
        ratings,
        n=5,
    )

    for rank, (
        name,
        rating,
    ) in enumerate(
        top5,
        start=1,
    ):

        stars = "*" * int(
            round(rating - 5)
        )

        print(
            f"{rank}. "
            f"{name:<25}"
            f"Rating: {rating:.1f} "
            f"{stars}"
        )

    print()

    print(divider)

    # SECTION 3


    print("SECTION 3 : PLAYERS ABOVE 75th PERCENTILE")
    print("-" * 50)

    above_percentile(
        names,
        goals,
        "Goals",
        p=75,
    )

    print()

    print(divider)

    # SECTION 4


    print("SECTION 4 : TEAM COMPARISON")
    print("-" * 50)

    team_stats = team_comparison(
        None,
        teams,
        goals,
        assists,
        pass_accuracy,
        ratings,
    )

    print()

    print(divider)


    # SECTION 5


    print("SECTION 5 : PLAYER Z-SCORES")
    print("-" * 60)

    print(
        "(z > +0.5 = Above Average | "
        "-0.5 to +0.5 = Average | "
        "z < -0.5 = Below Average)"
    )

    print()

    print(
        f"{'Name':<26}"
        f"{'Rating':>8}"
        f"{'Z-Score':>10}"
        f"   Label"
    )

    print("-" * 60)

    rating_zscores = zscore(
        ratings
    )

    for idx in sorted_indices:

        z = rating_zscores[idx]

        if z > 0.5:
            label = "Above Average"

        elif z < -0.5:
            label = "Below Average"

        else:
            label = "Average"

        print(
            f"{names[idx]:<26}"
            f"{ratings[idx]:>8.1f}"
            f"{z:>+10.2f}"
            f"   {label}"
        )

    print()

    print(divider)
    print("END OF REPORT")
    print(divider)

    return team_stats


# MAIN


def main():
    """
    Entry point for the Sports Stats Engine.
    """

    divider = "=" * 72

    print()
    print(divider)
    print("SPORTS STATS ENGINE - STARTING")
    print(divider)

    # Create outputs folder
    setup_folders()

    # Load player data
    players = load_players("players.csv")

    if not players:
        print("\nNo player data found.")
        return

    # Build NumPy arrays
    (
        names,
        teams,
        goals,
        assists,
        matches,
        pass_accuracy,
        ratings,
    ) = build_arrays(players)

    # Print report
    team_stats = print_full_report(
        names,
        teams,
        goals,
        assists,
        ratings,
        pass_accuracy,
    )

    # Save JSON summary
    top5 = top_players(
        names,
        ratings,
        n=5,
    )

    save_summary(
        "outputs/summary.json",
        top5,
        team_stats,
    )

    print()
    print("Done!")
    print("Open outputs/summary.json to view the saved report.")



# PROGRAM START


if __name__ == "__main__":
    main()