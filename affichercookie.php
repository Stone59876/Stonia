<?php 
session_start();

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
	<title>Affichage du cookie</title>
</head>
<body>
	<p> voici la page que vous voyez Monsieur <?php echo $_SESSION['pseudo'] ?></p>

</body>
</html>
