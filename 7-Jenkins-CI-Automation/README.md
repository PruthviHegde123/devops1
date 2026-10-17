# Exercise 7: Jenkins CI Automation

## Aim
To understand Continuous Integration and Jenkins automation.

## Tools Required
- Docker Desktop
- Jenkins
- PowerShell
- Git and GitHub

## Theory
Continuous Integration (CI) involves frequently integrating code changes into a shared repository and verifying them through automated builds and tests.

Jenkins is an open-source automation server used to automate software building, testing, and deployment tasks.

## Procedure
1. Start Docker Desktop.
2. Run Jenkins using Docker.
3. Retrieve the initial administrator password.
4. Open http://localhost:8080/.
5. Enter the password to unlock Jenkins.
6. Install suggested plugins.
7. Create the administrator account.
8. Complete the setup wizard.
9. Verify the Jenkins dashboard.

## Important Commands
- docker ps
- docker ps -a
- docker logs jenkins --tail 30
- docker start jenkins
- docker stop jenkins

## Result
Jenkins was installed and configured using Docker. The setup wizard was completed, and the Jenkins dashboard was accessed successfully.

## Screenshots
Store screenshots of the Jenkins setup and dashboard in the screenshots directory.

## Conclusion
This exercise demonstrated the installation and configuration of Jenkins using Docker for local Continuous Integration.

## References
- https://www.jenkins.io/
- https://www.jenkins.io/doc/
- https://docs.docker.com/
