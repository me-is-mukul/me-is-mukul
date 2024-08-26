<p align="center">
    <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Tilt+Prism&size=30&pause=1000&color=0FF75B&center=true&vCenter=true&width=800&height=80&lines=HI...+I+am+Mukul+Aggarwal;Welcome+to+my+GitHub+profile;Loves+%3C%2F+chess%3E+and+%3C%2F+readingBooks%3E" alt="Typing SVG" /></a>
</p>

<p align="center">
    <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Tilt+Prism&size=30&pause=1000&color=F70000FF&center=true&vCenter=true&width=800&height=80&lines=Updates.." alt="Typing SVG" /></a>
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


