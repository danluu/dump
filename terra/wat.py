import json

parsed = {}

with open('/Users/danluu/dev/dump/terra/filtered_events.json','r') as f:
# with open('/Users/danluu/dev/dump/terra/game-data/2017-05.json','r') as f:
# with open('/Users/danluu/dev/dump/terra/ratings.json','r') as f:
    parsed = json.load(f)
    # print(json.dumps(parsed, indent=2))

print(json.dumps(parsed["4pLeague_S1_D1L1_G4"]["events"]["faction"], indent=2))
