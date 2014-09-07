


# sh apcu.sh
# sh yaml.sh


#sh ImageMagick.sh
#sh nginx.sh
#sh php.sh
#sh xdebug.sh
#sh imagick.sh
#sh redis.sh
#sh python.sh

packages=( "ImageMagick" "nginx" "php" "xdebug" "imagick" "redis" "python" )
for package in "${packages[@]}"
do
   :
   sh "${package}.sh"

   if [[ $rc != 0 ]] ; then
       echo "Failed to build package ${package}"
       exit $rc
   fi
done   




/usr/local/bin/php ../src/makeHTML.php