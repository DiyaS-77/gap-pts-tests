import os
from datetime import datetime


def generate_pts_text_report(project, results, output_dir="reports"):
    """
    Generate simple text table report for PTS execution.
    """

    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{project}_PTS_Report_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)

    total = len(results)
    passed = sum(1 for r in results if r["verdict"] == "PASS")
    failed = sum(1 for r in results if r["verdict"] == "FAIL")
    inconclusive = sum(1 for r in results if r["verdict"] == "INDCSV")

    with open(filepath, "w") as f:

        f.write("===========================================================\n")
        f.write("                PTS EXECUTION REPORT\n")
        f.write("===========================================================\n\n")

        f.write(f"Project         : {project}\n")
        f.write(f"Execution Time  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("Summary\n")
        f.write("-----------------------------------------------------------\n")
        f.write(f"Total           : {total}\n")
        f.write(f"Passed          : {passed}\n")
        f.write(f"Failed          : {failed}\n")
        f.write(f"Inconclusive    : {inconclusive}\n\n")

        f.write("Detailed Results\n")
        f.write("-----------------------------------------------------------\n")
        f.write(f"{'Index':<8}{'Test Case ID':<25}{'Verdict':<12}{'Failure Reason'}\n")
        f.write("-----------------------------------------------------------\n")

        for i, r in enumerate(results, 1):

            reason = r["reason"] if r["reason"] else ""

            f.write(f"{i:<8}{r['testcase']:<25}{r['verdict']:<12}{reason}\n")

        f.write("\n===========================================================\n")

    return filepath
