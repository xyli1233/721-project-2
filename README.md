# 721-project-2
a simple calculator deplyed to kubernets and docker
1. docker build -t $name/721p2 .
2. docker push $name/721p2  push the image
3. minikube start
4. minikube dashboard --url 
5. kubectl create deployment hello-fastapi --image=registry.hub.docker.com/$name/721p2
6. kubectl expose deployment hello-fastapi --type=LoadBalancer --port=8080
7. kubectl get service hello-fastapi
8. minikube service hello-fastapi --url
curl http://127.0.0.1:51594/substract/1/2
