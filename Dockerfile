# Usa la imagen base de Astronomer Runtime
FROM quay.io/astronomer/astro-runtime:11.7.0

# Cambiar a root para la instalación de Google Chrome y dependencias
USER root

# Añadir la llave de Google Chrome y las dependencias necesarias en una sola capa
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        wget \
        gnupg \
        ca-certificates \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* /usr/share/man/* /usr/share/locale/*

# Regresar al usuario original
USER astro

# Configurar Airflow para que escuche en todas las interfaces
CMD ["bash", "-c", "airflow webserver -h 0.0.0.0"]
