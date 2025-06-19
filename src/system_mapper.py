import json
import subprocess
import os
import glob
from datetime import datetime

# תיקיות פלאגינים ותוספים ידועות
PLUGIN_DIRECTORIES = [
    '~/Library/Application Support',
    '~/Library/Audio/Plug-Ins',
    '/Library/Application Support',
    '~/Library/PreferencePanes',
    '~/Library/QuickLook',
    '~/Library/Internet Plug-Ins',
    '~/Library/Components',
    '~/Library/Extensions',
    '/Library/Audio/Plug-Ins',
    '/Library/QuickLook',
    '/System/Library/Extensions'
]


def get_applications_via_system_profiler():
    """
    מריץ system_profiler כדי לקבל רשימת תוכנות מותקנות בפורמט JSON.
    """
    try:
        result = subprocess.run(
            ['system_profiler', 'SPApplicationsDataType', '-json'],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode != 0:
            print(f"Error running system_profiler: {result.stderr}")
            return []
            
        data = json.loads(result.stdout)
        applications = []
        
        if 'SPApplicationsDataType' in data:
            for app in data['SPApplicationsDataType']:
                app_info = {
                    'name': app.get('_name', 'Unknown'),
                    'version': app.get('version', 'Unknown'),
                    'location': app.get('path', 'Unknown'),
                    'last_modified': app.get('lastModified', 'Unknown'),
                    'source': 'system_profiler',
                    'type': 'application'
                }
                applications.append(app_info)
                
        return applications
        
    except subprocess.TimeoutExpired:
        print("system_profiler command timed out")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from system_profiler: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error running system_profiler: {e}")
        return []


def scan_plugin_directories():
    """
    סורק תיקיות פלאגינים ותוספים ידועות.
    """
    plugins = []
    
    for plugin_dir in PLUGIN_DIRECTORIES:
        expanded_dir = os.path.expanduser(plugin_dir)
        
        if not os.path.exists(expanded_dir):
            continue
            
        try:
            # סריקה של רמה אחת בלבד (לא רקורסיבית עמוקה)
            for item in os.listdir(expanded_dir):
                item_path = os.path.join(expanded_dir, item)
                
                # דילוג על קבצים רגילים, מתמקדים בתיקיות ופלאגינים
                if os.path.isfile(item_path) and not item.endswith(('.plugin', '.component', '.bundle', '.prefPane')):
                    continue
                    
                try:
                    stat_info = os.stat(item_path)
                    plugin_info = {
                        'name': item,
                        'version': 'Unknown',
                        'location': item_path,
                        'last_modified': datetime.fromtimestamp(stat_info.st_mtime).isoformat(),
                        'source': 'plugin_scan',
                        'type': 'plugin' if os.path.isfile(item_path) else 'plugin_directory'
                    }
                    plugins.append(plugin_info)
                    
                except OSError:
                    # דילוג על קבצים שאין הרשאה לגשת אליהם
                    continue
                    
        except PermissionError:
            # דילוג על תיקיות שאין הרשאה לגשת אליהן
            continue
        except Exception as e:
            print(f"Error scanning {expanded_dir}: {e}")
            continue
            
    return plugins


def map_system_applications():
    """
    פונקציה ראשית שמחברת את כל מקורות המידע ומחזירה רשימה מאוחדת.
    """
    print("Mapping system applications...")
    
    # קבלת תוכנות מ-system_profiler
    applications = get_applications_via_system_profiler()
    print(f"Found {len(applications)} applications via system_profiler")
    
    # קבלת פלאגינים מסריקת תיקיות
    plugins = scan_plugin_directories()
    print(f"Found {len(plugins)} plugins via directory scan")
    
    # איחוד הרשימות
    all_items = applications + plugins
    
    # מיון לפי שם
    all_items.sort(key=lambda x: x['name'].lower())
    
    print(f"Total items mapped: {len(all_items)}")
    return all_items


if __name__ == "__main__":
    # בדיקה מהירה של המודול
    items = map_system_applications()
    for item in items[:5]:  # הדפסת 5 הראשונים לבדיקה
        print(f"{item['name']} - {item['type']} - {item['location']}") 