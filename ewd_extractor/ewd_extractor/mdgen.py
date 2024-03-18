import json
import sys

def generate_ewd_markdown(entries):
    entries = entries['entries']
    return "\n\n".join([ f'[{entry["title"]}]({entry["link"]})' for entry in entries ])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Required argument: ewd json filename.', file=sys.stderr)
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        entries_json = json.load(open(filename))
    except FileNotFoundError:
        print(f'EWD json file {filename} not found.')
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f'Failed to decode EWD json: {e}')
        sys.exit(1)
    
    print(generate_ewd_markdown(entries_json))