
template "/etc/yum.repos.d/basereality.repo" do
  source "basereality.repo.erb"
  owner "root"
  group "root"
  mode 00600
end


execute 'add_rpm_epel' do
  command 'wget -O /tmp/epel-release-6-8.noarch.rpm http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm && rpm -Uvh /tmp/epel-release-6-8.noarch.rpm'
  not_if "rpm -qa | grep epel-release-6-8.noarch"
end

template "/etc/yum.repos.d/epel.repo" do
  source "epel.repo.erb"
  owner "root"
  group "root"
  mode 00600
end


#execute 'add_rpm_remi' do
#  command 'wget -O /tmp/remi-release-6.rpm http://rpms.famillecollet.com/enterprise/remi-release-6.rpm && rpm -Uvh /tmp/remi-release-6.rpm'
#  # not_if "rpm -qa | grep remi-release-6-2.el6.remi.noarch"
#  not_if "rpm -qa | grep remi-release-6.4-1.el6.remi.noarch"
#end


# execute 'add_percona' do
#  command 'rpm -Uhv http://www.percona.com/downloads/percona-release/percona-release-0.0-1.x86_64.rpm'
#  not_if "rpm -qa | grep percona"
# end