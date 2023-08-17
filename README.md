# Clase GitHub

## Git y GitHub
**Git** es una herramienta de control de versiones que permite rastrear cambios en archivos y colaborar en proyectos de software de manera eficiente. **GitHub** es una plataforma en línea que facilita la gestión de repositorios Git de forma remota y ofrece herramientas adicionales para la colaboración y seguimiento de problemas.

## Comandos
- `git add`: Agrega cambios en los archivos al área de preparación para ser confirmados en el próximo commit.
- `git commit -m 'mensaje'`: Confirma los cambios en el área de preparación con un mensaje descriptivo que explica las modificaciones realizadas.
- `git push -u origin main`: Envía los commits confirmados al repositorio remoto llamado origin, en la rama main. Solo se tiene que escribir una vez.

## Conectarse a Git con SSH

1. **Generar clave SSH:**
   - Ejecutar en la terminal: `ssh-keygen -t rsa -b 4096 -C "<correo>"`

2. **Agregar clave SSH a tu agente:**
   - Iniciar el agente SSH: `eval "$(ssh-agent -s)"`

3. **Copiar clave pública al portapapeles:**

4. **Agregar clave pública a tu cuenta de GitHub:**
   - Iniciar sesión en GitHub.
   - Ir a "Settings" > "SSH and GPG keys".
   - Hacer clic en "New SSH key" y pegar la clave pública.

5. **Configurar URLs remotas en repositorios:**
   - Usar la URL SSH para clonar o cambiar remotamente: `git clone git@github.com:usuario/repo.git`
  

## Markdown cheatsheet
[Markdown cheatsheet](https://www.markdownguide.org/cheat-sheet)


# Bitacora
## Clase 1
Aprendimos a usar git y github, creamos el repositorio

## Clase 2
commit a a.py

## CLase 3
Actualizacion del Readme
