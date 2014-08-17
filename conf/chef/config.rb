file_cache_path  "/var/chef"
cookbook_path    Dir.pwd  + "/conf/chef/cookbooks"

data_bag_path    Dir.pwd  + "/conf/chef/data_bags"

environment_path Dir.pwd  + "/conf/chef/environment"


log_level        :info
# log_location     "/var/log/chef.log"  # or STDOUT
verbose_logging  true
# json_attribs    "/tmp/chefsolo.json"

# node_name