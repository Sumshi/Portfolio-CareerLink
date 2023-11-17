<?php
// This provides the functionality of email so that we can receive messages.

// Store the name that we will receive.
$name = $_POST['name'];

// Store the visitor's email that we will receive.
$visitor_email = $_POST['email'];

// Store the message that we will receive.
$subject = $_POST['subject'];
$message = $_POST['message'];

$email_from = 'maya@sumaya.me'; // my domain

$email_subject = 'any message'; // Add a semicolon here

$email_body = "User Name: $name.\n" .
              "User Email: $visitor_email.\n" .
              "Subject: $subject.\n" .
              "User Message: $message.\n";

$to = "sumayasomow@gmail.com";

$headers = "From: $email_from \r\n";

$headers .= "Reply-To: $visitor_email \r\n"; // Replace the period with a semicolon

mail($to, $email_subject, $email_body, $headers);

header("Location: contact.html");
?>
