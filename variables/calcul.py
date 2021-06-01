#puissance 2 / puissance au carre
square = 5 
squared = square ** 2
print(squared)

#Division
divide_france = square / 2
print(divide_france)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: xmk-admin-private
  labels:
    app: xmk-admin-private
spec:
  replicas: 2
  selector:
    matchLabels:
      app: xmk-admin-private
  template:
    metadata:
      labels:
        app: xmk-admin-private
    spec:
      containers:
      - name: xmk-admin-private
#        image: nginx:1.14.2
        image: de.icr.io/xmk-admin/xmk-admin:48-20200320215821
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
 name: xmk-admin-lb-private
 annotations:
   service.kubernetes.io/ibm-load-balancer-cloud-provider-ip-type: private
spec:
 type: LoadBalancer
 selector:
   app: xmk-admin-private
 ports:
  - protocol: TCP
    port: 80
    targetPort: 80

     
