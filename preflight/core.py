import asyncio, random, yaml
from dataclasses import dataclass

@dataclass
class ScanResult:
    image_name: str
    critical: int
    high: int
    medium: int
    failed_policy: bool

class PreFlightScanner:
    def __init__(self, config_path="pre-flight-config.yaml"):
        with open(config_path, "r") as f:
            cfg = yaml.safe_load(f)
        self.policy = cfg["pre_flight"]["security_policy"]

    async def scan_image(self, image_name: str):
        print(f"🔍 Scanning {image_name} with mock Qualys...")
        await asyncio.sleep(2)
        result = {
            "critical": random.randint(0, 1),
            "high": random.randint(0, 2),
            "medium": random.randint(0, 3),
        }
        failed = self._evaluate_policy(result)
        return ScanResult(image_name, **result, failed_policy=failed)

    def _evaluate_policy(self, result):
        if self.policy["fail_on_critical"] and result["critical"] > 0:
            return True
        if self.policy["fail_on_high"] and result["high"] > 0:
            return True
        if self.policy["fail_on_medium"] and result["medium"] > 0:
            return True
        return False

