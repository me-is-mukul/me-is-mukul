<p align="center">
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=bungee-tint+One&size=50&pause=1000&center=true&vCenter=true&width=1500&height=300&lines=Welcome+to+My+GitHub+Profile;I+am+Mukul+Aggarwal;Loves+To+play+%3CChess+%2F%3E+and+%3CReadingBooks+%2F%3E" alt="Typing SVG" /></a>
</p>

```python
import datetime, random
def daily_routine():
    hour = datetime.datetime.now().hour
    moods = ["energetic", "lazy", "hungry", "confused", "unstoppable", "existential"]
    schedule = {
        (5, 8): "Snooze battle",
        (8, 12): "Pretend to work",
        (12, 14): "Problem solving",
        (14, 18): "Afternoon slump",
        (18, 21): "Dinner and chill",
        (21, 24): "Problem solving",
        (0, 5): "Why are you awake?"
    }
    for (start, end), activity in schedule.items():
        if start <= hour < end:
            return f"{activity}. You're feeling {random.choice(moods)}."
print(daily_routine())


