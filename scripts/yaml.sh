#https://stereochro.me/ideas/rpm-for-the-unwilling


startDir=$(pwd)
. ./setupDirectory.sh

cp ../spec/php-yaml.spec $RPM_DIR/SPECS/php-yaml.spec
cp ../ini/yaml.ini $RPM_DIR/SOURCES/yaml.ini

cp packages/yaml-1.1.0.tgz $RPM_DIR/SOURCES/yaml-1.1.0.tgz
cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/php-yaml.spec

cp RPMS/x86_64/yaml-1.1.0-1.x86_64.rpm  $startDir/../repo/RPMS/x86_64/yaml-1.1.0.x86_64.rpm
cp SRPMS/yaml-1.1.0-1.src.rpm  $startDir/repo/SRPMS/../yaml-1.1.0-1.src.rpm

createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





