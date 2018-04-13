require 'nexy/cli/base'

module Nexy
  class CLI::Setup < CLI::Base
    def run
      if Nexy::Config.config_file_exists?
        update_existing_config!
      else
        create_new_config!
      end
    end

    private

    def update_existing_config!
      ui.say("An existing config file was found at: #{Nexy::Config::CONFIG_PATH}")
    end

    def create_new_config!
      ui.say("Let's set up nexy to work for you!")
    end
  end
end
