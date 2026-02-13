import xml.etree.ElementTree as ET
from datetime import datetime


def generate_pts_xml_report(results, project, output_file="pts_execution_report.xml"):
    """
    Generates PTS-style XML execution report.

    Args:
        results: list of dict
        project: project name
        output_file: output XML file path
    """

    root = ET.Element("PTSExecutionReport")
    execution_info = ET.SubElement(root, "ExecutionInfo")
    ET.SubElement(execution_info, "Project").text = project
    ET.SubElement(execution_info, "ExecutionTime").text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = len(results)
    passed = sum(1 for r in results if r["verdict"] == "PASS")
    failed = sum(1 for r in results if r["verdict"] == "FAIL")
    indcsv = sum(1 for r in results if r["verdict"] == "INDCSV")
    ET.SubElement(execution_info, "Total").text = str(total)
    ET.SubElement(execution_info, "Passed").text = str(passed)
    ET.SubElement(execution_info, "Failed").text = str(failed)
    ET.SubElement(execution_info, "Inconclusive").text = str(indcsv)

    testcases = ET.SubElement(root, "TestCases")

    for result in results:

        tc = ET.SubElement(testcases, "TestCase")

        ET.SubElement(tc, "TestCaseID").text = result["testcase"]
        ET.SubElement(tc, "Date").text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ET.SubElement(tc, "Verdict").text = result["verdict"]
        ET.SubElement(tc, "FailureReason").text = result["reason"] or ""

    tree = ET.ElementTree(root)

    ET.indent(tree, space="  ")

    tree.write(output_file, encoding="utf-8", xml_declaration=True)

    return output_file
