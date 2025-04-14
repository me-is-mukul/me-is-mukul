import requests
import matplotlib.pyplot as plt

USERNAME = "i_am_headache"

def fetch_stats(username):
    url = f"https://api.chess.com/pub/player/{username}/stats"
    response = requests.get(url)
    data = response.json()

    return {
        "Bullet": data.get("chess_bullet", {}).get("last", {}).get("rating", 0),
        "Blitz": data.get("chess_blitz", {}).get("last", {}).get("rating", 0),
        "Rapid": data.get("chess_rapid", {}).get("last", {}).get("rating", 0),
    }

def generate_chart(stats):
    labels = list(stats.keys())
    values = list(stats.values())

    plt.figure(figsize=(6, 4))
    bars = plt.bar(labels, values, color=["#f39c12", "#2980b9", "#27ae60"])
    plt.title(f"♟️ Chess.com Ratings for {USERNAME}", fontsize=14)
    plt.ylim(0, max(values) + 200)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.1, yval + 25, int(yval), fontsize=12)

    plt.tight_layout()
    plt.savefig("chess_stats.png")

if __name__ == "__main__":
    stats = fetch_stats(USERNAME)
    generate_chart(stats)
