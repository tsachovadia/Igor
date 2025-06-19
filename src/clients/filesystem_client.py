import os
import time
from tqdm import tqdm

# רשימת תיקיות שיש לדלג עליהן ("רועשות"/לא רלוונטיות)
BLACKLIST_DIRS = [
    'Library/Caches', 'Library/Containers', 'Library/Logs', 'Library/Application Support/Google',
    'Library/Application Support/Spotify', 'Library/Safari', 'Library/Mail', 'Library/CloudStorage',
    'Library/Group Containers', 'Library/Preferences', 'Library/Suggestions', 'Library/Accounts',
    'Library/Keychains', 'Library/IdentityServices', 'Library/PersonalizationPortrait',
    'Library/Assistant', 'Library/Autosave Information', 'Library/Developer', 'Library/Metadata',
    'Library/Saved Application State', 'Library/HTTPStorages', 'Library/Widgets', 'Library/Calendars',
    'Library/Messages', 'Library/Reminders', 'Library/SyncedPreferences', 'Library/Screen Savers',
    'Library/ColorPickers', 'Library/ColorSync', 'Library/Components', 'Library/Compositions',
    'Library/Contextual Menu Items', 'Library/Extensions', 'Library/FontCollections', 'Library/Fonts',
    'Library/Internet Plug-Ins', 'Library/Keyboard Layouts', 'Library/LaunchAgents', 'Library/LaunchDaemons',
    'Library/PreferencePanes', 'Library/Printers', 'Library/QuickLook', 'Library/Receipts', 'Library/ScriptingAdditions',
    'Library/Spelling', 'Library/Spotlight', 'Library/StartupItems', 'Library/Voices', 'Library/WebKit',
    '.Trash', '.git', '.DS_Store', '__pycache__', 'venv', 'node_modules', 'tmp', 'temp', 'cache', 'Caches',
    'System', 'private', 'dev', 'Volumes', 'Network', 'bin', 'sbin', 'cores', 'opt', 'usr', 'etc', 'var',
]

HOME_DIR = os.path.expanduser('~')


def is_blacklisted(path):
    rel_path = os.path.relpath(path, HOME_DIR)
    for b in BLACKLIST_DIRS:
        if rel_path.startswith(b) or os.path.basename(path) == b:
            return True
    return False


def scan_filesystem_bfs(root_dir=HOME_DIR, max_depth=6):
    """
    סורק את מערכת הקבצים (BFS) עם סינון חכם ומחזיר מבנה נתונים מקונן.
    """
    queue = [(root_dir, 0)]
    result = {
        'name': os.path.basename(root_dir),
        'path': root_dir,
        'type': 'directory',
        'children': [],
        'size': 0,
        'last_modified': os.path.getmtime(root_dir)
    }
    path_to_node = {root_dir: result}
    pbar = tqdm(total=1, desc='Scanning filesystem', unit='dir')
    scanned = set()

    while queue:
        current_path, depth = queue.pop(0)
        if current_path in scanned or is_blacklisted(current_path):
            continue
        scanned.add(current_path)
        try:
            entries = os.listdir(current_path)
        except Exception:
            continue
        pbar.total += len(entries)
        pbar.update(1)
        for entry in entries:
            full_path = os.path.join(current_path, entry)
            try:
                stat = os.stat(full_path)
            except Exception:
                continue
            node = {
                'name': entry,
                'path': full_path,
                'size': stat.st_size,
                'last_modified': stat.st_mtime
            }
            if os.path.isdir(full_path):
                node['type'] = 'directory'
                node['children'] = []
                if depth < max_depth:
                    queue.append((full_path, depth + 1))
            else:
                node['type'] = 'file'
            path_to_node[current_path]['children'].append(node)
            path_to_node[full_path] = node
    pbar.close()
    return result 