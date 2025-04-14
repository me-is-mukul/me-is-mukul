import matplotlib.pyplot as plt
import matplotlib.patches as patches
import requests
import matplotlib.image as mpimg
import os
USERNAME = "i_am_headache"

def fetch_stats(username):
    url = f"https://api.chess.com/pub/player/{username}/stats"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch stats for {username}. HTTP {response.status_code}")
        return {"Puzzles": 0, "Blitz": 0, "Rapid": 0}

    try:
        data = response.json()
    except ValueError:
        print("Response was not valid JSON.")
        return {"Puzzles": 0, "Blitz": 0, "Rapid": 0}

    return {
        "Puzzles": data.get("tactics", {}).get("highest", {}).get("rating", 0),
        "Blitz": data.get("chess_blitz", {}).get("last", {}).get("rating", 0),
        "Rapid": data.get("chess_rapid", {}).get("last", {}).get("rating", 0),
    }



def generate_chart(stats):
    labels = list(stats.keys())
    values = list(stats.values())

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.set_facecolor("#1e1e1e")  # Dark background
    fig.patch.set_facecolor("#1e1e1e")

    colors = ["#f39c12", "#2980b9", "#2ecc71"]
    icons = {
        "Puzzles": "📘",
        "Blitz": "⚡",
        "Rapid": "🚗"
    }

    # Plot bars
    bars = ax.bar(labels, values, color=colors, edgecolor="white", linewidth=1.5)

    # Add text labels with icons and fake "motion blur" look
    for bar, label, value in zip(bars, labels, values):
        x = bar.get_x() + bar.get_width() / 2
        y = bar.get_height()
        ax.text(x, y + 30, f"{icons[label]} {value}", ha='center', fontsize=13, color="white", fontweight="bold")

    # Set chart settings
    ax.set_title("♟️ Chess.com Stats for i_am_headache", fontsize=16, color="white", pad=20)
    ax.tick_params(colors='white', labelsize=12)
    ax.set_ylim(0, max(values) + 200)
    ax.spines["bottom"].set_color("white")
    ax.spines["left"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig("chess_stats.png", dpi=200)

if __name__ == "__main__":
    stats = fetch_stats(USERNAME)
    generate_chart(stats)
