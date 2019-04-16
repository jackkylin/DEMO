FROM python:3.7-slim
RUN apt-get update && apt-get install -y curl xvfb chromium unzip libgconf-2-4
ADD xvfb-chromium /usr/bin/xvfb-chromium
ADD chromedriver_linux64.zip /home/chromedriver_linux64.zip
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser
ENV CHROMEDRIVER_VERSION 2.41
ENV CHROMEDRIVER_SHA256 71eafe087900dbca4bc0b354a1d172df48b31a4a502e21f7c7b156d7e76c95c7
RUN echo "$CHROMEDRIVER_SHA256  /home/chromedriver_linux64.zip" | sha256sum -c - \
    && unzip "/home/chromedriver_linux64.zip" -d /usr/local/bin \
    && rm "/home/chromedriver_linux64.zip"
RUN pip install pytest selenium
WORKDIR /usr/src/app
CMD bash
