<body onload="window.print()">
<?php
//require('fpdf.php');
//$pdf = new FPDF();
//$pdf->AddPage();
//$output=shell_exec('python file.py');
//$pdf->SetFont('Arial','B',25);
//$pdf->Cell(120,30,'Malayalam Digital Representation is:');
//$pdf->Cell(50,55,$output);
//$pdf->Output();
$output=shell_exec('python file.py');
echo "<center><h1><pre>";
echo "Malayalam Digital Representation is:";
print_r($output);
echo "</pre></h1></center>";
file_put_contents("file.txt", "");
?>
</body>