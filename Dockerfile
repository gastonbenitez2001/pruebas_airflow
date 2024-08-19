FROM quay.io/astronomer/astro-runtime:11.7.0

# Cambiar a root para instalar Google Chrome
USER root

# Instalar las dependencias necesarias y Google Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# Regresar al usuario original
USER astro