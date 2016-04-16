<?php  
//http://localhost:8888/si-364/w11/trekr/trip.php?TripName=Bird%20Hills%20Nature%20Area&Lat=42.304086&Long=-83.761076
require_once "pdo.php";

$name = $_GET['TripName'];
$lat = $_GET['Lat'];
$long = $_GET['Long'];

$url = "http://api.openweathermap.org/data/2.5/weather?lat=".$lat."&lon=".$long."&appid=9e34a6923ce0275220e44888e5fbd04b";

function k_to_f($temp) {
    if ( !is_numeric($temp) ) { return false; }
    return round((($temp - 273.15) * 1.8) + 32);
}

//http://api.openweathermap.org/data/2.5/weather?lat=42.304086&lon=-83.761076&appid=9e34a6923ce0275220e44888e5fbd04b
$data = json_decode(file_get_contents($url),true);


$stmt = $pdo->prepare('SELECT openHours, bathroom, water, food, season, description FROM Trek WHERE name = :name AND latitude = :lat AND longitude = :long');
$stmt->execute(array( ':name' => $name, ':lat' => $lat, ':long' => $long));
$row = $stmt->fetch(PDO::FETCH_ASSOC);
$row["weather"] = $data["weather"][0]["main"];
$row["temp"] = k_to_f($data["main"]["temp"]);
//var_dump($data);


echo(json_encode($row));
