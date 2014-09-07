

#packages/elementtree-1.2.6-20050316.tar.gz
#packages/supervisor-3.0.tar.gz

#python setup.py bdist_rpm

startDir=$(pwd)



files=( )
files+=("Babel-1.3")
files+=("birkenfeld-sphinx-135030faa775")
files+=("docutils-0.12")
files+=("elementtree-1.2.6-20050316")
files+=("Jinja2-2.7.3")
files+=("MarkupSafe-0.23")
files+=("meld3-0.6.5" "supervisor-3.0")
files+=("Pygments-1.6")
files+=("pywatch-0.4")
files+=("pytz-2014.4")
files+=("setuptools-3.8.1")
files+=("six-1.7.3")
files+=("snowballstemmer-1.2.0")
files+=("sphinx-bootstrap-theme-master")



for file in "${files[@]}"
do
   :
   cd $startDir
   rm -rf /tmp/$file
   mkdir /tmp/$file
   cp ../packages/python/$file.tar.gz /tmp/$file/$file.tar.gz
   cd /tmp/$file
   tar -zxvf $file.tar.gz
   cd $file
   
   cat <<EOF > clean.txt
   #shamoan MOFO
EOF

    #python setup.py install --single-version-externally-managed -O1 --root=\$RPM_BUILD_ROOT --record=INSTALLED_FILES

    cat <<EOF > install.txt

    python setup.py install -O1 --root=\$RPM_BUILD_ROOT --record=INSTALLED_FILES
    
    sed -i -e 's/.*/"\/\0"/' INSTALLED_FILES
EOF

    
    if [[ $file == "supervisor-3.0" ]]
    then
    cat <<EOF >> install.txt
%{__mkdir} -p \$RPM_BUILD_ROOT%{_sysconfdir}/supervisor.d
echo '%dir %{_sysconfdir}/supervisor.d' >> INSTALLED_FILES
#cp INSTALLED_FILES /tmp/INSTALLED_FILES_BACKUP
EOF
    
fi

    #python setup.py bdist_rpm --install-script=install.txt --clean-script clean.txt
    python setup.py bdist_rpm --install-script=install.txt
    
    #python setup.py bdist_rpm
    
    rc=$?
    if [[ $rc != 0 ]] ; then
        echo "Failed to build rpm ${file}"
        exit $rc
    fi



    cp dist/*.x86_64.rpm $startDir/../repo/RPMS/x86_64
    cp dist/*.noarch.rpm $startDir/../repo/RPMS/noarch
    cp dist/*.src.rpm $startDir/../repo/SRPMS/noarch
done

cd $startDir
createrepo $startDir/../repo/RPMS
createrepo $startDir/../repo/RPMS/x86_64
createrepo $startDir/../repo/RPMS/noarch



