from datetime import datetime
import os

def generate_pts_table_report(project, results, output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{project}_PTS_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join(output_dir, filename)
    total = len(results)
    passed = sum(1 for r in results if r["verdict"] == "PASS")
    failed = sum(1 for r in results if r["verdict"] == "FAIL")
    inconclusive = sum(1 for r in results if r["verdict"] == "INDCSV")
    with open(filepath, "w") as f:
        f.write("="*60 + "\n")
        f.write("PTS EXECUTION REPORT\n")
        f.write("="*60 + "\n\n")
        f.write(f"Project         : {project}\n")
        f.write(f"Execution Time  : {datetime.now()}\n\n")
        f.write("Summary\n")
        f.write("-"*60 + "\n")
        f.write(f"Total testcases : {total}\n")
        f.write(f"Passed          : {passed}\n")
        f.write(f"Failed          : {failed}\n")
        f.write(f"Inconclusive    : {inconclusive}\n\n")
        f.write("Detailed Results\n")
        f.write("-"*60 + "\n")
        f.write(f"{'Index':<6} {'Test Case ID':<30} {'Verdict':<10} {'Failure Reason'}\n")
        f.write("-"*60 + "\n")
        for idx, r in enumerate(results, 1):
            reason = r["reason"] if r["reason"] else "-"
            f.write(f"{idx:<6} {r['testcase']:<30} {r['verdict']:<10} {reason}\n")
        f.write("\n" + "="*60 + "\n")
    return filepath
