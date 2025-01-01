from distributed.two_phase_commit import TransactionCoordinator

def test_2pc():
    coord = TransactionCoordinator(["db1", "db2"])
    assert coord.execute_transaction({"db1": "YES", "db2": "YES"})
    assert not coord.execute_transaction({"db1": "YES", "db2": "NO"})
