import os

# 1. Define the folders where Mac keeps built-in apps
folders_to_check = [
    "/System/Applications", 
    "/System/Applications/Utilities"
]

print("---  MAC PREINSTALLED SOFTWARE DISCOVERY ---")

# 2. Loop through each folder
for folder in folders_to_check:
    print(f"\n📂 Checking: {folder}")
    
    try:
        # Get a list of everything in that folder
        apps = os.listdir(folder)
        
        # 3. Sort them alphabetically
        apps.sort()
        
        for app in apps:
            # Only show things that end in ".app" (ignore hidden system files)
            if app.endswith(".app"):
                # Clean up the name (remove '.app')
                clean_name = app.replace(".app", "")
                print(f"  🚀 {clean_name}")
                
    except FileNotFoundError:
        print(f"  ❌ Could not find folder: {folder}")

print("\n--- END OF LIST ---")
