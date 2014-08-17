

execute 'centos_disable_iptables' do
    cwd "/tmp"
    command  "service iptables stop"
end

bash "centos_alias_php" do
    user "root"
    cwd "/tmp"
    code <<-EOT
       echo "alias php='/usr/local/bin/php'" >> /root/.bashrc
    EOT
    not_if "grep /root/.bashrc /usr/local/bin/php"
end
