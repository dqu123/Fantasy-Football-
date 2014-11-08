<?php
/* The login details of hostname, username, password, and
 * database are stored in a login file that should only
 * be read by the server. The file is obviously omitted
 * in github, but one simply needs to add a login.php file
 * in this directory defining
 *     $db_hostname
 *     $db_username
 *     $db_password 
 *     $db_database
 */  
require_once 'login.php';
// Connect to MySQL
$link = mysql_connect($db_hostname, $db_username, $db_password);
if (!$link) {
    die('Could not connect: ' . mysql_error());
}
echo "Connected to MySQL server successfully\n";
mysql_select_db($db_database)
    or die("Unable to select database: " . mysql_error());

// Drop players table if exists 
$query =  "DROP TABLE IF EXISTS players";
$result = mysql_query($query);
if (!$result) {
    die("Database access failed: " . mysql_error());
}

// Create players table 
$query =  "CREATE TABLE players(
    player_id INTEGER AUTO_INCREMENT,
    name VARCHAR(32) NOT NULL,
    position VARCHAR(3) NOT NULL,
    team CHAR(3) NOT NULL, 
    active INTEGER,
    PRIMARY KEY (player_id)
)";
$result = mysql_query($query);
if (!$result) {
    die("Database access failed: " . mysql_error());
}
echo "Players table created succesfully\n";

// Fetch players data from json file
$p_json = file_get_contents('../../json/players.json');
$players = json_decode($p_json); 
$players = $players->{'Players'};
$num_players = count($players);

// Insert players data
$query =  "INSERT INTO players VALUES ";
for ($j = 0; $j < $num_players; ++$j) {
    $query = $query . '(NULL, ' 
    . '\'' . mysql_real_escape_string($players[$j]->displayName) . '\'' . ', '
    . '\'' . mysql_real_escape_string($players[$j]->position)    . '\'' . ', ' 
    . '\'' . mysql_real_escape_string($players[$j]->team)        . '\'' . ', ' 
    . $players[$j]->active . ')';
    if ($j < $num_players - 1) {
        $query = $query . ', ';
    }    
}
$result = mysql_query($query);
if (!$result) {
    die("Database access failed: " . mysql_error());
}

echo "Player data added successfully\n";

// Drop weekly_stats table if exists 
$query =  "DROP TABLE IF EXISTS weekly_stats";
$result = mysql_query($query);
if (!$result) {
    die("Database access failed: " . mysql_error());
}

// Create players table 
$query =  "CREATE TABLE weekly_stats(
	stat_id INTEGER AUTO_INCREMENT,
	week INTEGER NOT NULL,
	name VARCHAR(32) NOT NULL, 
	position VARCHAR(3) NOT NULL,
	standard NUMERIC(12, 2) NOT NULL,
    team CHAR(3) NOT NULL, 
    PRIMARY KEY (stat_id)
)";
$result = mysql_query($query);
if (!$result) {
    die("Database access failed: " . mysql_error());
}
echo "weekly_stats table created succesfully\n";

// Fetch weekly_stats data from json file
for ($i = 0; $i < 10; $i++) {
	$s_json = file_get_contents('../../json/week' . strval($i + 1) . 'all.json');
	$rankings = json_decode($s_json); 
	$rankings = $rankings->{'Rankings'};
	$num_players = count($rankings);
	// Insert players data
	$query =  "INSERT INTO weekly_stats VALUES ";
	for ($j = 0; $j < $num_players; ++$j) {
		$query = $query . '(NULL, '
		. '\'' . mysql_real_escape_string($rankings[$j]->week)    . '\'' . ', ' 
		. '\'' . mysql_real_escape_string($rankings[$j]->{'name'}) . '\'' . ', '
		. '\'' . mysql_real_escape_string($rankings[$j]->position)    . '\'' . ', ' 
		. '\'' . mysql_real_escape_string($rankings[$j]->standard)    . '\'' . ', ' 
		. '\'' . mysql_real_escape_string($rankings[$j]->team)        . '\'' . ')';
		if ($j < $num_players - 1) {
			$query = $query . ', ';
		}    
	}
	$result = mysql_query($query);
	if (!$result) {
		die("Database access failed: " . mysql_error());
	}
}
echo "weekly data added successfully\n";

?>
