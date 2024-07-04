# magical_academy

En el Reino del Trébol, el Rey Mago necesita un sistema para la academia de magia
que administre el registro de solicitud de estudiantes y la asignación aleatoria de
sus Grimorios. Los Grimorios se clasifican según el tipo de trébol en la portada, y
los estudiantes según sus afinidades mágicas específicas.

Endpoints Requeridos: 
 POST /solicitud: Envía solicitud de ingreso.
 PUT /solicitud/{id}: Actualiza solicitud de ingreso.
 PATCH /solicitud/{id}/estatus: Actualiza estatus de solicitud. 
 GET /solicitudes: Consulta todas las solicitudes. 
 GET /asignaciones: Consulta asignaciones de Grimorios. 
 DELETE /solicitud/{id}: Elimina solicitud de ingreso.

Datos Requeridos en la Solicitud:
 Nombre: solo letras, máximo 20 caracteres. 
 Apellido: solo letras, máximo 20 caracteres.
 Identificación: números y letras, máximo 10 caracteres.
 Edad: solo números, 2 dígitos. 
 Afinidad Mágica: Una única opción entre Oscuridad, Luz, Fuego, Agua, Viento o Tierra. 

## Para iniciar el programa, primero instalamos docker desktop

https://www.docker.com/products/docker-desktop/

## Segundo, clonamos el repositorio

git clone https://github.com/nfernandez97/magical_academy.git

## Tercero, corremos el siguiente comando dentro de la carpeta de nuestro proyecto 

docker-compose up -d 

Una vez realizados estos 3 pasos, nos dirigimos a localhost:3000 donde estará alojada nuestra UI 


## Adicionalmente

podemos dirigirnos a localhost:8000/docs donde podemos ver de manera detallada los endpoints que utiliza esta API 