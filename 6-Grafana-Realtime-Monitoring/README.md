# Exercise 6: Grafana Real-Time Monitoring

## Aim
To monitor a delivery service using Prometheus metrics and Grafana dashboards.

## Tools Used
- Python
- Flask
- Prometheus
- Grafana
- Docker

## Overview
The application exposes delivery-service metrics that Prometheus can collect. Grafana uses Prometheus as its data source to visualize these metrics and monitor service activity.

## Metrics
The monitoring setup includes delivery-related metrics such as:
- Total deliveries
- Pending deliveries
- Deliveries on the way
- Average delivery time

## Configuration Files
- delivery_metrics.py: Application and metrics implementation.
- requirements.txt: Python dependencies.
- Dockerfile: Instructions for building the application image.
- prometheus.yml: Prometheus scrape configuration.
- alert_rules.yml: Alerting rule definitions.

## Verification
Prometheus was verified to return 21 result series for the query `{job="delivery_service"}`.

Grafana panels were configured, but one panel did not consistently display data. Complete visualization of every panel could not be verified.

## Conclusion
The exercise demonstrates exposing application metrics, collecting them with Prometheus, and visualizing monitoring data in Grafana.
