from scapy.all import sniff, wrpcap

def network_capture(interface, output_file):
    packets = sniff(iface=interface, timeout=60)
    wrpcap(output_file, packets)
    print(f"Network traffic saved to {output_file}")
