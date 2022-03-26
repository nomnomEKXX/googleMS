FROM python:3-slim
WORKDIR /usr/src/app
ENV GOOGLE_MAPS_API_KEY = AIzaSyCd5JgqK3vcSWsx29XrLb7e4BnMjI2rtBw
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./googleMapsAPI.py .
CMD [ "python", "./googleMapsAPI.py" ]
