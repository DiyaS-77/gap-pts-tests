<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">

<html>

<head>

<title>PTS Execution Report</title>

<style>

body {
    font-family: Arial;
    background-color: #f2f2f2;
}

table {
    border-collapse: collapse;
    width: 90%;
    margin: 20px;
}

th {
    background-color: #333;
    color: white;
    padding: 10px;
}

td {
    padding: 8px;
    border: 1px solid #ccc;
}

.pass {
    color: green;
    font-weight: bold;
}

.fail {
    color: red;
    font-weight: bold;
}

.indcsv {
    color: orange;
    font-weight: bold;
}

</style>

</head>

<body>

<h2>PTS Execution Report</h2>

<h3>Execution Summary</h3>

<table>

<tr>
<th>Project</th>
<th>Total</th>
<th>Passed</th>
<th>Failed</th>
<th>Inconclusive</th>
</tr>

<tr>

<td>
<xsl:value-of select="PTSExecutionReport/ExecutionInfo/Project"/>
</td>

<td>
<xsl:value-of select="PTSExecutionReport/ExecutionInfo/Total"/>
</td>

<td>
<xsl:value-of select="PTSExecutionReport/ExecutionInfo/Passed"/>
</td>

<td>
<xsl:value-of select="PTSExecutionReport/ExecutionInfo/Failed"/>
</td>

<td>
<xsl:value-of select="PTSExecutionReport/ExecutionInfo/Inconclusive"/>
</td>

</tr>

</table>

<h3>Test Cases</h3>

<table>

<tr>
<th>Test Case</th>
<th>Verdict</th>
<th>Failure Reason</th>
</tr>

<xsl:for-each select="PTSExecutionReport/TestCases/TestCase">

<tr>

<td>
<xsl:value-of select="TestCaseID"/>
</td>

<td>

<xsl:attribute name="class">

<xsl:choose>

<xsl:when test="Verdict='PASS'">pass</xsl:when>
<xsl:when test="Verdict='FAIL'">fail</xsl:when>
<xsl:otherwise>indcsv</xsl:otherwise>

</xsl:choose>

</xsl:attribute>

<xsl:value-of select="Verdict"/>

</td>

<td>
<xsl:value-of select="FailureReason"/>
</td>

</tr>

</xsl:for-each>

</table>

</body>

</html>

</xsl:template>

</xsl:stylesheet>
