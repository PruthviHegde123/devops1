# Exercise 5: Docker Security with AppArmor

## Aim
To explore how AppArmor can provide additional security restrictions for Docker containers.

## Tools Used
- Docker Desktop
- Docker
- Python
- Flask
- Docker SDK for Python
- AppArmor
- Ubuntu on WSL2

## Files
- `app.py` - Flask web application.
- `Dockerfile` - Builds the Flask Docker image.
- `my-apparmor-profile` - AppArmor profile created for the experiment.
- `apply_apparmor.py` - Builds the image and starts a container with the requested security option.
- `test_restricted_actions.py` - Tests access to `/etc/passwd` and execution of `/bin/bash`.
- `outputs/` - Stores command output and test results.
- `screenshots/` - Stores screenshots captured during execution.

## Procedure
1. Created a Flask application that listens on port 5000.
2. Created a Dockerfile using Python 3.8-slim and Flask.
3. Built the Docker image named `flask-apparmor`.
4. Created an AppArmor profile for the experiment.
5. Ran the Python script to build the image and start a container with the requested AppArmor security option.
6. Inspected the container security options.
7. Tested reading `/etc/passwd` and executing `/bin/bash`.
8. Checked AppArmor support in the WSL2 environment.

## Results
- The Docker image was built successfully.
- The Flask application returned the expected response when tested on host port 5001.
- The Python script successfully started a container with the requested security option recorded as `apparmor=my-apparmor-profile`.
- The restricted-action tests both returned exit code 0. Reading `/etc/passwd` succeeded, and `/bin/bash` executed successfully.
- The WSL2 environment reported AppArmor disabled (`N`), and `apparmor_parser` was unavailable in the Docker Desktop environment checked.
- In Ubuntu on WSL2, the AppArmor parser was installed, but the AppArmor filesystem was not mounted.
- The runtime AppArmor profile reported by Docker was blank during inspection.

The results do not demonstrate that the intended AppArmor restrictions were enforced. Docker accepting the requested security option alone does not prove that the profile was active.

## Output Files
- `outputs/apply-apparmor-output.txt`
- `outputs/restricted-actions-output.txt`
- `outputs/docker-images.txt`
- `outputs/containers-output.txt`
- `outputs/flask-logs.txt`
- `outputs/security-options.txt`

## Screenshots
Practical screenshots are stored in the `screenshots/` directory.

## Conclusion
The Flask application and Docker image were created and tested successfully. The AppArmor profile was supplied as a requested container security option, but the current WSL2 environment did not demonstrate successful AppArmor enforcement. A compatible environment with AppArmor enabled is required to verify that the intended restrictions block the tested actions.
