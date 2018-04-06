require 'yaml'


module Nexy
  module Config
    extend self

    CONFIG_PATH      = '~/.nexy'
    FULL_CONFIG_PATH = File.expand_path(CONFIG_PATH)

    def config_file_exists?
      File.file?(FULL_CONFIG_PATH)
    end
  end
end