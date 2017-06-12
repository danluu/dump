import json

# with open('/Users/danluu/dev/dump/terra/game-data/2017-05.json','r') as f:
with open('/Users/danluu/dev/dump/terra/ratings.json','r') as f:
    parsed = json.load(f)
    print(json.dumps(parsed, indent=2))
    
