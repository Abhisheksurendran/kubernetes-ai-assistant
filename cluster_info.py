
from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create Kubernetes API client
v1 = client.CoreV1Api()

# Retrieve nodes
nodes = v1.list_node()

print("\n===== KUBERNETES NODE INFORMATION =====")

for node in nodes.items:
    print("Node:", node.metadata.name)

    for condition in node.status.conditions:
        if condition.type == "Ready":
            print("Ready:", condition.status)


# Retrieve pods from default namespace
pods = v1.list_namespaced_pod(namespace="default")

print("\n===== KUBERNETES POD INFORMATION =====")

for pod in pods.items:
    print("\nPod Name:", pod.metadata.name)
    print("Namespace:", pod.metadata.namespace)
    print("Status:", pod.status.phase)

    ready_count = 0
    total_count = len(pod.status.container_statuses or [])

    for container in pod.status.container_statuses or []:
        if container.ready:
            ready_count += 1

    print("Ready:", f"{ready_count}/{total_count}")

