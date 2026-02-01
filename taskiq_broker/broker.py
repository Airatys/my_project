from taskiq_nats import NatsBroker, PullBasedJetStreamBroker

# broker = NatsBroker(servers="nats://127.0.0.1:4222", queue="taskiq_queue")
broker = PullBasedJetStreamBroker(servers="nats://127.0.0.1:4222", queue="taskiq_queue")