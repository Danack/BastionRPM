#https://stereochro.me/ideas/rpm-for-the-unwilling

startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/monit/monit.spec $RPM_DIR/SPECS/monit.spec
cp ../packages/monit/* $RPM_DIR/SOURCES/
cp ../zips/monit/monit-5.12.tar.gz $RPM_DIR/SOURCES/

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/monit.spec

. ${startDir}/copyAndRepo.sh



#cp ../packages/monit/monitrc $RPM_DIR/SOURCES/monitrc
#cp ../packages/monit/monit.logrotate $RPM_DIR/SOURCES/monit.logrotate
#cp ../packages/monit/monit-logging-conf $RPM_DIR/SOURCES/monit-logging-conf




