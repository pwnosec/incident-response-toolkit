import os

def memory_dump(output_path):
    try:
        print("Attempting memory dump using dd...")
        result = os.system(f"sudo dd if=/dev/mem of={output_path} bs=1M")
        if result != 0:
            print("Error: Failed to execute memory dump. Check system compatibility or permissions.")
        else:
            print(f"Memory dump saved to {output_path}")
    except Exception as e:
        print(f"Exception during memory dump: {e}")
