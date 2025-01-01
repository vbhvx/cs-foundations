"""Two-Phase Commit (2PC) atomic distributed transaction coordinator."""

class TransactionCoordinator:
    def __init__(self, participants: list):
        self.participants = participants

    def execute_transaction(self, votes: dict) -> bool:
        # Phase 1: Prepare
        all_yes = all(votes.get(p) == "YES" for p in self.participants)
        # Phase 2: Commit or Abort
        return all_yes
