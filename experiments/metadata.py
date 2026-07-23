from dataclasses import dataclass
import platform
import sys
from datetime import datetime


@dataclass
class Metadata:

    project = "OpenDMF"

    version = "0.2.0"

    python_version = sys.version

    operating_system = platform.system()

    platform = platform.platform()

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )