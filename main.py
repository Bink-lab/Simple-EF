import os
import shutil
import logging
from pathlib import Path
import keyboard
import time

print(""" ____ ___ __  __ ____  _     _____
/ ___|_ _|  \/  |  _ \| |   | ____|
\___ \| || |\/| | |_) | |   |  _|
 ___) | || |  | |  __/| |___| |___
|____|___|_|  |_|_|   |_____|_____|\n\n""")

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def clean_roblox_data():
    """Clean up Roblox data"""
    try:
        # Get LocalAppData directory
        local_app_data = os.getenv('LOCALAPPDATA')
        if not local_app_data:
            logging.warning("LocalAppData directory not found")
            return False

        # Construct Roblox path
        roblox_path = Path(local_app_data) / "Roblox"

        # Log Roblox path construction
        logging.info(f"Constructing Roblox path: {roblox_path}")

        # Check if Roblox folder exists
        if not roblox_path.exists():
            logging.warning("Roblox folder not found")
            return False

        # Handle logs folder
        logs_path = roblox_path / "logs"
        if logs_path.exists():
            try:
                # Log log deletion attempt
                logging.info(f"Deleting logs folder: {logs_path}")
                shutil.rmtree(logs_path)
                logging.success("Successfully deleted logs folder")
            except Exception as e:
                # Log error deleting logs folder
                logging.error(f"Error deleting logs folder: {e}")
                return False

        # Handle RobloxCookies.dat
        localStorage_path = roblox_path / "LocalStorage"
        cookies_file = localStorage_path / "RobloxCookies.dat"

        if cookies_file.exists():
            try:
                # Log cookie file deletion attempt
                logging.info(f"Deleting RobloxCookies.dat: {cookies_file}")
                os.remove(cookies_file)
                logging.success("Successfully deleted RobloxCookies.dat")
            except Exception as e:
                # Log error deleting RobloxCookies.dat
                logging.error(f"Error deleting RobloxCookies.dat: {e}")
                return False

        return True

    except Exception as e:
        # Log any other errors that occur during cleanup
        logging.error(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    success = clean_roblox_data()

    if success:
        logging.success("All cleanup operations completed successfully")
    else:
        logging.warning("Some cleanup operations failed")

    print("\n[!] Press ESC to exit...")
    while True:
        if keyboard.is_pressed('esc'):
            break
        time.sleep(0.1)  # Reduce CPU usage cuz ye

# Yippie!!! roblox auth go boom boom