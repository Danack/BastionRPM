


startDir=$(pwd)

. ./setupDirectory.sh

pythonTempDir=${startDir}/../temp/pythonBuild 

mkdir -p ${pythonTempDir}


files=( )
files+=("Babel-1.3")
files+=("birkenfeld-sphinx-135030faa775")
files+=("docutils-0.12")
files+=("elementtree-1.2.6-20050316")
files+=("Jinja2-2.7.3")
files+=("MarkupSafe-0.23")
files+=("meld3-0.6.5")
files+=("Pygments-1.6")
files+=("pywatch-0.4")
files+=("pytz-2014.4")
files+=("setuptools-3.8.1")
files+=("six-1.7.3")
files+=("snowballstemmer-1.2.0")
files+=("sphinx-bootstrap-theme-master")
files+=("supervisor-3.0")



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
EOF


    #Prepare an install script
    cat <<EOF > install.txt
    python setup.py install -O1 --root=\$RPM_BUILD_ROOT --record=INSTALLED_FILES
    sed -i -e 's/.*/"\/\0"/' INSTALLED_FILES
EOF

    #SupervisorD needs an entry in the sysconfdir - aka /etc/
    #for most systems.
    if [[ $file == "supervisor-3.0" ]]
    then

    cat <<EOF >> install.txt
%{__mkdir} -p \$RPM_BUILD_ROOT%{_sysconfdir}/supervisor.d
echo '%dir %{_sysconfdir}/supervisor.d' >> INSTALLED_FILES

%{__mkdir} -p \$RPM_BUILD_ROOT/var/log/supervisor
echo '%dir /var/log/supervisor' >> INSTALLED_FILES

cp ${startDir}/../packages/python/supervisord.conf \$RPM_BUILD_ROOT/etc/supervisord.conf
chmod 660 \$RPM_BUILD_ROOT/etc/supervisord.conf
echo '/etc/supervisord.conf' >> INSTALLED_FILES

%{__mkdir} -p \$RPM_BUILD_ROOT/etc/init.d
echo '%dir %{_sysconfdir}/init.d/supervisord' >> INSTALLED_FILES
cp ${startDir}/../packages/python/supervisord.init.d \$RPM_BUILD_ROOT/etc/init.d/supervisord
chmod 766 \$RPM_BUILD_ROOT/etc/init.d/supervisord
echo '/etc/init.d/supervisord' >> INSTALLED_FILES

%{__mkdir} -p \$RPM_BUILD_ROOT/etc/logrotate.d
cp ${startDir}/../packages/python/supervisord.logrotate \$RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/supervisord
chmod 644 \$RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/supervisord
echo '/etc/logrotate.d/supervisord' >> INSTALLED_FILES

EOF

#TODO - I can copy to the sources dir first and then have a slightly better install process?
    
fi

    python setup.py bdist_rpm --install-script=install.txt
    
    rc=$?
    if [[ $rc != 0 ]] ; then
        echo "Failed to build rpm ${file}"
        exit $rc
    fi
    
    cp dist/*.rpm ${pythonTempDir}

done

rpm --resign ${pythonTempDir}/*.rpm

#copy the built files to the repo directory
cp ${pythonTempDir}/*.x86_64.rpm $startDir/../repo/RPMS/x86_64
cp ${pythonTempDir}/*.noarch.rpm $startDir/../repo/RPMS/noarch
cp ${pythonTempDir}/*.src.rpm $startDir/../repo/SRPMS/noarch


createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/noarch
createrepo $startDir/../repo/RPMS/x86_64

#. ${startDir}/copyAndRepo.sh

#cd $startDir
#createrepo $startDir/../repo/RPMS
#createrepo $startDir/../repo/RPMS/x86_64
#createrepo $startDir/../repo/RPMS/noarch



