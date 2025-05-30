# Minikube-and-Kucetl
# Minikube and Kucetl Lab Setup

To work with Kubernetes on your local laptop using Minikube and kubectl, follow these steps. Below is an example of how to set up, deploy, and manage a basic Kubernetes cluster using Minikube and kubectl.

### Prerequisites:
1. **Install Minikube**: Minikube runs a local Kubernetes cluster in a virtual machine (VM).
2. **Install kubectl**: kubectl is the command-line tool for interacting with Kubernetes.

### Step-by-step Example:

#### Step 1: Install Minikube and kubectl
First, make sure you have Minikube and kubectl installed.

- **For Minikube**:
  - **Linux**: `curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64`
  - **macOS**: `brew install minikube`
  - **Windows**: Use [Chocolatey](https://chocolatey.org/) (`choco install minikube`)

- **For kubectl**:
  - **Linux/macOS**: `curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"`
  - **Windows**: Download [kubectl for Windows](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/)

#### Step 2: Start Minikube
Start a Kubernetes cluster using Minikube.

```bash
minikube start
```

This will initialize a local Kubernetes cluster inside a virtual machine.

#### Step 3: Verify Cluster
To verify that the Minikube cluster is running, you can use the following command:

```bash
kubectl get nodes
```

This should display a node with a `Ready` status, showing that your local cluster is up.

#### Step 4: Create a Deployment
Now, let’s create a simple Kubernetes deployment using a container image. For example, you can deploy a simple nginx web server.

```bash
kubectl create deployment nginx --image=nginx
```

This command tells Kubernetes to create a deployment named `nginx`, using the official `nginx` image.

#### Step 5: Expose the Deployment
Next, you need to expose your deployment to make it accessible. You can expose it through a service:

```bash
kubectl expose deployment nginx --type=NodePort --port=80
```

This will expose the `nginx` deployment via a NodePort, which is accessible on a port in the range `30000-32767`.

#### Step 6: Get the URL for Access
After exposing the deployment, you need to get the URL to access the service. Minikube provides an easy way to access it:

```bash
minikube service nginx --url
```

This will provide a URL, like `http://192.168.99.100:30001`, that you can use to access your nginx web server.

#### Step 7: Check Running Pods
You can check the status of the pods running in your Kubernetes cluster:

```bash
kubectl get pods
```

You should see the pod for `nginx` listed with a `Running` status.

#### Step 8: Scale the Deployment
You can scale your deployment to increase or decrease the number of replicas (pods) running.

For example, to scale to 3 replicas:

```bash
kubectl scale deployment nginx --replicas=3
```

To verify the scaling, check the pods again:

```bash
kubectl get pods
```

#### Step 9: Deleting the Deployment
When you're done and want to clean up, you can delete the deployment and service:

```bash
kubectl delete service nginx
kubectl delete deployment nginx
```

### Example of Working Kubernetes Command Flow:

```bash
# Start Minikube
minikube start

# Verify Minikube and Kubernetes cluster status
kubectl get nodes

# Create a deployment for nginx
kubectl create deployment nginx --image=nginx

# Expose the nginx deployment
kubectl expose deployment nginx --type=NodePort --port=80

# Get the URL of the exposed service
minikube service nginx --url

# Check the status of running pods
kubectl get pods

# Scale the nginx deployment to 3 replicas
kubectl scale deployment nginx --replicas=3

# Clean up (delete service and deployment)
kubectl delete service nginx
kubectl delete deployment nginx
```

### Conclusion:
By using Minikube and kubectl on your local laptop, you can easily create, manage, and scale Kubernetes deployments. Minikube is an excellent tool for setting up a local cluster to test and experiment with Kubernetes before deploying to a production environment.
