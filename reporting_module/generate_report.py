import json

def generate_report(data, template):
    report = template.copy()
    report.update(data)
    with open("incident_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("Report generated successfully!")
