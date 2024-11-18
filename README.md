# Proyecto de Servidor de Aplicación Multiusuario para Seguimiento de Entrenamientos

Este proyecto consiste en el desarrollo de un servidor de aplicaciones multiusuario que permite a los usuarios registrar y realizar un seguimiento de sus sesiones de entrenamiento. La aplicación generará gráficos para visualizar el progreso de los usuarios y proporcionará recomendaciones sobre el peso que deberían mover en futuros entrenamientos para seguir progresando.

## python verion: 3.12

#### 1. Crear un entorno
```
python3.12 -m venv venv 
```
#### 2. Activar el entorno

```
source venv/bin/activate 
```
#### 3. Instalar dependencias
```
pip install -r requirements.txt 
```
#### 4. Lanzar el servidor
```
uvicorn main:app --reload
```
#### 4.1 Opcion para indicar puerto
```
uvicorn main:app --host 192.168.1.133 --port 9876
```