# Docker ELK Stack
Credit to [deviantony/docker-elk](https://github.com/deviantony/docker-elk) for a great starting point.

## Setup
Run this script:

```bash
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo/docker.repo
sudo yum install -y docker-ce python-pip git
sudo systemctl enable docker
sudo systemctl start docker
sudo pip install -U docker-compose
git clone https://github.com/rhefner1/docker-elk-iot.git
sudo sysctl -w vm.max_map_count=262144
```

## Usage

Start the ELK stack using *docker-compose*:

```bash
$ docker-compose up -d
```

Now that the stack is running, you'll want to inject logs in it. Try running `scripts/send_message.py` which publishes the message to RabbitMQ. Logstash then receives the message and drops it into Elasticsearch, where it can be viewed with Kibana.

You can access Kibana UI by hitting [http://localhost:5601](http://localhost:5601) with a web browser.

By default, the stack exposes the following ports:
- 5000: Logstash TCP input.
- 9200: Elasticsearch HTTP
- 9300: Elasticsearch TCP transport
- 5601: Kibana
- 5672: RabbitMQ

## Restarting Services
- If you edit any of the configuration files or mess something up, you'll need to restart the services by following these steps:
  - Run `sudo docker-compose stop`
  - Run `sudo docker-compose build`
  - Run `sudo docker-compose up -d`
- If you want to erase all Elasticsearch data, run this command while services are stopped: `sudo rm -rf /es-data`
