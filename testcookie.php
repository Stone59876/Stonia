<?php

session_start();

$_SESSION['pseudo'] = 'pseudonyme';
$_SESSION['couleur'] = '#ccffcc'

?>

<!DOCTYPE html>
<html>
<head>
	<style>
		body
		{
			background-color:<?php echo $_SESSION['couleur'] ?> 
		}
	</style>
	<title>Test Cookie Entré</title>
</head>
<body>
	<form method="post" action="testcookie.php">
		<input type="text" name="pseudo">
		<input type="submit" name="Valider">
		<input type="color" name="couleur">
	</form>

</body>
</html>

<?php 
if ( isset($_SESSION['pseudo']) and isset($_POST['pseudo']) )
{
	$_SESSION['pseudo'] = $_POST['pseudo'];
	echo $_POST['pseudo'];
	echo '  ';
	echo $_SESSION['pseudo'];
}
else
{
	echo 'erreur';
}

if ( isset($_SESSION['couleur']) and isset($_POST['couleur']) )
{
	$_SESSION['couleur'] = $_POST['couleur'];
	?>
	<style>
		body
		{
			background-color:<?php echo $_SESSION['couleur'] ?> 
		}
	</style>
	<a href="affichercookie.php">Cliquez ici pour voir la page</a>
	<?php
}
else
{
	echo "couleur de base";
}
?>


