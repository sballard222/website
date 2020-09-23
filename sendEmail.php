<?php
$data = [];
if ($_POST) {
    $name = "";
    //$phone = "";
    $email = "";
    //$subject = "";
    $comments = "";
    $recipient="m.oboudi@yahoo.com"; // Your email comes here

    if (isset($_POST['name'])) {
        $name = $_POST['name'];
    }
    
    // if (isset($_POST['phone'])) {
    //     $phone = filter_var($_POST['phone'], FILTER_SANITIZE_STRING);
    // }

    if (isset($_POST['email'])) {
        $email = str_replace(array("\r", "\n", "%0a", "%0d"), '', $_POST['email']);
        $email = filter_var($email, FILTER_VALIDATE_EMAIL);
    }

    // if (isset($_POST['subject'])) {
    //     $subject = $_POST['subject'];
    // }

    if (isset($_POST['comments'])) {
        $comment = htmlspecialchars($_POST['comments']);
        $comments = $comment.'<br>Name is: '.$name/*.'<br>Phone number is: '.$phone*/;
    }


    $headers = 'MIME-Version: 1.0' . "\r\n"
        . 'Content-type: text/html; charset=utf-8' . "\r\n"
        . 'From: ' . $email . "\r\n";
    if (mail($recipient, /*$subject,*/ $comments, $headers)) {
        $data = array(
            'status' => 'Congratulation',
            'message' => 'Your message sent successfully.'
        );
    } else {
        $data = array(
            'status' => 'Error',
            'message' => 'Your message did not send.'
        );
    }
} else {
	$data = array(
		'status' => 'Warning',
		'message' => 'Something went wrong, Please try again.'
	);
}
echo json_encode($data);