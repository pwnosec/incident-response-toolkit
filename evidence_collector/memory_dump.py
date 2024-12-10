import os

def memory_dump(output_path):
    try:
        os.system(f"sudo dd if=/dev/mem of={output_path} bs=1M")
        print(f"Memory dump saved to {output_path}")
    except Exception as e:
        print(f"Error during memory dump: {e}")
