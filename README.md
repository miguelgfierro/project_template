# Machine Learning project template

The objective of this repository is to serve as a template for machine learning projects.

## Getting Started

To set up the project, the easiest way is to copy the all the folders into an empty GitHub repository. Make sure you change the name of the library `miguellib`.

## Structure

- .github: CI/CD with GitHub Actions. It runs the tests every time there is a pull request to the repository.
- docs: Documentation of the project.
- examples: Jupyter notebooks with machine learning experiments. Here is where you would do data exploration, try different machine learning models, etc.
- miguellib: Libraries with common functions that you use in the project. 
- tests: Python tests of the libraries.

## Setup

    pip install -e .
    python -c "import miguellib; print(miguellib.__version__)"

## Coding Principles

Next there are a few coding principles that I follow when working on machine learning projects.

### Start from something that works

Here is one of the most practical tips I know about working on machine learning. **Instead of starting from scratch, start with something that works and adapt it to your problem.**

For example, let's say you want to build a recommendation system with data from your company. What I would do is something as simple as this:

1. Go to [Recommenders](https://github.com/recommenders-team/recommenders) and look at an example that a similar dataset structure and compute. For example, if your data is text-based and you want to use GPU, explore the examples of LSTUR or NPA.
2. Install the dependencies and run the example. Make sure that it works.
3. Change the data of the example to your data. If your data is different or more extensive, just forget about it and use the part of your data that is similar to the example. Make sure that it works.
4. Change the code to adapt it to your specific data and problem.

### Notebooks that call a library

One of the main differences between a professional and an amateur machine learning project is this. Don't put your functions and classes in the notebooks, instead, create libraries and call them from the notebooks. This is the only way to reuse your code and make it scalable. 

Most of the time, notebooks are not deployed, they are used for experimentation and visualization. You deploy the libraries. In addition, if you create libraries, you can test them.

### Why tests are important?

Tests solve one of the most expensive problems in development: maintenance. The way I see testing is like the immune system of your project. It protects your project from bugs and errors and makes sure your project is healthy. 

A strong test pipeline minimizes maintenance. It is one of the best investments you can do in your project, because it will avoid new buggy code in the project, and it will detect breaking changes when using dependencies.
