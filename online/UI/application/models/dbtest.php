#!/usr/local/bin/php
<?php
$conn = mysql_connect("localhost","root","hello1234");
if (!$conn)
{
    die('Could not connect: ' . mysql_error());
}
print("connect to mysql ok")

// some code

mysql_close($conn);
?>
