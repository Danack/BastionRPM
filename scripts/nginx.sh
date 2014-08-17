#https://stereochro.me/ideas/rpm-for-the-unwilling


startDir=$(pwd)
. ./setupDirectory.sh

cp ../spec/nginx.spec $RPM_DIR/SPECS/nginx.spec
cp ../ini/nginx/* $RPM_DIR/SOURCES/

#cp ../ini/nginx.conf $RPM_DIR/SOURCES/nginx.conf
#cp ../ini/nginx.sysconf $RPM_DIR/SOURCES/nginx.sysconf
#cp ../ini/nginx.init $RPM_DIR/SOURCES/nginx.init
#cp ../ini/nginx.logrotate $RPM_DIR/SOURCES/logrotate


cp ../packages/nginx-1.7.4.tar.gz $RPM_DIR/SOURCES/nginx-1.7.4.tar.gz
cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/nginx.spec

cp SRPMS/nginx-1.7.4-1.el6.ngx.src.rpm   $startDir/../repo/SRPMS/nginx-1.7.4-1.el6.ngx.src.rpm
cp RPMS/x86_64/nginx-1.7.4-1.el6.ngx.x86_64.rpm  $startDir/../repo/RPMS/x86_64/nginx-1.7.4-1.el6.ngx.x86_64.rpm
cp RPMS/x86_64/nginx-debug-1.7.4-1.el6.ngx.x86_64.rpm $startDir/../repo/RPMS/x86_64/nginx-debug-1.7.4-1.el6.ngx.x86_64.rpm
 


createrepo $startDir/../repo/SRPMS
createrepo $startDir/../repo/RPMS/x86_64





