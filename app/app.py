import logging
import random
import time
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="../logs/application.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Application events with their corresponding log levels
events = [
    ("INFO", "User login successful"),
    ("INFO", "Product viewed"),
    ("INFO", "Order created successfully"),
    ("INFO", "Payment completed"),
    ("WARNING", "High memory usage detected"),
    ("ERROR", "API request timeout"),
    ("ERROR", "Database connection failed"),
    ("CRITICAL", "Database server unreachable")
]

print("==========================================")
print("   Application Log Generator Started")
print("==========================================")
print("Press Ctrl + C to stop.\n")

try:
    while True:
        # Select a random event
        level, message = random.choice(events)

        # Log the event based on its severity
        if level == "INFO":
            logging.info(message)

        elif level == "WARNING":
            logging.warning(message)

        elif level == "ERROR":
            logging.error(message)

        elif level == "CRITICAL":
            logging.critical(message)

        # Print the event to the console
        print(f"{datetime.now()} | {level:<8} | {message}")

        # Generate a log every 10 seconds
        time.sleep(10)

except KeyboardInterrupt:
    print("\nLog generator stopped.")
