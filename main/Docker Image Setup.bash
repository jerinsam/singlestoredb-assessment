
## Get SingleStore Image for Docker
docker run -i --init --name singlestore-ciab -e LICENSE_KEY="BDkzMzAzOTA3MmI5MjQyMDNiZGEyZGQwN2E2ODM3ZjAzAAAAAAAAAAAEAAAAAAAAACgwNAIYO7kOr5wICCHwJv0ObUnRW14tfDtXh2iRAhhLv643Dy6RUE+R+BIJUmBCu99oJ2nfFQ8AAA==" -e ROOT_PASSWORD="jerin" -p 3306:3306 -p 8080:8080 singlestore/cluster-in-a-box


## Start the Container
docker start singlestore-ciab