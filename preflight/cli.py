import argparse, asyncio
from preflight.core import PreFlightScanner

def main():
    parser = argparse.ArgumentParser(description="Pre-Flight Security Scanner")
    parser.add_argument('--image', required=True, help='Container image name')
    args = parser.parse_args()

    scanner = PreFlightScanner()
    result = asyncio.run(scanner.scan_image(args.image))

    print(f"\n Image: {result.image_name}")
    print(f"Critical: {result.critical}, High: {result.high}, Medium: {result.medium}")
    print("Result:", " FAILED" if result.failed_policy else "PASSED")

    exit(1 if result.failed_policy else 0)

if __name__ == "__main__":
    main()

