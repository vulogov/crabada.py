from typing import List
from src.libs.CrabadaWeb2Client.types import CrabForLending


class CrabBlacklist:
    """
    Keep track of blacklisted crabs
    """

    def __init__(self) -> None:
        self.blacklist: List[CrabForLending] = []

    def append(self, crab: CrabForLending) -> List[CrabForLending]:
        """
        Add a crab to the blacklist
        """
        self.blacklist.append(crab)
        return self.blacklist

    def remove(self, crab: CrabForLending) -> List[CrabForLending]:
        """
        Remove a crab from the blacklist
        """
        self.blacklist.remove(crab)
        return self.blacklist

    def isBlacklisted(self, crab: CrabForLending) -> bool:
        """
        Returns true if the given crab is in the blacklist
        """
        crabs = [c for c in self.blacklist if c["crabada_id"] == crab["crabada_id"]]
        return len(crabs) > 0
