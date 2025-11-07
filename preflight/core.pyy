import asyncio, random
from dataclasses import dataclass

@dataclass
class ScanResult:
    image_name: str
    critical: int
    high: int
    medium: int
    failed_policy: bool

class PreFlightScanner:
    async def scan_image(self, image_name: str):
        print(f"🔍 Scanning {image_name} with mock Qualys...")
        await asyncio.sleep(2)
        result = {
            "critical": random.randint(0, 1),
            "high": random.randint(0, 2),
            "medium": random.randint(0, 3),
        }
        failed = result["critical"] > 0 or result["high"] > 1
        return ScanResult(image_name, **result, failed_policy=failed)

