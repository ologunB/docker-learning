# ML Docker Example

This project demonstrates how to use Docker to containerize a simple machine learning application that predicts housing prices based on specific features such as area, number of bedrooms, and number of bathrooms.

## Table of Contents

- [Project Overview](#project-overview)
- [Why Use Docker?](#why-use-docker)
- [Features](#features)
- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [Making Predictions](#making-predictions)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This machine learning application uses a linear regression model trained on a dataset of housing prices. It takes input parameters via a RESTful API and predicts the price of a house based on its features. The model is built using Python and utilizes libraries like Flask, Pandas, and scikit-learn.

## Why Use Docker?

Docker provides a consistent and reproducible environment for your applications. By containerizing the application, we can ensure that it runs the same way regardless of where it is deployed. Some key benefits include:

- **Isolation**: Each Docker container runs in its own environment, preventing conflicts between dependencies.
- **Portability**: The application can be easily moved across different environments (development, testing, production) without modification.
- **Scalability**: Docker makes it easy to scale applications by running multiple instances of containers.
- **Simplified Deployment**: Using Docker allows for simpler deployment processes and easier management of dependencies.

## Features

- Predicts housing prices based on area, number of bedrooms, and bathrooms.
- RESTful API built with Flask for making predictions.
- Dockerized application for easy deployment and scalability.
- Simple and intuitive interface for making predictions.

## Getting Started

### Prerequisites

To run this project, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- A terminal or command prompt for running commands.

### Running the Application

1. **Clone the Repository**: Copy the project files into a directory called `ml-docker-example`.
   ```bash
   git clone https://github.com/yourusername/ml-docker-example.git
   cd ml-docker-example
   ```

2. **Build the Docker Image**:
   Run the following command to build the Docker image:
   ```bash
   docker build -t ml-docker-example .
   ```

3. **Run the Docker Container**:
   After building the image, run the following command to start the container:
   ```bash
   docker run -p 5000:5000 ml-docker-example
   ```

4. The application will now be running locally on port 5000.

## Making Predictions

To make predictions using the model, send a POST request to the `/predict` endpoint. You can use `curl` or any API client like Postman.

### Example using curl:

```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"Area": 1600, "Bedrooms": 3, "Bathrooms": 2}'
```

### Sample Request Body:

```json
{
  "Area": 1600,
  "Bedrooms": 3,
  "Bathrooms": 2
}
```

### Example Response:

```json
{
  "predicted_price": 320000
}
```

## Dependencies

The application relies on the following Python libraries, which are included in the `requirements.txt` file:

- Flask
- Pandas
- scikit-learn

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.