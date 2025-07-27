# Flask Random Number Generator on Kubernetes

This project demonstrates deploying a simple Flask application to Kubernetes, complete with configuration, secrets, persistent storage, monitoring, and scaling. The application exposes a `/random` endpoint that returns a random number within a configurable range.

## Project Structure tree

```
.
├── .gitignore
├── cronjob.yaml
├── deployment.yaml
├── flask-hpa.yaml
├── metrics_pvc.yaml
├── pod-metrics-binding.yaml
├── pod-metrics-role.yaml
├── random-range-configmap.yaml
├── service.yaml
├── docker/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── plus/
    ├── ab_bench.yaml
    ├── api_key.txt
    ├── cronjob-with-sidecar.yaml
    ├── nginx.conf
    ├── persistent-volume.yaml
    ├── pod.yaml
    ├── pv-claim.yaml
    ├── pv-volume.yaml
    └── test.env
```

## Components

### Flask Application

- **docker/app.py**: Flask app serving `/random`, configurable via environment variables.
- **docker/Dockerfile**: Containerizes the Flask app.
- **docker/requirements.txt**: Python dependencies.
- Currently published to docker.io/robolion1200/my_random_flask:1

### Kubernetes Manifests

- **deployment.yaml**: Deploys the Flask app with environment variables from a ConfigMap and Secret, and sets up health checks and resource limits.
- **service.yaml**: Exposes the Flask app as a LoadBalancer service on port 80.
- **random-range-configmap.yaml**: ConfigMap for min/max random values and app metadata. Also defines a Secret for sensitive data.
- **flask-hpa.yaml**: Horizontal Pod Autoscaler for the Flask deployment, scaling based on CPU usage.
- **metrics_pvc.yaml**: PersistentVolume and PersistentVolumeClaim for storing HPA monitoring logs.
- **cronjob.yaml**: CronJob that logs pod metrics to the persistent volume every 15 minutes.
- **pod-metrics-role.yaml** & **pod-metrics-binding.yaml**: RBAC for accessing pod metrics.

### Additional Resources (`plus/`)

- **ab_bench.yaml**: Pod for running Apache Bench load tests against the Flask service.
- **cronjob-with-sidecar.yaml**: CronJob with a sidecar container for archiving logs.
- **persistent-volume.yaml**: Defines a shared PersistentVolume and PersistentVolumeClaim.
- **pv-volume.yaml** & **pv-claim.yaml**: Additional PV and PVC for other pods.
- **pod.yaml**: Example pod using PVC, config, and an init container.
- **nginx.conf**: NGINX configuration for use in pods.
- **test.env**: Example environment file.
- **api_key.txt**: Example API key (not used in manifests).

## Usage

1. **Build and Push Docker Image**
   - Build the image from `docker/` and push to your registry.
2. **Apply Kubernetes Manifests**
   - Create ConfigMaps, Secrets, PVs, PVCs, then deploy the app and services:
     ```sh
     kubectl apply -f random-range-configmap.yaml
     kubectl apply -f metrics_pvc.yaml
     kubectl apply -f deployment.yaml
     kubectl apply -f service.yaml
     kubectl apply -f flask-hpa.yaml
     kubectl apply -f cronjob.yaml
     # ...and any additional resources as needed
     ```
3. **Access the Application**
   - Use the external IP of the LoadBalancer service to access `/random`.

## Endpoints

- `GET /random`: Returns a random number and app metadata.

## Scaling & Monitoring

- The app auto-scales based on CPU usage.
- Pod metrics are logged by a CronJob to persistent storage.

## License

MIT
