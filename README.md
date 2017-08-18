# Hoja de Trabajo 4 de Integración

## Microservicio de control de pedidos

Pull from docker hub: 
<br>
`docker pull gar13177/integracion-ht4`
<br>
Update docker hub:
<br>
`docker commit <container-id> gar13177/integracion-ht4`
<br>
`docker push gar13177/integracion-ht4`


Información: 
* Documentación de docker: https://www.docker.com
* Instalación de docker en linux: https://www.docker.com/docker-ubuntu
* Tutorial Django-Docker: https://docs.docker.com/compose/django/
* Información Django Restful: http://www.django-rest-framework.org


Para correr con docker:
<br>
`git pull https://github.com/gar13177/integracion-ht4.git`
<br>
`docker-compose up`

Para correr sin docker:
<br>
`git pull https://github.com/gar13177/integracion-ht4.git`
<br>
`pip install -r requirements.txt`
`python manage.py runserver`

Navegar en el contenedor de docker:
* Correr contenedor de docker
* Ejecutar comando `docker ps`
* Buscar instancia con python (tiene nombre _ht4_web_1_)
* Ejecutar comando `docker exec -it ht4_web_1 bash`
* Para salir del contenedor `exit`


Para correr sin docker:
<br>
`git pull https://github.com/gar13177/integracion-ht4.git`
<br>
`pip install -r requirements.txt`
<br>
`python manage.py runserver`


Más información sobre django y docker:
<br>
https://github.com/erroneousboat/docker-django