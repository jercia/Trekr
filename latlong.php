<?php
/*
// http://www.movable-type.co.uk/scripts/latlong.html
var R = 6371000; // metres
var φ1 = lat1.toRadians();
var φ2 = lat2.toRadians();
var Δφ = (lat2-lat1).toRadians();
var Δλ = (lon2-lon1).toRadians();

var a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
        Math.cos(φ1) * Math.cos(φ2) *
        Math.sin(Δλ/2) * Math.sin(Δλ/2);
var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

var d = R * c;

*/

//http://samarthg.people.si.umich.edu/trekr/list.php?Lat=42.280738&Long=-83.7423605
function getDistanceFromLatLonInMi($lat1, $lon1, $lat2, $lon2) {
  $R = 6371000; // Radius of the earth in km
  $theta1 = deg2rad($lat1);
  $theta2 = deg2rad($lat2);
  $dLat = deg2rad($lat2-$lat1);  // deg2rad below
  $dLon = deg2rad($lon2-$lon1); 
  $a = sin($dLat/2) * sin($dLat/2) + cos($theta1) * cos($theta2) * sin($dLon/2) * sin($dLon/2); 
  $c = 2 * atan2(sqrt($a), sqrt(1-$a)); 
  $d = $R * $c; // Distance in km
  return ($d/1000)*0.621371;
}
//echo getDistanceFromLatLonInKm(42.304086, -83.761076, 42.304086, -83.761076);
if (isset($_GET['lat1'])&&isset($_GET['lat2'])&&isset($_GET['long1'])&&isset($_GET['long2'])){
	echo getDistanceFromLatLonInMi($_GET['lat1'], $_GET['long1'], $_GET['lat2'], $_GET['long2']);
}
