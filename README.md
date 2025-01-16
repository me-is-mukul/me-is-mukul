# 🌟 Hey there, I'm Mukul! 👋

![LeetCode Stats](https://leetcard.jacoblin.cool/me_is_mukul_25?theme=dark&font=Karma&ext=heatmap)

---

## 🌐 Connect with me:
<p align="center">
  <a href="https://linkedin.com/in/mukul-aggarwal-377562316/" target="_blank">
    <img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn" width="40"/>
  </a>
  <a href="https://instagram.com/rotten_paintbrush" target="_blank">
    <img src="https://img.icons8.com/color/48/000000/instagram-new.png" alt="Instagram" width="40"/>
  </a>
</p>

---

## 🧠 My Daily Routine in Python:
```python
import datetime, random

def daily_routine():
    # Get current hour
    hour = datetime.datetime.now().hour
    
    # Moods of the day
    moods = [
        "🔥 unstoppable", 
        "💤 sleepy", 
        "🍕 hungry", 
        "🤔 confused", 
        "⚡ energetic", 
        "🌈 inspired"
    ]
    
    # Routine schedule
    schedule = {
        (5, 8): "⏰ Snooze battles",
        (8, 12): "💻 Pretend to work (while procrastinating)",
        (12, 14): "🧠 Problem-solving sprints",
        (14, 18): "😴 Afternoon slump... power nap?",
        (18, 21): "🍽 Dinner and Netflix (or maybe chill)",
        (21, 24): "🧑‍💻 Late-night problem-solving mode",
        (0, 5): "🌌 Why are you still awake?!"
    }
    
    # Match current time to activity
    for (start, end), activity in schedule.items():
        if start <= hour < end:
            mood = random.choice(moods)
            return f"Right now: {activity} | Current mood: {mood}"

# Output today's activity and mood
print(daily_routine())
