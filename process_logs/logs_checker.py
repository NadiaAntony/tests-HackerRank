import process_logs as pl
import utest_process_logs as upl

print("running unit tests..")
upl.utest_process_logs()

logs = ["30 99 12", "30 20 1", "12 100 2", "20 80 22"]
threshold = 2
print("running for case threshold="+str(threshold)+", logs=" +str(logs))
result=pl.process_logs(logs, threshold)
print("IDs with trancations above threshold "+str(result))
