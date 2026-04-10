# countdown.py - Event countdown tracker
# Author: Jhosmar
# Date: 2026-04-10

from datetime import date
import time
import os

# file to saved events
EVENTS_FILE = "events.txt"


def load_events():
    """Load events from file"""
    events = {}
    try:
        with open(EVENTS_FILE, "r") as f:
            for line in f:
                if ":" in line:
                    name, date_str = line.strip().split(":", 1)
                    events[name] = date_str
    except FileNotFoundError:
        pass
    return events

# separacion entre funciones
# made for jhosmar
def save_event(events):
    """Save events to file"""
    with open(EVENTS_FILE, "w") as f:
        for name, date_str in events.items():
            f.write(f"{name}:{date_str}\n")

# separacion entre funciones

def add_events(events):
    """Add new event"""
    name = input("Event name: ")
    year = int(input("year (YYYY): "))
    month = int(input("Month (1-12): "))
    day = int(input("Day (1-31): "))

    try:
        event_date = date(year, month, day)
        events[name] = event_date.isoformat()
        save_event(events)
        print(f"✅ Event '{name}' added!")
    except ValueError:
        print("❌ Invalid date. Try again.")

# separacion entre funciones
# made for jhosmar
def show_countdown(events):
    """Show days remaining for each event"""
    if not events:
        print ("No events yet.Add one first")
        return

    today = date.today()
    print ("\n=== COUNTDOWN ===")
    for name, date_str in events.items():
        event_date = date.fromisoformat(date_str)
        days = (event_date - today).days
# separacion
        if days > 0:
            print(f"📅 {name}: {days} days remaining")

        elif days == 0:
            print(f"🎉 {name}:IS TODAY! 🎉")

        else:
            print(f"⏰ {name}: {abs(days)} days ago")
    print ("=" * 20)

# separacion entre funciones
# made for jhosmar

def delete_event(events):
    """delete an events"""
    if not events:
        print ("No events to delete")
        return

# separacion de 4 espacios

    print("\nEvents:")
    for name in events:
        print(f"  - {name}")
    name = input("Event name to delete: ")
    if name in events:
        del events[name]
        save_event(events)
        print (f"✅ '{name}' deleted.")
    else:
        print(f"❌ '{name}' not found.")

# separacion entre funciones
# made for jhosmar

def main():
    events = load_events()

    while True:
        print ("\n=== COUNTDOWN TRACKER ===")
        print ("1 show countdown")
        print ("2 add events")
        print ("3 delete events")
        print ("4 exit")
        option = input("Choose an option: ")

        if option == "1":
            show_countdown(events)
        elif option == "2":
            add_events(events)
        elif option == "3":
            delete_event(events)
        elif option == "4":
            print ("See you later")
            break
        else:
            print ("invalid option. try again ")

        time.sleep(2)



if __name__ == "__main__":
    main()

