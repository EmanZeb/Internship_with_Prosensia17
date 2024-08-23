import datetime
import random

# Initialize data storage
entries = []
goals = []
badges = set()

# Mood suggestions
suggestions = {
    'Positive': ['Keep up the good work!', 'Continue with your current activities.'],
    'Negative': ['Try going for a walk.', 'Consider talking to a friend or family member.', 'Engage in a hobby you enjoy.'],
    'Neutral': ['Try something new or different today.', 'Reflect on what you are grateful for.']
}

mood_boosting_tips = [
    "Take a short walk outside.",
    "Listen to your favorite music.",
    "Try meditation or deep breathing exercises.",
    "Write down three things you're grateful for.",
    "Reach out to a friend or loved one."
]

# Add a diary entry
def add_entry(description):
    """Add a diary entry with mood analysis."""
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mood = analyze_sentiment(description)
    entries.append({
        'date': date,
        'description': description,
        'mood': mood
    })
    
    # Check for badges
    award_badges()
    
    print(f"Entry added. Today's mood: {mood}")
    print(f"Suggestion: {', '.join(suggestions.get(mood, ['No suggestions available']))}")

# Add a goal
def add_goal(goal):
    """Add a personal growth goal."""
    goals.append({
        'date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'goal': goal
    })
    print("Goal added.")

# Analyze entries
def analyze_entries():
    """Analyze sentiment and provide suggestions."""
    if not entries:
        print("No entries to analyze.")
        return
    
    for entry in entries:
        mood = entry['mood']
        print(f"Date: {entry['date']}")
        print(f"Sentiment: {mood}")
        print(f"Suggestion: {', '.join(suggestions.get(mood, ['No suggestions available']))}")
        print("-" * 40)

# Simple sentiment analysis function
def analyze_sentiment(text):
    positive_words = {'happy', 'joy', 'love', 'great', 'fantastic', 'good', 'excited'}
    negative_words = {'sad', 'angry', 'hate', 'terrible', 'bad', 'depressed'}
    
    positive_count = sum(word in positive_words for word in text.lower().split())
    negative_count = sum(word in negative_words for word in text.lower().split())
    
    if positive_count > negative_count:
        return 'Positive'
    elif negative_count > positive_count:
        return 'Negative'
    else:
        return 'Neutral'

# View goals
def view_goals():
    """View personal growth goals and progress."""
    if not goals:
        print("No goals set.")
        return
    
    for goal in goals:
        print(f"Date: {goal['date']}")
        print(f"Goal: {goal['goal']}")
        print("-" * 40)

# Award badges based on mood history and goals
def award_badges():
    """Award achievement badges based on user activity."""
    if len(entries) >= 7 and "Consistent Journaler" not in badges:
        badges.add("Consistent Journaler")
        print("You've earned the 'Consistent Journaler' badge for journaling for 7 days!")
    
    positive_moods = [entry['mood'] for entry in entries if entry['mood'] == 'Positive']
    if len(positive_moods) >= 5 and "Positive Streak" not in badges:
        badges.add("Positive Streak")
        print("You've earned the 'Positive Streak' badge for having 5 positive mood entries!")

# Display a random mood-boosting tip
def mood_boosting_tip():
    """Display a random mood-boosting tip."""
    print("Mood-Boosting Tip: " + random.choice(mood_boosting_tips))

# Daily reminders to journal
def daily_reminder():
    """Remind user to journal daily."""
    last_entry_date = datetime.datetime.strptime(entries[-1]['date'], "%Y-%m-%d %H:%M:%S") if entries else None
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    if last_entry_date and last_entry_date.strftime("%Y-%m-%d") != today_date:
        print("Reminder: You haven't added a diary entry today. Don't forget to journal!")

# Mood graphs (text-based visualization)
def mood_graph():
    """Display a simple text-based graph of mood trends."""
    if not entries:
        print("No mood data to display.")
        return
    
    mood_counts = {'Positive': 0, 'Neutral': 0, 'Negative': 0}
    for entry in entries:
        mood_counts[entry['mood']] += 1
    
    print("Mood Graph:")
    for mood, count in mood_counts.items():
        print(f"{mood}: {'*' * count}")

# Main function to interact with the diary
def main():
    """Main function to interact with the personal diary."""
    while True:
        print("1. Add Entry")
        print("2. Analyze Entries")
        print("3. Add Goal")
        print("4. View Goals")
        print("5. View Achievement Badges")
        print("6. Get Mood-Boosting Tip")
        print("7. View Mood Graph")
        print("8. Exit")
        daily_reminder()
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter diary entry: ")
            add_entry(description)
        elif choice == '2':
            analyze_entries()
        elif choice == '3':
            goal = input("Enter personal growth goal: ")
            add_goal(goal)
        elif choice == '4':
            view_goals()
        elif choice == '5':
            print("Achievement Badges: ", ", ".join(badges) if badges else "No badges earned yet.")
        elif choice == '6':
            mood_boosting_tip()
        elif choice == '7':
            mood_graph()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()