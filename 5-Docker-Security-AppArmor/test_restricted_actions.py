import docker

IMAGE_NAME = "flask-apparmor"
PROFILE_NAME = "my-apparmor-profile"

client = docker.from_env()

tests = [
    {
        "name": "Read /etc/passwd",
        "command": ["cat", "/etc/passwd"]
    },
    {
        "name": "Run /bin/bash",
        "command": ["/bin/bash", "-c", "echo AppArmor test"]
    }
]

for test in tests:
    print(f"\nTest: {test['name']}")

    try:
        container = client.containers.run(
            IMAGE_NAME,
            command=test["command"],
            detach=True,
            security_opt=[f"apparmor={PROFILE_NAME}"]
        )

        result = container.wait()
        output = container.logs().decode("utf-8", errors="replace")

        print("Exit code:", result["StatusCode"])
        print("Output:", output)

        container.remove()

    except docker.errors.DockerException as error:
        print("Docker error:", error)
