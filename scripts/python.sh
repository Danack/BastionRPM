

#packages/elementtree-1.2.6-20050316.tar.gz
#packages/supervisor-3.0.tar.gz

#python setup.py bdist_rpm

startDir=$(pwd)



files=( "elementtree-1.2.6-20050316" "meld3-0.6.5" "supervisor-3.0" "setuptools-3.8.1" )
for file in "${files[@]}"
do
   :
   cd $startDir
   mkdir /tmp/$file
   cp ../packages/$file.tar.gz /tmp/$file/$file.tar.gz
   cd /tmp/$file
   tar -zxvf $file.tar.gz
   cd $file
   
   python setup.py bdist_rpm 
   
   cat <<EOF > install.txt
   python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
   #cp INSTALLED_FILES INSTALLED_FILES_BACKUP
   sed -i -e 's/.*/"\/\0"/' INSTALLED_FILES
EOF

   python setup.py bdist_rpm --install-script install.txt

   cp dist/*.noarch.rpm $startDir/../repo/RPMS/noarch
   cp dist/*.src.rpm $startDir/../repo/SRPMS/noarch
done

cd $startDir
createrepo $startDir/../repo/RPMS



