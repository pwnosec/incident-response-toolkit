def generate_timeline(events):
    timeline = sorted(events, key=lambda x: x['timestamp'])
    return timeline
