import process_logs as pl

def utest_process_logs():
    """
    unit test to check:
    edge cases
    """
    assert pl.process_logs('', 0) == []
    assert pl.process_logs(["30 99 12"], 2) == []
