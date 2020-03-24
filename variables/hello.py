print('Hello')
spain = 95
france = 82
print(france)
france_type = type(france)
print(france_type)
# nombre àvirgule // float
france_exact = 11.5
print(type(france_exact))
# chaine de caractè /string
hello = 'hello'
hello_world = "hrllo world"
print(hello)
print(type(hello))
# les booleen /boolean type de variable qui renvoi vrai ou faux
true_type = True
false_type = False
print(true_type)
print(type(true_type))
# convertir un type de donnees
# str() to int() et vice-versa

int_to_str = str(2)   #ici on a une chaine de caractere dans le str parceque il y a pas les guillements autour de 2
print(int_to_str)
print(type(int_to_str)) # le type que l' on obtiendra ici est un string

str_to_int = int("2")
print(str_to_int)
print(type(str_to_int))

apiVersion: v1
kind: Service
metadata:
  name: xmk-admin-lb-private
  annotations:
   service.kubernetes.io/ibm-load-balancer-cloud-provider-ip-type: private
spec:
  ports:
    - protocol: TCP
      port: 80      
      targetPort: 80
  selector:
    run: xmk-admin-private
  type: LoadBalancer
--- 
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: xmk-admin-dp-private
spec:
  replicas: 2
  template:
    metadata:
      labels:
        run: xmk-admin-private
    spec:
      containers:
      - name: xmk-admin-private
        image: de.icr.io/xmk-admin/xmk-admin:48-20200320215821
        ports:
        - containerPort: 80
        - containerPort: 443
