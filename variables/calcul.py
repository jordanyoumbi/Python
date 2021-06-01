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

      
 select  a.third_party_id, a.national_id, b.targeting_id, c.code, d.eligible, d.validity_end_date, e.code from xmk.external_offer_targeted_third_party a

   inner join xmk.touch_point c on (c.code='EDT')

   inner join xmk.external_service_offer e on (e.code='CYBER-RISK')

   inner join xmk.third_party_vs_external_offer_eligibility d on (d.external_offer_targeted_third_party_id = a.id and d.external_service_offer_id=e.id and d.eligible=true and d.clinched_partner_journey=false and d.validity_end_date > '2021-03-01')

   inner join xmk.external_offer_third_party_touch_point b on (b.touchpoint_id = c.id and b.third_party_vs_external_offer_eligibility_id = d.id)
;
