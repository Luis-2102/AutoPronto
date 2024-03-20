<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Recoge los datos del formulario
    $name = strip_tags(trim($_POST["name"]));
    $name = str_replace(array("\r","\n"),array(" "," "),$name);
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $message = trim($_POST["message"]);

    // Verifica que los campos obligatorios no estén vacíos
    if (empty($name) || empty($email) || empty($message)) {
        http_response_code(400);
        echo "Por favor completa todos los campos del formulario.";
        exit;
    }

    // Configura la dirección de destino
    $recipient = "lalomoto21@gmail.com";

    // Configura el asunto del correo
    $subject = "Nuevo mensaje de $name";

    // Construye el contenido del correo
    $email_content = "Nombre: $name\n";
    $email_content .= "Email: $email\n\n";
    $email_content .= "Mensaje:\n$message\n";

    // Construye los encabezados del correo
    $email_headers = "From: $name <$email>";

    // Envía el correo
    if (mail($recipient, $subject, $email_content, $email_headers)) {
        // Cambios para depuración
        echo "Gracias! Tu mensaje ha sido enviado.";
    } else {
        // Cambios para depuración
        http_response_code(500);
        echo "Lo sentimos, ha ocurrido un error al enviar tu mensaje. Por favor intenta de nuevo más tarde.";
    }

} else {
    http_response_code(403);
    echo "Hubo un problema con tu envío. Por favor intenta de nuevo.";
}

