# 2024-March-11 Cloud and Semester Introduction

## Initial Brainstorming Session - Technologies and Motivators for Distributed Systems

![Brainstorming](/pics/2024-03-11-DistributedSystemsBrainstorm.png)

### Content

* Why distributed systems, why container, why modern software?
* What is Cloud Computing? Encounters in everyday life and history
* Characteristic, advantages & challenges
* Terminology - public, private, hybrid, dedicated
* Abstraction layers - IaaS, PaaS, FaaS, SaaS
* Overview - Hypervisors, virtual machines, containers and orchestration

### Objectives and exercises
_The student is able to describe the reasons for distributed systems and
cloud computing in own words and list examples for offerings, topologies and technologies. Includes ability to differentiate between different abstraction layers and knowledge how those layers and according technologies interact with each other. No exercises in this module_

### Student Questions

* What is Polyglot Software Development?
* What did the role of containers change for polyglot software?
* Security and Cloud - is it safe? :-)

![Polyglot Container](/pics/2024-03-11-ContainerVsTraditional.png)

### Outlook for Labs

* Distributed app
* Polyglot implementation
* Containerisation
* Kubernetes
* DevOps/CICD/Observability (optional)

![Exercise Tech Stack](/pics/2024-03-11-Blackboard.jpg)

### Homework

* Get a public GitHub, GitLab or Bitbucket account
* Play around with GitHub codespaces and/or Gitpod
  
# 2024-March-18 Session canceled

# 2024-March-25 Cloud-based IDEs Intro & Docker/Container

### Content 
* Why do we need Containers?
* Challenges for (polyglot) distributed systems in traditional IT:

  * Each environment has to be configured manually: Servers as well as local dev environments
  * Configuration has to be as identical as possible: minor configuration drifts can lead to errors and the "it runs on my machine" problem
  * Polyglot Server Environments are a huge challenge as for each programing language a separate configuration has to be managed on all systems.
  * Changing Versions is tedious for local dev environment

  ![image](https://github.com/maeddes/hse-24-summer/assets/22505258/63a76e4b-cd0e-4f9d-8e6e-cb7b364d4581)

  * Whereas containerized Applications bring their own Environment and Configuration
  * No need to preconfigure the local environment per programming language or application.
  * Only the container engine is required to run all kinds of containers.
    
 ![image](https://github.com/maeddes/hse-24-summer/assets/22505258/35dfe922-1c43-46db-a419-4c602dd084dc)

 * How does the container engine work?
 * Layer-based setup of containers
 * Container vs Container Image
 * How to create a container from application to dockerfile to image to running container

  ![image](https://github.com/maeddes/hse-24-summer/assets/22505258/bcad4374-da59-429a-8272-1b42642c888c)

### Student Questions:
* Do I have to set up, build, and run the dockerfile  for each container?
* Can I run multiple applications inside a container?

### Labs
Exercises can be found [here](https://lecture.new.trainings.nvtc.io/basics/container/)


# 2024-April-8th Spring Boot Intro & HTTP/REST 

## Spring Boot

![Spring Boot typical flow](https://raw.githubusercontent.com/maeddes/hft-2022-winter/main/pics/spring_boot_initializr_flow_2022_10_17.png)

* Background: Spring Framework - History & components
* Spring ← → Spring Boot
* Spring Initializr (start.spring.io) & starter dependencies
* Basic project structure (folders, configuration ..)
* "Hello, World!" example explained
* Using Actuator

### Objectives

The student is able to build and configure an own Spring Boot application from scratch with the IDE of choice. The exercise is to build an own "Hello, World!" application that exposes various - endpoints and is able to execute CRUD operations on the state of the application. Optional: Add logging and testing, configure Actuator.

### Review questions

* "WHY Spring Boot?" Provide 3 advantages of this framework
* Describe Spring Boot to somebody not familiar with it in own words ()
* How do you start building a Spring Boot app? Initializr & Dependencies
* List 4 different starter dependencies and explain briefly what they do (old question) (4P)
"I did not do my lab task with Spring Boot. I implemented using Python and I can tell you how it works there ..."

### Helpful Links:

- https://start.spring.io
- https://www.baeldung.com/spring-requestmapping
- https://www.baeldung.com/spring-boot-actuator-enable-endpoints

## REST

![REST, Controllers, Representations](https://github.com/maeddes/hft-23-winter/blob/main/pics/REST_stuff.png)

* Synchronous communication
* HTTP and REST
* Verbs, Resources, Nouns
* Evolution, Richardson Maturity Model
* CRUD Operations
* Building a REST API with Spring (Boot)
* Building a data model with REST

### Links:

* https://restfulapi.net/idempotent-rest-apis/
* https://restfulapi.net/richardson-maturity-model/
* https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

* https://www.baeldung.com/spring-requestmapping
* https://www.baeldung.com/spring-request-response-body
* https://www.baeldung.com/spring-rest-openapi-documentation
* https://www.baeldung.com/spring-cors

### Review questions

* Identify good and bad API examples and explain why
* Describe the concepts of Verbs and Nouns
* When is an invocation idempotent and safe? What does it mean? Provide examples
* Describe in your own words the mapping of REST calls to database (SQL) and CRUD calls

### Objectives and exercises
_The student understands the concepts of an API and synchronous communication in distributed systems and can explain it in own words._

# 2024-April-15th Distributed Application Sample / Outlook Lab / Docker Advanced topics - TODO :-)

# 2024-April-22nd Cloud-native Software development - Theory part

Cloud-native Software development - Theory part

Theory lecture - Cloud-Native Software 

* CAP Theorem
* Conway's Law
* Fallacies of distributed computing
* Domain-Driven Design basics (not relevant for exam)
* 12-factor application
* Evolution of applications and deployments: Monolithic -> Service-Oriented Architecture -> Microservices
* Introduction to serverless and FaaS terminology

### Objectives and exercises
_The student knows about the evolution of distributed systems (and middleware) and the drivers towards state-of-the-art implementation and deployment. She/he can explain the underlying concepts and theories and put it into practical context. No dedicated exercises for this module. Recap of basics: Spring Boot, Docker, configuration._

### Review questions

* "WHY" Cloud-Native Software? What IS Cloud-Native Software?
* Why "evolution" from a monolithic approach to a distributed approach?
* How does the CAP Theorem/Conway's Law relate to this?
* (NO Domain-Driven Design questions)
* How do the 12-factor application "methodology" relate to the technologies that we covered in this semester? (important)
* "WHY" is external configuration important in cloud-native software?
* Where did you see aspects of external configuration in the technologies we used? Provide examples
* What is the advantage of polyglot applications? Why in particular for cloud-native software? What kind of disadvantages do you see?
