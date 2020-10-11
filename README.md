## DOCKER Capabilities with FLASK, MONGODB, MONGOEXPRESS

## STEPS

1. git clone this repo
2. check the folder structure
3. ensure you have docker, docker-compose
4. docker-compose -f deployments/docker-compose.yml up --scale app=<1,6> --build --force-recreate -V -d
5. open MongoEXpress http://localhost:8985
6. create a database "mini_test"
7. create a collection "products"
8. update datafile.son ( first product)
9. call localhost:<11920,11925>/
    * /fetch
    */import => not updated
    */ => initial info

## CONTACT
vazudew@gmail.com :rocket2: