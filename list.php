<?php  
//http://samarthg.people.si.umich.edu/trekr/list.php?lat=42.280738&long=-83.7423605
require_once "pdo.php";
require_once "latlong.php";

$stmt = $pdo->prepare('SELECT name, imageList, address, length, duration, level, season, longitude, latitude FROM Trek');
$stmt->execute();
$retval = array();

$lat = $_GET['Lat'];//42.304086;
$long = $_GET['Long'];//-83.761076;

while ( $row = $stmt->fetch(PDO::FETCH_ASSOC) ) {
    $row["distance"] = intval(10*getDistanceFromLatLonInMi($lat, $long, $row["latitude"], $row["longitude"]))/10;
    $row["imageList"] = explode(",", $row["imageList"]);
    //$row["season"] = explode(",", $row["season"]);
    $retval[] = $row;
}
$obj=array();
$obj["hikes"] = $retval;

echo(json_encode($obj));
