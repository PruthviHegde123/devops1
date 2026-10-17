import docker

IMAGE_NAME = "flask-apparmor"
CONTAINER_NAME = "flask-apparmor-container"
PROFILE_NAME = "my-apparmor-profile"

client = docker.from_env()

print("Building Docker image...")

image, build_logs = client.images.build(path=".", tag=IMAGE_NAME)

for log in build_logs:
    if "stream" in log:
        print(log["stream"].strip())

print("\nStarting container with AppArmor profile...")

container = None

try:
    container = client.containers.run(
        IMAGE_NAME,
        name=CONTAINER_NAME,
        detach=True,
        ports={"5000/tcp": 5002},
        security_opt=[f"apparmor={PROFILE_NAME}"]
    )

    print("Container started:", container.name)
    container.reload()

    print("\nContainer security options:")
    print(container.attrs["HostConfig"]["SecurityOpt"])

except docker.errors.DockerException as error:
    print("\nContainer could not start.")
    print("Docker reported:", error)

finally:
    if container is not None:
        try:
            container.stop()
            container.remove()
            print("\nContainer stopped and removed.")
        except docker.errors.DockerException as error:
            print("Cleanup warning:", error)
