# Proyecto de Servidor de Aplicación Multiusuario para Seguimiento de Entrenamientos

Este proyecto consiste en el desarrollo de un servidor de aplicaciones multiusuario que permite a los usuarios registrar y realizar un seguimiento de sus sesiones de entrenamiento. La aplicación generará gráficos para visualizar el progreso de los usuarios y proporcionará recomendaciones sobre el peso que deberían mover en futuros entrenamientos para seguir progresando.

```
uvicorn main:app --reload
uvicorn main:app --host 192.168.1.133 --port 9876
```