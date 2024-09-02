[project]
name = "fishmlserv"
version = "0.7.0"
description = "Machine Learning Model - using sklearn(KNeighborsClassifier) using FastApi, Fly.io"
authors = [
    {name = "hahahellooo", email = "hahahello777@gmail.com"},
]
dependencies = [
    "fastapi>=0.112.2",
    "uvicorn[standard]>=0.30.6",
    "matplotlib>=3.9.2",
    "scikit-learn>=1.5.1",
]
requires-python = ">=3.8"
readme = "README.md"
license = {text = "MIT"}


[tool.pdm]
distribution = false

[tool.pdm.dev-dependencies]
note = [
    "notebook>=7.2.2",
]
