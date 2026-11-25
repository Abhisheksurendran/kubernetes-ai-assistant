# AI-Powered Kubernetes Assistant

An AI-powered DevOps project designed to investigate Kubernetes cluster health, analyse application failures, and provide actionable troubleshooting recommendations.

## Project Objectives

- Connect to a Kubernetes cluster using Python.
- Monitor nodes, pods, deployments and services.
- Detect unhealthy pods and CrashLoopBackOff issues.
- Analyse Kubernetes events and container logs.
- Integrate AI for root-cause analysis.
- Integrate Prometheus for resource monitoring.
- Recommend fixes with approval-based remediation.

## Technology Stack

- Python
- Kubernetes Python Client
- Kubernetes
- Docker
- OpenAI API
- FastAPI
- Prometheus
- Grafana
- Git and GitHub

## Current Progress

- [x] Python virtual environment setup
- [x] Kubernetes Python Client installation
- [x] Kubernetes node information retrieval
- [x] Kubernetes pod information retrieval
- [ ] Automatic unhealthy pod detection
- [ ] Log and event analysis
- [ ] AI integration
- [ ] Prometheus integration
- [ ] Controlled remediation
- [ ] Kubernetes deployment

## Architecture

The Python application communicates with the Kubernetes API server to retrieve cluster information. An AI agent will analyse the collected information and provide troubleshooting recommendations.

## Author

Abhishek Surendran

GitHub: https://github.com/Abhisheksurendran
