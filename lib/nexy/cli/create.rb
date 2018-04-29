require 'nexy/cli/base'

module Nexy
  class CLI::Create < CLI::Base
    def self.required_keys
      ['projects_path']
    end

    def run
      ui.say("Let's create a new project!")
    end
  end
end
