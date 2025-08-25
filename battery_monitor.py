import time
import psutil
import ctypes

def show_popup(title, message):
    """Show a simple Windows popup dialog"""
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)

def main():
    # Show startup popup once
    show_popup("Battery Monitor", "Battery Monitor is started and running in background.")

    alerted_high = False
    alerted_low = False

    while True:
        battery = psutil.sensors_battery()
        if not battery:
            break  # Exit if no battery found

        percent = battery.percent
        charging = battery.power_plugged

        # If charging and battery is high
        if charging and percent >= 98 and not alerted_high:
            show_popup("Battery Alert", "Turn off charging (Battery ≥ 98%)")
            alerted_high = True
            alerted_low = False  # reset

        # If not charging and battery is low
        if not charging and percent <= 30 and not alerted_low:
            show_popup("Battery Alert", "Start charging (Battery ≤ 30%)")
            alerted_low = True
            alerted_high = False  # reset

        # Reset alerts when conditions go back to normal
        if charging and percent < 98:
            alerted_high = False
        if not charging and percent > 30:
            alerted_low = False

        time.sleep(60)  # check once every 60 seconds (very low CPU usage)


if __name__ == "__main__":
    main()
