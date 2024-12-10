import os

def disk_imaging(device, output_path):
    try:
        os.system(f"sudo dd if={device} of={output_path} bs=64K conv=noerror,sync")
        print(f"Disk image saved to {output_path}")
    except Exception as e:
        print(f"Error during disk imaging: {e}")
