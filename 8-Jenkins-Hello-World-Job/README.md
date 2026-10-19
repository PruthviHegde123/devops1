# Exercise 8: Hello World Jenkins Job

## Aim
To create and execute a Jenkins Freestyle job that retrieves a shell script from GitHub and displays Hello, Jenkins! in the build console.

## Objectives
- Understand Jenkins Freestyle projects.
- Integrate Jenkins with a GitHub repository.
- Execute a shell script through a Jenkins build.
- Verify build results using Console Output.

## Tools Required
- Jenkins
- Docker Desktop
- Git
- GitHub
- Web browser
- PowerShell

## Theory
Jenkins is an automation server used to automate software development tasks. A Freestyle project allows users to configure build steps through the Jenkins interface.

GitHub hosts the source code repository. Jenkins can retrieve the source code from GitHub and execute configured build steps.

## Procedure
1. Start Docker Desktop and ensure Jenkins is running.
2. Create a shell script named hello-world.sh.
3. Add the command echo "Hello, Jenkins!" to the script.
4. Upload the script to the GitHub repository.
5. Open Jenkins at http://localhost:8080/.
6. Create a Freestyle project named HelloWorld.
7. Configure Git under Source Code Management with the GitHub repository URL.
8. Add an Execute shell build step.
9. Enter the command sh hello-world.sh.
10. Save the job and click Build Now.
11. Open the build Console Output and verify the result.

## GitHub Repository
https://github.com/PruthviHegde123/devops-sample-code

## Expected Output
Hello, Jenkins!
Finished: SUCCESS

## Result
The HelloWorld Jenkins Freestyle job retrieved the shell script from GitHub, executed it successfully, and displayed Hello, Jenkins! in the console.

## Screenshots
The screenshots directory contains evidence of the Jenkins dashboard and successful build output.

## Conclusion
This exercise demonstrates how Jenkins integrates with GitHub and executes a shell script through a Freestyle project.
