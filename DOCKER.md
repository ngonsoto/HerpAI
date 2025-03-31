## 🐳 Docker container

Follow these steps to run HerpAI inside a docker container.

### 1. Clone the repository

```bash
git clone https://github.com/openbiocure/HerpAI.git
cd HerpAI
```

### 2. Build the docker image

```bash
docker build -t herpai-app .
```

### 3. Configure environment variables

Create a `.env` file in the project root with your API keys:

```bash
echo "SONNET_API_KEY={your-sonnet-api-key-here}" > .env
echo "OPENAI_API_KEY={your-openai-api-key-here}" >> .env
```

### 4. Run the docker container

Using the built image and the environment variables, run the container:

```bash
sudo docker run -it --env-file .env -p 5000:8080 -v /tmp:/app/output herpai-app
```

The application will be accesible at `http://localhost:5000`. The output files will be saved to `/tmp` directory. Change the port and/or directory mounted as required.

