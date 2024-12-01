import os
import shutil
from pathlib import Path
import keyboard
import time

print(""" $$$$$$\  $$\                         $$\           
$$  __$$\ \__|                        $$ |          
$$ /  \__|$$\ $$$$$$\$$$$\   $$$$$$\  $$ | $$$$$$\  
\$$$$$$\  $$ |$$  _$$  _$$\ $$  __$$\ $$ |$$  __$$\ 
 \____$$\ $$ |$$ / $$ / $$ |$$ /  $$ |$$ |$$$$$$$$ |
$$\   $$ |$$ |$$ | $$ | $$ |$$ |  $$ |$$ |$$   ____|
\$$$$$$  |$$ |$$ | $$ | $$ |$$$$$$$  |$$ |\$$$$$$$\ 
 \______/ \__|\__| \__| \__|$$  ____/ \__| \_______|
                            $$ |                    
                            $$ |                    
                            \__|                    \n\n""")

def clean_roblox_data():
    try:
        local_app_data = os.getenv('LOCALAPPDATA')
        if not local_app_data:
            print("[E] LocalAppData directory not found")
            return False
        roblox_path = Path(local_app_data) / "Roblox"
        if not roblox_path.exists():
            print("[E] Roblox folder not found")
            return False
            
        # Handle logs folder
        logs_path = roblox_path / "logs"
        if logs_path.exists():
            try:
                shutil.rmtree(logs_path)
                print("[S] Successfully deleted logs folder")
            except Exception as e:
                print(f"[E] Error deleting logs folder: {e}")
                return False
                
        # Handle RobloxCookies.dat
        localStorage_path = roblox_path / "LocalStorage"
        cookies_file = localStorage_path / "RobloxCookies.dat"
        
        if cookies_file.exists():
            try:
                os.remove(cookies_file)
                print("[!] Successfully deleted RobloxCookies.dat")
            except Exception as e:
                print(f"[E] Error deleting RobloxCookies.dat: {e}")
                return False
                
        return True
        
    except Exception as e:
        print(f"[E]    An error occurred: {e}")
        return False

if __name__ == "__main__":
    success = clean_roblox_data()
    if success:
        print("[S] All cleanup operations completed successfully")
    else:
        print("[E] Some cleanup operations failed")
    
    print("\n[!] Press ESC to exit...")
    while True:
        if keyboard.is_pressed('esc'):
            break
        time.sleep(0.1)  # Reduce CPU usage cuz ye

# Yippie!!! roblox auth go boom boom
