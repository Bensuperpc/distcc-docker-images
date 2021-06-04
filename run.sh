
# https://medium.com/@konrad.wilhelm.kleine/3-tips-to-make-your-cxx-projects-compile-5-times-faster-3847eee9d55c
docker run \
  -p 3632:3632 \
  -p 3633:3633 \
  -d \
  --name localdistcc \
  bensuperpc/distcc
#--allow
#docker exec -it localdistcc htop
#--cpus="1.5"