docker build -t phototype .
docker run -d --restart unless-stopped -p 3022:3022 --name phototype phototype
docker ps
