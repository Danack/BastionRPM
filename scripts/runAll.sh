

packages=( )
packages+=("Babel-1.3")


packages+=("ImageMagick")
packages+=("imagick")
packages+=("libyaml")
packages+=("nginx")
packages+=("php")
packages+=("python")
packages+=("redis")
packages+=("valgrind")
packages+=("xdebug")
packages+=("yuicompressor")


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