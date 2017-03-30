FROM logstash:5.2

# Install Ruby toolchain
RUN apt update
RUN apt install -y ruby ruby-dev git

# Clone mqtt plugin
WORKDIR /app
# RUN git clone https://github.com/johnalla0/logstash-input-mqtt.git
RUN git clone https://github.com/CanTireInnovations/logstash-input-mqtt.git /app

# Build Logstash plugin
RUN gem build ./logstash-input-mqtt.gemspec

# Add your logstash plugins setup here
RUN logstash-plugin install ./logstash-input-mqtt-0.0.2.gem
