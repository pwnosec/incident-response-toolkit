from evidence_collector.memory_dump import memory_dump
from evidence_collector.disk_imaging import disk_imaging
from analysis_engine.ioc_detection import check_iocs
from reporting_module.generate_report import generate_report

def main():
    print("Starting the Incident Response Toolkit...")
    print("Collecting memory dump...")
    memory_dump("/tmp/memory_dump.img")
    print("Memory dump complete.")

    print("Collecting disk image...")
    disk_imaging("/dev/sda", "/tmp/disk_image.img")
    print("Disk imaging complete.")

    print("Checking IOCs...")
    iocs = ["malicious_ip", "bad_hash"]
    detected = check_iocs(iocs, "test data")
    print(f"IOCs detected: {detected}")

    print("Generating report...")
    generate_report({"ioc_matches": detected}, {"title": "Incident Report"})
    print("Report generation complete.")

if __name__ == "__main__":
    main()
