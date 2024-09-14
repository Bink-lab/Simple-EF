import os
import shutil
import psutil
import time
import keyboard

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

def kill_process(process_name):
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and process_name.lower() in proc.info['name'].lower():
                proc.kill()
                print(f"[+] Terminated process: {proc.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def delete_folder(folder_path):
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f"[+] Deleted folder: {folder_path}")
        except Exception as e:
            print(f"[!] Error deleting folder: {e}")
    else:
        print(f"[!] Folder not found: {folder_path}")

if __name__ == "__main__":
    # Terminate processes
    kill_process("Bloxstrap")
    kill_process("RobloxPlayerBeta.exe")

    # Give the system a moment to terminate the processes
    time.sleep(3)

    # Path to the Roblox folder in LOCALAPPDATA
    local_app_data = os.getenv('LOCALAPPDATA')
    roblox_folder = os.path.join(local_app_data, 'Roblox')

    # Specify subfolders to delete
    local_storage_folder = os.path.join(roblox_folder, 'LocalStorage')
    logs_folder = os.path.join(roblox_folder, 'Logs')

    # Delete the subfolders
    delete_folder(local_storage_folder)
    delete_folder(logs_folder)

print("\nPress esc to exit...")
keyboard.wait("Esc")
