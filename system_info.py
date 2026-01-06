#!/usr/bin/env python3
import platform
import json
import sys

def get_system_info():
    info = {
        "os": platform.system(),
        "node_name": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine()
    }
    # Add any arguments passed to the script for demonstration
    if len(sys.argv) > 1:
        info["arguments_received"] = sys.argv[1:]
        
    return json.dumps(info, indent=4)

if __name__ == "__main__":
    print(get_system_info())
