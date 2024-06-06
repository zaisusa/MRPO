from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Date:
    id: int
    created_at: datetime
